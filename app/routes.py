# -*- coding: utf-8 -*-
# @Author: Luís Adolfo Araújo

import os
import hashlib

from app import app, session
from app.models import Usuario
from flask import Flask, Response, request, jsonify, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from flask_jwt_extended import create_access_token, JWTManager
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# Setup the Flask-JWT-Extended extension

app.config["JWT_SECRET_KEY"] = "lakjsndcpuansdpa234897230h2u1h23iu4b23kb12j3hbe1o23n123e1kjln"
jwt = JWTManager(app)

login_manager = LoginManager()
login_manager.login_view = 'index'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return Usuario.query.get(int(user_id))

@app.route("/auth", methods=["POST", "GET"])
def create_token():
    login = request.json.get("login", None)
    password = request.json.get("password", None)    
    password = hashlib.md5(password.encode('UTF-8')).hexdigest()
    
    user = Usuario.query.filter_by(login=login).first()
    pswd = Usuario.query.filter_by(senha=password).first()

    # Create a route to authenticate your users and return JWTs. The
    # create_access_token() function is used to actually generate the JWT.
    if(user and pswd):
        access_token = create_access_token(identity=login)
        login_user(user)
        return jsonify(access_token=access_token), 200
        
    else: 
        return 'Credenciais inválidas', 403

# TODO - validate username (check if already exists)
@app.route("/user/newUser", methods=["POST"])
def postNewUser():
  obj = request.get_json()

  if obj["permission"] == "Administrador":
      permission = 1
  else:
      permission = 0
  name = obj["name"]
  login = obj["login"] 
  email = obj["email"]
  password = obj["password"]

  localSession = session()
  
  newUser = Usuario(
      permissoes_id = permission,
      nome = name,
      login = login,
      email = email,
      senha = hashlib.md5(password.encode('UTF-8')).hexdigest(),
  )
  localSession.add(newUser)
  localSession.commit()
  return make_response(jsonify({"message": "received!"}), 200)

@app.route("/logout", methods=["POST"])
def logout():
  logout_user()
  return make_response(jsonify({"message": "Logged out!"}), 200)