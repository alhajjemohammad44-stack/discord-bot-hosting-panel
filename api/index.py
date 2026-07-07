"""
Vercel entry point for Discord Bot Hosting Panel
"""
import sys
import os

# Add project root to path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cwd = os.getcwd()
for p in [root_dir, cwd]:
    if p not in sys.path:
        sys.path.insert(0, p)

os.environ.setdefault('ADMIN_PASSWORD', '61174271082')
os.environ.setdefault('SECRET_KEY', 'discord-bot-hosting-secret-key-vercel')

# Create directories
for folder in ['bots', 'data', 'uploads']:
    for base in [cwd, '/tmp']:
        try:
            os.makedirs(os.path.join(base, folder), exist_ok=True)
        except:
            pass

# Import the Flask app
app = None
try:
    from app import app as flask_app
    app = flask_app
except Exception as e:
    # Fallback: simple Flask debug
    from flask import Flask, jsonify
    app = Flask(__name__)
    @app.route('/')
    @app.route('/<path:path>')
    def debug(path=''):
        import traceback
        return jsonify({
            'error': str(e),
            'traceback': traceback.format_exc(),
            'cwd': os.getcwd(),
            'files_cwd': os.listdir('.')[:30],
        })
