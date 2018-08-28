import os
import base64
import flask
import bcrypt
import datetime
from init import app, db
import models
from sqlalchemy import desc
from math import ceil


@app.route('/integrationTest', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json(silent=True)

    return uuid


@app.route('/logout')
def logout():
    return flask.redirect('/')
