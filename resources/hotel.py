from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
	def get(self):
		return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}

class Hotel(Resource):
		argumentos = reqparse.RequestParser()
		argumentos.add_argument('nome', type=str, required=True, help="Hotel name is required")
		argumentos.add_argument('estrelas', type=float, required=True)
		argumentos.add_argument('diaria', type=float, required=True)
		argumentos.add_argument('cidade', type=str, required=True)


		def get(self, hotel_id):
			hotel = HotelModel.find_hotel(hotel_id)
			if hotel:
				return hotel.json()
			return {"menssage": 'Hotel not found.'}, 404

		def post(self, hotel_id):
			if HotelModel.find_hotel(hotel_id):
				return {"message": f'Hotel id {hotel_id} already exists.'}, 400

			dados = Hotel.argumentos.parse_args()
			hotel = HotelModel(hotel_id, **dados)
			try:
				hotel.save_hotel()
			except:
				return {"message": "Internal server error"}, 500

			return hotel.json()

		def put(self, hotel_id):
			dados = Hotel.argumentos.parse_args()
			hotel_encontrado = HotelModel.find_hotel(hotel_id)

			if hotel_encontrado:
				hotel_encontrado.update_hotel(**dados)

				try:
					hotel_encontrado.save_hotel()
				except:
					return {"message": "Internal server error"}, 500

				return hotel_encontrado.json(), 200 #ok

			hotel = HotelModel(hotel_id, **dados)
			try:
				hotel.save_hotel()
			except:
				return {"message": "Internal server error"}, 500
			return hotel.json(), 201 #criado


		def delete(self, hotel_id):
			hotel = HotelModel.find_hotel(hotel_id)
			if hotel:
				try:
					hotel.delete_hotel()
				except:
					return {"message": "Internal server error"}, 500

				return {"message": "Hotel deletado com sucesso!"}, 204
			return {"message": "ITEM NOT FOUND!"}, 404
