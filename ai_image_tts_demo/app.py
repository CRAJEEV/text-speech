import os
import torch
import torch.nn as nn
from torchvision.utils import save_image
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from diffusers import StableDiffusionPipeline
from TTS.api import TTS

class TextEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.gpt2 = GPT2LMHeadModel.from_pretrained('gpt2')
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    def forward(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors='pt')
        output = self.gpt2(input_ids)
        return output.last_hidden_state[:, -1, :]

class ImageGenerator(nn.Module):
    def __init__(self):
        super().__init__()
        self.pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
        if torch.cuda.is_available():
            self.pipeline = self.pipeline.to("cuda")
        else:
            print("CUDA is not available. Running on CPU. This may be slow.")

    def forward(self, prompt):
        image = self.pipeline(prompt).images[0]
        return image

class TTSModule:
    def __init__(self):
        self.tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")

    def generate_speech(self, text, output_path):
        self.tts.tts_to_file(text=text, file_path=output_path)

class AIImageTTSApp:
    def __init__(self):
        print("Initializing AI Image and TTS Application...")
        self.text_encoder = TextEncoder()
        print("Text Encoder initialized.")
        self.image_generator = ImageGenerator()
        print("Image Generator initialized.")
        self.tts_module = TTSModule()
        print("TTS Module initialized.")
        print("Application ready!")

    def generate(self, prompt, image_output_path, audio_output_path):
        try:
            # Generate image
            print("Generating image...")
            image = self.image_generator(prompt)
            image.save(image_output_path)
            print(f"Image saved to {image_output_path}")

            # Generate speech
            print("Generating speech...")
            self.tts_module.generate_speech(prompt, audio_output_path)
            print(f"Audio saved to {audio_output_path}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

def main():
    app = AIImageTTSApp()
    
    while True:
        prompt = input("Enter your prompt (or 'quit' to exit): ")
        
        if prompt.lower() == 'quit':
            break
        
        image_output_path = input("Enter the image output path (default: output_image.png): ") or "output_image.png"
        audio_output_path = input("Enter the audio output path (default: output_audio.wav): ") or "output_audio.wav"
        
        app.generate(prompt, image_output_path, audio_output_path)

if __name__ == "__main__":
    main()