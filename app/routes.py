# -*- coding: utf-8 -*-
# @Author: Luís Adolfo Araújo


import os
from app import app

from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

from flask_jwt_extended import create_access_token, JWTManager
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET')
jwt = JWTManager(app)

app.secret_key = os.environ.get('SECRET_KEY', 'sample key')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_PORT'] = os.environ.get('MYSQL_PORT')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

db = MySQL(app)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "admin" or password != "@Admin123":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

