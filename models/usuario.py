from db import db

class UserModel(db.Model):
	__tablename__ = "usuarios"

	user_id = db.Column(db.Integer(), primary_key = True)
	login = db.Column(db.String(40))
	senha = db.Column(db.String(40))


	def __init__(self, login, senha):
		self.login = login
		self.senha = senha

	def json(self):
		return {
			"user_id": self.user_id,
			"login": self.login
		}


	@classmethod
	def find_user(cls, user_id):
		user = cls.query.filter_by(user_id=user_id).first()
		if user:
			return user
		else:
			return None

	def save_user(self):
		db.session.add(self)
		db.session.commit()

	def delete_user(self):
		db.session.delete(self)
		db.session.commit()

