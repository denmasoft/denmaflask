import decimal
import string
import random
import json
import io
import os
import base64
import boto3
import simplejson

from werkzeug import secure_filename
from flask_cors import CORS
from flask import Flask, jsonify, make_response, request, current_app, abort, send_from_directory

import magic
from PyPDF2 import PdfFileReader
from google.protobuf.json_format import MessageToJson
from google.oauth2 import service_account
from google.cloud import vision
from pdf2image import convert_from_path
import cv2 as cv
from Middlewares import CreateModelMiddleware
s3 = boto3.client('s3')

# flask app config
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.wsgi_app = CreateModelMiddleware(app.wsgi_app)

@app.route('/')
def root():
    print('called the root route')
    return jsonify({'message': 'Hello from Lambda'})

@app.route('/pass')
def root():
    print('called the root route')
    return jsonify({'message': 'Hello from pass'})

@app.route('/create-model', methods=["POST"])
def root():
    print('called the root route')
    return jsonify({'message': 'Hello from Lambda'})


def make_error_response(statusCode, message, request_id, file_key):
    return {'status_code': statusCode, 'status': 'error', 'message': message, 'request_id': request_id, 'file_key': file_key}


if __name__ == "__main__":
    app.run()
