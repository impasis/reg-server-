import asyncio
import websockets
import sys
# from txt_check import txt_read_file


async def connect_to_server():
	global global_username
	global global_password

	try:
		async with websockets.connect("ws://localhost:8765") as websocket:
			while True:
				cmd = input("$ ")

				if cmd == "!register":
					if global_username is None and global_password is None:
						name = input("username: ")
						password = input("password: ")
						await websocket.send(f"reg-{name}-{password}")

						response = await websocket.recv()
						print(f"Server: {response}")

						if response == "OK":
							global_username = name
							global_password = password
							# await websocket.send(f"Connect!-{global_username}")
					else:
						print("Ты зарегестрирован. Для того чтобы зарегестрироваться заново, тебе нужно выйти из аккаунта")
				
				elif cmd == "!login":
					name = input("username: ")
					password = input("password: ")
					await websocket.send(f"log-{name}-{password}")

					response = await websocket.recv()
					print(f"Server: {response}")

					if response == "OK":
						global_username = name
						global_password = password
						# await websocket.send(f"Connect!-{global_username}")

				elif cmd == "!profile":
					if global_username is None or global_password is None:
						print("Ты не зарегистрирован!")
					else:
						print(f"Name: {global_username}")

				elif cmd == "!exit":
					# await websocket.send(f"Disconnect!-{global_username}")
					global_username = None
					global_password = None
					print("OK")
				
				elif cmd == "!close":
					# await websocket.send(f"Disconnect!-{global_username}")
					sys.exit()
				
				# elif cmd == "!online":
				#	txt_read_file()
				
				elif cmd == "!help":
					print("!exit - Выход из аккаунта")
					print("!profile - Просмотр своего профиля")
					print("!login - Вход в аккаунт")
					print("!close - Закрыть приложение")
					print("!register - Зарегестрировать аккаунт")
					# print("!online - Посмотреть пользователей, которые находятся онлайн")
				
				else:
					print(" Oops!\n Неверная команда!\n Попробуйте написать `!help`")
	
	except ConnectionRefusedError:
		print("[WinError 1225] Удаленный компьютер отклонил это сетевое подключение")

		# if global_username is not None and global_password is not None:
		#	await websocket.send(f"Disconnect!-{global_username}")
			 


global_username = None
global_password = None
asyncio.get_event_loop().run_until_complete(connect_to_server())