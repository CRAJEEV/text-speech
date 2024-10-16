# AI Image Generation and TTS Application

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Components](#components)
6. [Troubleshooting](#troubleshooting)
7. [Future Improvements](#future-improvements)

## Introduction

This application combines AI-powered image generation and text-to-speech (TTS) capabilities. It allows users to input a text prompt, which is then used to generate a corresponding image and an audio file of the text being spoken. The application uses state-of-the-art models including GPT-2 for text encoding, Stable Diffusion for image generation, and Tacotron 2 for text-to-speech conversion.

## Prerequisites

- Python 3.7 or higher
- CUDA-compatible GPU (recommended for faster image generation)
- At least 10 GB of free disk space

## Installation

1. Clone the repository or create a new directory:
   ```
   mkdir ai_image_tts_demo
   cd ai_image_tts_demo
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```
   pip install torch torchvision transformers diffusers TTS
   ```

4. Create a new file named `app.py` and copy the provided code into it.

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. When prompted, enter your text prompt. This will be used to generate both the image and the speech.

3. Specify the output paths for the image and audio files, or press Enter to use the default paths.

4. Wait for the generation to complete. This may take a few minutes, especially for image generation.

5. Check the specified output paths for your generated image and audio file.

6. Repeat the process with new prompts, or type 'quit' to exit the application.

## Components

### TextEncoder
Uses GPT-2 to encode the input text. This provides a rich representation of the text that can be used for various downstream tasks.

### ImageGenerator
Utilizes the Stable Diffusion model to generate images based on text prompts. Stable Diffusion is a state-of-the-art text-to-image model known for its high-quality outputs.

### TTSModule
Employs the TTS library with the Tacotron 2 model to convert text into speech. Tacotron 2 is known for producing natural-sounding speech.

### AIImageTTSApp
The main application class that brings together all components and manages the generation process.

## Troubleshooting

- If you encounter CUDA out-of-memory errors, try reducing the size of the generated image or using a GPU with more memory.
- If the image generation is very slow, ensure you're using a CUDA-compatible GPU. Without GPU acceleration, image generation can take a long time.
- If you face issues with library installations, ensure you're using a compatible Python version and that your pip is up-to-date.

## Future Improvements

1. Add a graphical user interface (GUI) for easier interaction.
2. Implement batch processing for generating multiple images/audio files.
3. Add options for different image sizes and styles.
4. Incorporate more TTS voices and languages.
5. Optimize for faster generation on CPU for users without GPUs.

Remember, this application is a prototype and may require further optimization and error handling for production use.
