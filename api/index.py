"""
Vercel entry point for Discord Bot Hosting Panel
"""
import sys
import os
import traceback as tb_module
import shutil

# Add project root to path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cwd = os.getcwd()
for p in [root_dir, cwd]:
    if p not in sys.path:
        sys.path.insert(0, p)

os.environ.setdefault('ADMIN_PASSWORD', '61174271082')
os.environ.setdefault('SECRET_KEY', 'discord-bot-hosting-secret-key-vercel')

# Create directories in /tmp (Vercel writable storage)
for folder in ['bots', 'data', 'uploads']:
    os.makedirs(os.path.join('/tmp', folder), exist_ok=True)

# Copy existing database to /tmp if it exists
src_db = os.path.join(cwd, 'data', 'bots.db')
dst_db = os.path.join('/tmp', 'data', 'bots.db')
if os.path.exists(src_db) and not os.path.exists(dst_db):
    try:
        shutil.copy2(src_db, dst_db)
    except:
        pass

# Import the Flask app - save error for debug
import_error = None
app = None

try:
    from app import app as flask_app
    app = flask_app
except Exception as exc:
    import_error = exc
    tb_module.print_exc()

# Fallback: create debug app if import failed
if app is None:
    from flask import Flask, jsonify
    app = Flask(__name__)
    
    @app.route('/')
    @app.route('/<path:path>')
    def debug(path=''):
        return jsonify({
            'status': 'error',
            'error': str(import_error) if import_error else 'Unknown error',
            'traceback': tb_module.format_exc() if import_error else 'No traceback',
            'cwd': os.getcwd(),
            'file': __file__,
            'root_dir': root_dir,
            'files_cwd': os.listdir('.')[:50],
            'files_root': os.listdir(root_dir)[:50] if os.path.exists(root_dir) else [],
            'python_version': sys.version,
        })
