from flask import Flask 
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def cria_banco():
	db.create_all()


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(debug=True)
