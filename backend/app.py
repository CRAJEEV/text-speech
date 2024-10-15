from flask import Flask, request, send_from_directory
from flask_cors import CORS
from gtts import gTTS
import os

app = Flask(__name__)
CORS(app)

# Directory to store generated audio files
OUTPUT_FOLDER = 'output_files'
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Static list of available voices for gTTS (English male, female, child)
AVAILABLE_VOICES = [
    {'id': 'en', 'name': 'English'},
    {'id': 'en-us', 'name': 'American English'},
    {'id': 'en-uk', 'name': 'British English'},
    {'id': 'en-au', 'name': 'Australian English'},
    # Add more as needed
]

@app.route('/api/voices', methods=['GET'])
def list_voices():
    return {'voices': AVAILABLE_VOICES}

@app.route('/api/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.json
    text = data.get('text')
    voice = data.get('voice', 'en')

    # Generate a dynamic filename based on the text (using first 10 chars)
    filename = f"{text[:10]}_{voice}.mp3"
    file_path = os.path.join(OUTPUT_FOLDER, filename)

    try:
        tts = gTTS(text=text, lang=voice)
        tts.save(file_path)
        return {'filename': filename}, 200
    except Exception as e:
        return {'error': str(e)}, 500

@app.route('/api/files', methods=['GET'])
def list_files():
    files = os.listdir(OUTPUT_FOLDER)
    return {'files': files}

@app.route('/output/<filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

@app.route('/api/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    try:
        os.remove(os.path.join(OUTPUT_FOLDER, filename))
        return {'message': 'File deleted successfully.'}, 200
    except FileNotFoundError:
        return {'message': 'File not found.'}, 404
    except Exception as e:
        return {'message': str(e)}, 500
        

if __name__ == '__main__':
    app.run(debug=True)
