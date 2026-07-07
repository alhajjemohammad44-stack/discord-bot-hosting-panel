"""
Vercel entry point for Discord Bot Hosting Panel
"""
import sys
import os

# Add the project root to path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

# ========== Vercel Environment Setup ==========
# On Vercel, only /tmp is writable, so redirect folders there
if os.environ.get('VERCEL') == '1' or os.path.exists('/var/task'):
    # We're on Vercel/AWS Lambda
    tmp_dir = '/tmp'
    for folder in ['bots', 'data', 'uploads', 'static/uploads']:
        os.makedirs(os.path.join(tmp_dir, folder), exist_ok=True)
        os.makedirs(os.path.join(root_dir, folder), exist_ok=True)
else:
    # Local development
    for folder in ['bots', 'data', 'uploads', 'static/uploads']:
        os.makedirs(os.path.join(root_dir, folder), exist_ok=True)

# Set environment variables
os.environ.setdefault('ADMIN_PASSWORD', '61174271082')
os.environ.setdefault('SECRET_KEY', 'discord-bot-hosting-secret-key-vercel')
os.environ.setdefault('PORT', '5000')

# Import the Flask app
from app import app as flask_app

# Vercel handler
app = flask_app
