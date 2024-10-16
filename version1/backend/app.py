from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from gtts import gTTS
import os
import uuid
import speech_recognition as sr
from pydub import AudioSegment  # For converting audio formats

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to generate meaningful filename
def convert_to_wav(file_path):
    audio = AudioSegment.from_mp3(file_path)  # Convert from mp3 to AudioSegment
    wav_filename = os.path.join("uploads", f"{uuid.uuid4()}.wav")
    audio.export(wav_filename, format="wav")
    return wav_filename

def generate_filename(prefix, ext="mp3"):
    sanitized_prefix = prefix.replace(" ", "_").replace(".", "").lower()[:10]  # Use first 10 chars
    return f"{sanitized_prefix}_{uuid.uuid4()}.{ext}"

@app.route('/api/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.json
    text = data.get('text')
    voice = data.get('voice', 'en')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        tts = gTTS(text=text, lang=voice)
        filename = generate_filename(text, ext="mp3")
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        tts.save(filepath)
        return jsonify({"success": True, "filename": filename}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/files', methods=['GET'])
def get_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify({"files": files})

@app.route('/api/files/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

@app.route('/api/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    try:
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file temporarily as mp3
    temp_mp3_filename = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.mp3")
    file.save(temp_mp3_filename)

    try:
        # Convert MP3 to WAV
        temp_wav_filename = convert_to_wav(temp_mp3_filename)

        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_wav_filename) as source:
            audio = recognizer.record(source)
        
        text = recognizer.recognize_google(audio)
        return jsonify({"success": True, "text": text}), 200
    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand audio"}), 400
    except sr.RequestError as e:
        return jsonify({"error": f"Could not request results: {str(e)}"}), 500
    finally:
        os.remove(temp_mp3_filename)
        os.remove(temp_wav_filename)

if __name__ == '__main__':
    app.run(debug=True)
