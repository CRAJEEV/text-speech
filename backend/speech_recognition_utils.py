from pydub import AudioSegment
import os
import speech_recognition as sr

def convert_audio_to_wav(input_file):
    # Convert audio file to WAV format
    output_file = os.path.splitext(input_file)[0] + '.wav'
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format='wav')
    return output_file

def transcribe_audio(audio_file):
    # Convert audio file to WAV format if necessary
    wav_file = convert_audio_to_wav(audio_file)

    with sr.AudioFile(wav_file) as source:
        recognizer = sr.Recognizer()
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data)
