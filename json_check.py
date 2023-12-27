import json


def write_user(login, password, name):
	if len(login) <= 3:
		return "Длина вашего хендла должна быть строго больше 3"
	if len(password) <= 4:
		return "Длина вашего пароля должна быть строго больше 4"

	to_json = {}

	with open(name) as file:
		file_content = file.read()
		to_json = json.loads(file_content)
	
	if login in to_json:
		return "Это имя уже используется"
	
	to_json[login] = password

	with open(name, 'w') as file:
		file.write(json.dumps(to_json))
	
	return "OK"


def check_user(login, password, name):
	data = read_json(name)

	if login not in data:
		return "Неверное имя пользователя или пароль"
	
	if data[login] != password:
		return "Неверное имя пользователя или пароль"
	
	return "OK"


def read_json(name):
	with open(name) as file:
		file_content = file.read()
		data = json.loads(file_content)

	return data