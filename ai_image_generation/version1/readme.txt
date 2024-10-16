# Create a virtual environment
python -m venv myenv
# Activate the virtual environment
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate

# Install required libraries
pip install torch torchvision matplotlib flask

ai_image_generation/
│
├── app.py               # Main application file
├── models/              # Directory for models
│   └── your_model.py    # Define your model architecture
├── datasets/            # Directory for datasets
├── static/              # Directory for serving static files (like images)
└── templates/           # Directory for HTML templates
