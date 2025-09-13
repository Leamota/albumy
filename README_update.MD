# Albumy ML Integration

![Screenshot](http://127.0.0.1:5000/static/images/index.jpg)

A photo-sharing web app with **ML-powered features**: automatic alt-text generation and object detection for tagging.

## Features

- Upload and manage photos
- Automatic alt-text generation using BLIP
- Object detection → automatic tagging
- Search photos, users, and tags
- Collect, comment, and manage notifications

## Setup

1. **Clone the repository**
```bash
git clone <repo_url>
cd albumy

Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Install dependencies
pip install -r requirements.txt


Set environment variables
export FLASK_APP=albumy
export FLASK_ENV=development
# Optional: API keys if using external ML models

Initialize the database
flask db upgrade

Usage
Run the app
flask run

Access at http://127.0.0.1:5000/

Upload photos → alt-text generated automatically if description is empty

Detected objects are added as tags automatically


Dependencies
Flask

Flask-Login

SQLAlchemy

Pillow

torch

transformers

Other dependencies listed in requirements.txt