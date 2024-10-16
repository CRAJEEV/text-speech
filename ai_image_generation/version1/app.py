# app.py
from flask import Flask, request, render_template
import torch
from models.model_v1 import Generator

app = Flask(__name__)

# Load your trained model (example)
generator = Generator(input_dim=100, output_dim=784)
generator.load_state_dict(torch.load('path/to/your/model.pth'))
generator.eval()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    noise = torch.randn(1, 100)  # Generate random noise
    with torch.no_grad():
        generated_image = generator(noise)
        # Process the generated image (e.g., convert to PIL image)
        # Save or return the image
    return "Image generated!"

if __name__ == '__main__':
    app.run(debug=True)
