from flask import Flask
from flask.json import jsonify
from flask_restful import  Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #Le indica a alchemy que la db se encuentra en el root de nuestro proyect
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
app.secret_key = 'password'
api = Api(app) #Permite de una manera muy fácil añadir resources a nuestra app. 


jwt = JWT(app,authenticate, identity) 
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #el modo de acceder a los endpoing similar a los decoradores @app.route('/store')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True) #con el parámetro debug podemos depurar los errores mostrados.
