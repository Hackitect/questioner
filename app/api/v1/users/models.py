from app.api.v1.utils.validators import Validators
import datetime

users_list = []


validate = Validators()

class Users():

	def signup(self, email, firstname, lastname, username, password, timestamp):
				
		if validate.is_valid_password(password) is False:
			return {"message": "password does not meet requirements"}
		if validate.is_valid_username(username) is False:
			return {"message": "Username must be a string of at least 3 characters"}
		if validate.is_valid_email(email) is False:
			return {"message": "Provide valid email of the correct format"}
		else:
			id = len(users_list) + 1
			new_user = {'id': id, 'username': username, 'firstname': firstname, 'lastname':lastname, 'password': password, 
						'email': email, 'timestamp': timestamp}
			users_list.append(new_user)
			return {
				"message": "New user added with the following details",
				"User created": username,
				"time created": timestamp				
				}


	