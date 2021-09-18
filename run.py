from app import app
from db import db

db.init_app(app) 

@app.before_first_request
def create_tables():
    db.create_all() #IMPORTANTE: SQLAlchemy CREA LAS BASES DE DATOS POR NOSOTROS. ES IMPORTANTE IMPORTAR LO QUE QUEREAMOS QUE SQLAlchemy cree
