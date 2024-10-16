from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from text_to_speech import convert_text_to_speech
from voice_customization import train_custom_voice, synthesize_with_custom_voice
from audio_management import save_audio, delete_audio, get_audio_list
from speech_recognition import Recognizer, AudioFile
from flask_cors import CORS
import os

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tts_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)  # Enable CORS for all routes

# Directory to store uploaded files
temp_dir = "temp"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

class AudioFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    filename = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    voice_type = db.Column(db.String(50), nullable=False)
    voice_tone = db.Column(db.String(50), nullable=False)

class CustomVoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    voice_name = db.Column(db.String(100), nullable=False)
    voice_data = db.Column(db.LargeBinary, nullable=False)

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    existing_user = User.query.filter_by(username=data['username']).first()
    
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400  # Conflict status

    user = User(username=data['username'], password_hash=generate_password_hash(data['password']))
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        return jsonify({'message': 'Login successful', 'user_id': user.id})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    text = data.get('text', '')
    voice_type = data.get('voice_type', '')
    voice_tone = data.get('voice_tone', '')

    # Print the values for debugging
    print(f"Text: {text}, Voice Type: {voice_type}, Voice Tone: {voice_tone}")

    try:
        audio_file = convert_text_to_speech(text, voice_type, voice_tone)
        return jsonify({"audio_file": audio_file}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/api/files', methods=['GET'])
def get_files():
    try:
        # List all files in the output_files directory
        files = os.listdir('output_files')
        return jsonify([{'filename': f} for f in files]), 200
    except Exception as e:
        return jsonify({"error": f"Could not list files: {str(e)}"}), 500


@app.route('/api/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = os.path.join('output_files', filename)
    
    if os.path.exists(file_path):
        try:
            os.remove(file_path)  # Delete the file from the filesystem
            return '', 204  # Successfully deleted
        except Exception as e:
            return jsonify({"error": f"Could not delete file: {str(e)}"}), 500
    else:
        return jsonify({"error": "File not found"}), 404



@app.route('/api/voices', methods=['GET'])
def get_voices():
    voices = ['voice1', 'voice2', 'voice3']  # Sample voices
    return jsonify(voices)

@app.route('/api/train-voice', methods=['POST'])
def train_voice():
    voice_data = request.files['voice_data']
    user_id = request.form['user_id']
    voice_name = request.form['voice_name']
    
    success, voice_model = train_custom_voice(voice_data)
    if success:
        new_voice = CustomVoice(user_id=user_id, voice_name=voice_name, voice_data=voice_model)
        db.session.add(new_voice)
        db.session.commit()
        return jsonify({'message': 'Voice trained successfully'})
    return jsonify({'message': 'Voice training failed'}), 400

@app.route('/api/custom-voices', methods=['GET'])
def get_custom_voices():
    user_id = request.args.get('user_id')
    voices = CustomVoice.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': v.id, 'name': v.voice_name} for v in voices])

@app.route('/api/synthesize-custom', methods=['POST'])
def synthesize_custom():
    data = request.json
    text = data['text']
    voice_id = data['voice_id']
    
    custom_voice = CustomVoice.query.get_or_404(voice_id)
    audio = synthesize_with_custom_voice(text, custom_voice.voice_data)
    filename = save_audio(audio)
    
    return jsonify({'filename': filename})

def transcribe_audio(audio_file_path):
    # Initialize the recognizer
    recognizer = Recognizer()
    
    try:
        with AudioFile(audio_file_path) as source:
            audio = recognizer.record(source)  # Read the entire audio file
            text = recognizer.recognize_google(audio)  # Use Google Web Speech API
            return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/api/speech-to-text', methods=['POST'])
def speech_to_text():
   
    if 'audio_file' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio_file']

    # Save the uploaded audio file temporarily
    audio_file_path = os.path.join(temp_dir, audio_file.filename)

    try:
        audio_file.save(audio_file_path)  # Save the file
    except Exception as e:
        return jsonify({"error": f"Failed to save audio file: {str(e)}"}), 500

    # Transcribe the audio file
    transcription = transcribe_audio(audio_file_path)

    # Optionally, you can remove the file after processing
    os.remove(audio_file_path)

    return jsonify({"transcription": transcription}), 200

@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    # Ensure the audio files directory exists
    audio_files_path = os.path.join(temp_dir, filename)
    
    if not os.path.exists(audio_files_path):
        return jsonify({"error": "File not found"}), 404

    return send_file(audio_files_path, as_attachment=True)

# Route to list the generated audio files
@app.route('/api/list-audio-files', methods=['GET'])
def list_audio_files():
    try:
        # List all files in the output_files directory
        files = os.listdir(output_files)
        print(f"Files in output_files: {files}")  # Debug: list the files found
        return jsonify(files), 200
    except Exception as e:
        return jsonify({"error": f"Could not list files: {str(e)}"}), 500

# Create tables at startup
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensures the tables are created
    app.run(debug=True)
