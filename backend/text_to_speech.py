from gtts import gTTS
import os

# Mapping custom voice names to gTTS supported language codes
voice_mapping = {
    'voice1': 'en',  # English
    'voice2': 'es',  # Spanish
    'voice3': 'fr',  # French
}

# Ensure the output_files directory exists
output_dir = "output_files"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def convert_text_to_speech(text, voice_type, voice_tone):
    # Get the language code from the mapping
    lang = voice_mapping.get(voice_type)

    if lang is None:
        raise ValueError(f"Language not supported: {voice_type}")

    try:
        tts = gTTS(text=text, lang=lang)
        # Create a valid file path in the output_files directory
        audio_file = os.path.join(output_dir, f'{text[:10].replace(" ", "_")}.mp3')  # Replace spaces in filename
        tts.save(audio_file)
        return audio_file
    except Exception as e:
        raise RuntimeError(f"Text-to-speech conversion failed: {e}")
    
    