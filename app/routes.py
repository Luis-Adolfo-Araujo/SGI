# -*- coding: utf-8 -*-
# @Author: Luís Adolfo Araújo

import hashlib
import json

from app import app, session
from app.models import Fornecedor, Material, Usuario
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
@login_required
def postNewUser():
  try:
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
  except:
    return make_response(jsonify({"message": "Falha ao criar novo usuário"}))

@app.route("/prov/newProv", methods=["POST"])
@login_required
def postNewProvider():
    try:
        obj = request.get_json()
        
        nomeFantasia = obj["nomeFantasia"]
        razaoSocial = obj["razaoSocial"]
        cep = obj["cep"]
        cnpj = obj["cnpj"]
        numero = obj["numero"]
        logradouro = obj["logradouro"]
        uf = obj["uf"]
        cidade = obj["cidade"]
        situacao = obj["situacao"]
        bairro = obj["bairro"]
        nomeContato1 = obj["nomeContato1"]
        nomeContato2 = obj["nomeContato2"]
        emailContato1 = obj["emailContato1"]
        emailContato2 = obj["emailContato2"]
        foneContato1 = obj["foneContato1"]
        foneContato2 = obj["foneContato2"]

        localSession = session()

        newProvider = Fornecedor(
            nome=razaoSocial,
            nome_fantasia=nomeFantasia,
            cep=cep,
            cnpj=cnpj,
            numero=numero,
            logradouro=logradouro,
            uf=uf,
            cidade=cidade,
            situacao=situacao,
            bairro=bairro,
            nome_contato1=nomeContato1,
            nome_contato2=nomeContato2,
            email_contato1=emailContato1,
            email_contato2=emailContato2,
            fone_contato1=foneContato1,
            fone_contato2=foneContato2
        )
        
        localSession.add(newProvider)
        localSession.commit()

        return make_response(jsonify({"message": "Fornecedor cadastrado com sucesso!"}), 200)
    except:
        return make_response(jsonify({"message": "Algo deu errado ao cadastrar fornecedor!"}))

@app.route("/material/newMaterial", methods=["POST"])
@login_required
def postNewMaterial():
    try:
        obj = request.get_json()
        localSession = session()

        tipo = obj["tipo"]
        if tipo == "Câmera":
            tipo = 1
        elif tipo == "Rastreador":
            tipo = 2
        else: 
            tipo = 3
        
        grupo = obj["grupo"]
        if grupo == "Câmera":
            grupo = 1
        elif grupo == "Rastreador":
            grupo = 2
        else: 
            grupo = 3
        
        modelo = obj["modelo"]
        fabricante = obj["fabricante"]
        posicao = obj["posicao"]
        estoqueMin = obj["estoqueMin"]
        ncm = obj["ncm"]
        nSerie = obj["nSerie"]

        newMaterial = Material(
            tipo_id=tipo,
            grupo_id=grupo,
            modelo=modelo,
            fabricante_id=fabricante,
            ncm=ncm,
            estoque_minimo=estoqueMin,
            posicao_estoque=posicao,
            possui_numero_serie=nSerie
        )
        localSession.add(newMaterial)
        localSession.commit()
        return make_response(jsonify({"message": "Material cadastrado com sucesso!"}), 200)
    except:
        return make_response(jsonify({"message": "Algo deu errado ao cadastrar material!"}))

@app.route("/fetchData/usuario", methods=["GET"])
@login_required
def fetchDbUserData():
    
    localSession = session()
    headers = {
        'headers': [
            'Ativo',
            'Email', 
            'Login',
            'Nome',
            'Permissão'
            ]
        }
    data = localSession.execute("SELECT ativo, email, login, nome, permissoes_id   FROM usuario")
    # <sqlalchemy.engine.cursor.CursorResult object at 0x10877ca90>
    # convert cursorResult (some spetial keyed tuple that is returned) to dict so that we can manipulate data
    data = [r._asdict() for r in data]
    for row in data:
        if row['permissoes_id'] == 1:
            row['permissoes_id'] = 'Administrador'
        else:
            row['permissoes_id'] = 'Almoxarifado'
        
        if row['ativo'] == 1:
            row['ativo'] = 'ativo'
        else:
            row['ativo'] = 'inativo'
    data.insert(0, headers)
    
    return make_response(jsonify(data), 200)

@app.route("/fetchData/material", methods=["GET"])
@login_required
def fetchDbMaterialData():
    
    localSession = session()
    headers = {
        'headers': [
            'Estoque minimo',
            'Fabricante',
            'Grupo',
            'Modelo',
            'Ncm',
            'Numero Série',
            'Posicao Estoque',
            'Tipo', 
            ]
        }
    data = localSession.execute("""SELECT 
    fabricante_id, tipo_id, 
    grupo_id, modelo, ncm, 
    estoque_minimo, posicao_estoque, 
    foto, possui_numero_serie 
    FROM material""")

    # <sqlalchemy.engine.cursor.CursorResult object at 0x10877ca90>
    # convert cursorResult (some spetial keyed tuple that is returned) to dict so that we can manipulate data
    data = [r._asdict() for r in data]
    data.insert(0, headers)
    print(data)    
    return make_response(jsonify(data), 200)

@app.route("/fetchData/fornecedor", methods=["GET"])
@login_required
def fetchDbFornecedorData():
    
    localSession = session()
    headers = {
        'headers': [
            'Bairro',
            'CEP',
            'Cidade',
            'CNPJ',
            'Email Contato 1',
            'Email Contato 2',
            'Fone Contato 1',
            'Fone Contato 2',
            'Logradouro',
            'Nome Contato 1',
            'Nome Contato 2',
            'Nome Fantasia',
            'Número',
            'Razão Social',
            'Situacao',
            'UF',
            ]
        }
    data = localSession.execute("SELECT nome, nome_fantasia, cep, cnpj, numero, logradouro, uf, cidade, situacao, bairro, nome_contato1, nome_contato2, email_contato1, email_contato2, fone_contato1, fone_contato2 FROM fornecedor")

    # <sqlalchemy.engine.cursor.CursorResult object at 0x10877ca90>
    # convert cursorResult (some spetial keyed tuple that is returned) to dict so that we can manipulate data
    data = [r._asdict() for r in data] 
    data.insert(0, headers)
    return make_response(jsonify(data), 200)

@app.route("/fetchData/fabricante", methods=["GET"])
@login_required
def fetchDbFabricanteData():
    
    localSession = session()
    headers = {
        'headers': [
            'Bairro',
            'CEP',
            'Cidade',
            'CNPJ',
            'Email Contato 1',
            'Email Contato 2',
            'Fone Contato 1',
            'Fone Contato 2',
            'Logradouro',
            'Nome Contato 1',
            'Nome Contato 2',
            'Nome Fantasia',
            'Número',
            'Razão Social',
            'Situacao',
            'UF',
            ]
        }
    data = localSession.execute("SELECT nome, nome_fantasia, cep, cnpj, numero, logradouro, uf, cidade, situacao, bairro, nome_contato1, nome_contato2, email_contato1, email_contato2, fone_contato1, fone_contato2 FROM fornecedor")

    # <sqlalchemy.engine.cursor.CursorResult object at 0x10877ca90>
    # convert cursorResult (some spetial keyed tuple that is returned) to dict so that we can manipulate data
    data = [r._asdict() for r in data] 
    data.insert(0, headers)
    return make_response(jsonify(data), 200)


@app.route("/logout", methods=["POST"])
def logout():
  try:
    logout_user()
    return make_response(jsonify({"message": "Sessão encerrada!"}), 200)
  except:
    return make_response(jsonify({"message": "Falha ao encerrar sessão"}))