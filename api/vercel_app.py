"""
Vercel wrapper - imports the Flask app safely
"""
import sys
import os
import traceback

# Add project root to path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cwd = os.getcwd()
for p in [root_dir, cwd]:
    if p not in sys.path:
        sys.path.insert(0, p)

os.environ.setdefault('ADMIN_PASSWORD', '61174271082')
os.environ.setdefault('SECRET_KEY', 'discord-bot-hosting-secret-key-vercel')

try:
    # Try importing the Flask app
    from app import app
    print("✅ Flask app imported successfully")
except Exception as e:
    print(f"❌ Failed to import app: {e}")
    traceback.print_exc()
    
    # Fallback: create a minimal Flask app with debug info
    from flask import Flask, jsonify
    app = Flask(__name__)
    
    @app.route('/')
    @app.route('/<path:path>')
    def debug_page(path=''):
        return jsonify({
            'error': str(e),
            'traceback': traceback.format_exc(),
            'cwd': os.getcwd(),
            'file': __file__,
            'root_dir': root_dir,
            'path': sys.path,
            'files_cwd': os.listdir('.')[:50],
            'files_root': os.listdir(root_dir)[:50],
            'env': {k:v for k,v in os.environ.items() if not k.startswith('VERCEL')}
        })
