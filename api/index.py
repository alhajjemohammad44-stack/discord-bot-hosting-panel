"""
Vercel entry point for Discord Bot Hosting Panel
"""
import sys
import os
import traceback
import json

# Ensure the project root is in the Python path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cwd = os.getcwd()
for p in [root_dir, cwd]:
    if p not in sys.path:
        sys.path.insert(0, p)

os.environ.setdefault('ADMIN_PASSWORD', '61174271082')
os.environ.setdefault('SECRET_KEY', 'discord-bot-hosting-secret-key-vercel')

# Create necessary directories
for folder in ['bots', 'data', 'uploads']:
    for base in [cwd, '/tmp']:
        try:
            os.makedirs(os.path.join(base, folder), exist_ok=True)
        except:
            pass

# Try to import the Flask app
app = None
import_error = None

try:
    from app import app as flask_app
    app = flask_app
    print("✅ App imported successfully")
except Exception as e:
    import_error = e
    traceback.print_exc()
    print(f"❌ Import failed: {e}")

# If import failed, create a debug Flask app
if app is None:
    from flask import Flask, jsonify
    app = Flask(__name__)
    
    @app.route('/')
    @app.route('/<path:path>')
    def debug(path=''):
        debug_info = {
            'error': str(import_error) if import_error else 'Unknown',
            'traceback': traceback.format_exc() if import_error else '',
            'cwd': os.getcwd(),
            'file': __file__,
            'python_version': sys.version,
            'root_dir': root_dir,
        }
        try:
            debug_info['files_cwd'] = os.listdir('.')[:30]
            debug_info['files_root'] = os.listdir(root_dir)[:30]
        except:
            pass
        
        return jsonify(debug_info)
