"""
Vercel entry point for Discord Bot Hosting Panel
"""
import sys
import os

# ========== Debug: print paths ==========
print("=== VERCEL DEBUG ===")
print(f"CWD: {os.getcwd()}")
print(f"FILE: {__file__}")
print(f"DIRNAME: {os.path.dirname(os.path.abspath(__file__))}")
print(f"PARENT: {os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}")
print(f"PATH: {sys.path}")
print(f"FILES: {os.listdir(os.path.dirname(os.path.abspath(__file__)))}")
try:
    parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"PARENT_FILES: {os.listdir(parent)}")
except:
    pass
print("===================")

# Try multiple path strategies
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Also add current working directory
cwd = os.getcwd()
if cwd not in sys.path:
    sys.path.insert(0, cwd)

# Set environment variables
os.environ.setdefault('ADMIN_PASSWORD', '61174271082')
os.environ.setdefault('SECRET_KEY', 'discord-bot-hosting-secret-key-vercel')
os.environ.setdefault('PORT', '5000')

# Import the Flask app
try:
    from app import app as flask_app
    app = flask_app
    print("✅ Successfully imported app!")
except Exception as e:
    print(f"❌ Import error: {e}")
    # Fallback: simple debug app
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def debug():
        import traceback
        return f"""
        <h1>Debug Info</h1>
        <pre>
        CWD: {os.getcwd()}
        FILE: {__file__}
        PARENT: {os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))}
        PATH: {sys.path}
        ERROR: {e}
        </pre>
        """
