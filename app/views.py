from app import app
from flask import render_template

@app.route("/")
def index():
  return render_template("public/index.html")

@app.route("/home")
def home():
  return render_template("public/templates/public_template.html")

@app.route("/userRegister")
def userRegister():
  return render_template("public/templates/userRegister.html")

@app.route("/providerRegister")
def providerRegister():
  return render_template("public/templates/providerRegister.html")

@app.route("/manufacturerRegister")
def manufacturerRegister():
  return render_template("public/templates/manufacturerRegister.html")

@app.route("/material")
def materialregister():
  return render_template("public/templates/material.html")

@app.route("/movimentacao")
def movimentacaoRegister():
  return render_template("public/templates/movimentacao.html")
