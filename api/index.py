"""
Vercel entry point for Discord Bot Hosting Panel
"""
import sys
import os

# Ensure the project root is in the Python path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cwd = os.getcwd()

for p in [root_dir, cwd]:
    if p not in sys.path:
        sys.path.insert(0, p)

# Set environment variables
os.environ.setdefault('ADMIN_PASSWORD', '61174271082')
os.environ.setdefault('SECRET_KEY', 'discord-bot-hosting-secret-key-vercel')

# Create necessary directories
for folder in ['bots', 'data', 'uploads']:
    try:
        os.makedirs(os.path.join(cwd, folder), exist_ok=True)
    except:
        try:
            os.makedirs(os.path.join('/tmp', folder), exist_ok=True)
        except:
            pass

# Import the Flask app - top level for Vercel
from app import app
