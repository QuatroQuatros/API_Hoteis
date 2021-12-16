from flask_restful import Resource, reqparse
from models.usuario import UserModel


class User(Resource):
		argumentos = reqparse.RequestParser()
		argumentos.add_argument('login', type=str, required=True, help="login is required")
		argumentos.add_argument('senha', type=str, required=True, help="password is required")


		def get(self, user_id):
			user = UserModel.find_user(user_id)
			if user:
				return user.json()
			return {"menssage": 'user not found.'}, 404


		def delete(self, user_id):
			user = UserModel.find_user(user_id)
			if user:
				try:
					user.delete_user()
				except:
					return {"message": "Internal server error"}, 500

				return {"message": "usuario deletado com sucesso!"}, 204
			return {"message": "ITEM NOT FOUND!"}, 404
