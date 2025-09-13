http://127.0.0.1:5000/<img width="1634" height="968" alt="image" src="https://github.com/user-attachments/assets/6beaade9-6494-454b-85f0-14bf73ca8e61" />
Albumy ML Integration

A photo-sharing web app with **ML-powered features**: automatic alt-text generation and object detection for tagging.

Features

- Upload and manage photos
- Automatic alt-text generation using BLIP
- Object detection → automatic tagging
- Search photos, users, and tags
- Collect, comment, and manage notifications

 Setup

1. **Clone the repository**
```bash
git clone <repo_url>
cd albumy

Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Install dependencies
pip install -r requirements_update.txt

Set environment variables:
export FLASK_APP=albumy
export FLASK_ENV=development

Initialize database:
flask db upgrade
flask db # Optional
flask forge

Run app:
flask run

Open app:
Access at http://127.0.0.1:5000/

Upload photos → alt-text generated automatically if description is empty

Detected objects are added as tags automatically



