from flask import render_template, redirect, url_for, Flask
from app import app
import requests
import json
import os

HOST = os.environ.get('RESTAPI_HOST')
PORT = os.environ.get('RESTAPI_PORT')


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html', title='DevOps-Kv-116')


@app.route('/issues/', methods=['GET'])
def getIssues():
    request = requests.get(f'http://{HOST}:{PORT}/issues/')
    request_data = json.loads(request.content)
    return render_template('issues.html', title='DevOps-Kv-116', request_data=request_data)


@app.route('/labels/', methods=['GET'])
def getLabels():
    request = requests.get(f'http://{HOST}:{PORT}/labels/')
    request_data = json.loads(request.content)
    return render_template('labels.html', title='DevOps-Kv-116', request_data=request_data)


@app.route('/issues/by-label/<label>', methods=['GET'])
def getIssuesByLabel(label):
    request = requests.get(f'http://{HOST}:{PORT}/issues/by-label/{label}')
    request_data = json.loads(request.content)
    return render_template('bug.html', request_data=request_data)
