import pika
import time
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for
import uuid
import psycopg2

UPLOAD_DIRECTORY = Path("files")
UPLOAD_DIRECTORY.mkdir(exist_ok=True)

app = Flask(__name__)


@app.route('/greet', methods=['GET'])
def get_uuid():
    connection = psycopg2.connect(user="postgres", password="secret",
                                  host="localhost", port="5432",
                                  database="voice")
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    return {"id": uuid.uuid4()}


@app.route('/speak', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            file.save(app.config['UPLOAD_FOLDER'] / file.filename)
            return


def something():
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.basic_publish(exchange='', routing_key="test",
                          body=b'audio.m4a')
    connection.close()
