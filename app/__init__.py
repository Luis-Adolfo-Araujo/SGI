import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "lakjsndcpuansdpa234897230h2u1h23iu4b23kb12j3hbe1o23n123e1kjln"

engine = create_engine('mysql+pymysql://dev:e77989ed21758e78331b20e477fc5582@191.252.156.244:3306/sgi')

session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = session.query_property()
db = SQLAlchemy(app)

CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from app import models
from app import views
from app import routes
