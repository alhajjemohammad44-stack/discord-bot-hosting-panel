import sys
import os

# Create a simple WSGI app
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'cwd': os.getcwd(),
        'file_dir': os.path.dirname(os.path.abspath(__file__)),
        'root_dir': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'path': sys.path,
        'files_in_root': os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'env': dict(os.environ),
        'vercel': os.environ.get('VERCEL'),
    })
