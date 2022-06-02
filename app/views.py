from app import app
from flask import render_template, request, redirect, jsonify, make_response
from flask_login import login_required, current_user

@app.route("/", methods=["GET", "POST"])
def index():
  try:
    return render_template("public/templates/webTemplate.html", name=current_user.nome)
  except:
    if request.method == "POST": 

      return redirect(request.url)
    return render_template("public/templates/login.html")

# alterar arquivo de webTemplate para home.
@app.route("/home")
@login_required
def home():
  return render_template("public/templates/webTemplate.html", name=current_user.nome)

@app.route("/user")
@login_required
def userRegister():
  return render_template("public/templates/user/userRegister.html", name=current_user.nome)

@app.route("/userGrid")
@login_required
def userGrid():
  return render_template("public/templates/user/userGrid.html", name=current_user.nome)

@app.route("/prov")
@login_required
def providerRegister():
  return render_template("public/templates/almoxarifado/provider/providerRegister.html", name=current_user.nome)

@app.route("/provGrid")
@login_required
def providerGrid():
  return render_template("public/templates/almoxarifado/provider/providerGrid.html", name=current_user.nome)

@app.route("/manuf")
@login_required
def manufacturerRegister():
  return render_template("public/templates/almoxarifado/manufacturer/manufacturerRegister.html", name=current_user.nome)

@app.route("/manufGrid")
@login_required
def manufacturerGrid():
  return render_template("public/templates/almoxarifado/manufacturer/manufacturerGrid.html", name=current_user.nome)

@app.route("/material")
@login_required
def materialregister():
  return render_template("public/templates/almoxarifado/material/material.html", name=current_user.nome)

@app.route("/materialGrid")
@login_required
def materialGrid():
  return render_template("public/templates/almoxarifado/material/gridMaterial.html", name=current_user.nome)

@app.route("/mov")
@login_required
def movimentacaoRegister():
  return render_template("public/templates/almoxarifado/movimentacao/movimentacao.html", name=current_user.nome)

@app.route("/movGrid")
@login_required
def movimentacaoGrid():
  return render_template("public/templates/almoxarifado/movimentacao/gridMovimentacao.html", name=current_user.nome)
