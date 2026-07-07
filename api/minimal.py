"""Minimal Vercel test"""
from flask import Flask, jsonify
import sys, os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'status': 'ok',
        'cwd': os.getcwd(),
        'files': os.listdir('.')[:20],
        'path': sys.path[:5],
        'version': sys.version
    })
