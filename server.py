import asyncio
import websockets
from json_check import *
# from txt_check import txt_write_user, txt_delete_user


async def echo(websocket, path):
    async for message in websocket:
        message = message.split('-')
        """if message[0] == "Connect!":
            txt_write_user(message[1])

        elif message[0] == "Disconnect!":
            print("HI!")
            txt_delete_user(message[1])"""

        cmd, login, password = message

        if cmd == "reg":
            await websocket.send(write_user(login, password, "data1.json"))
            
        elif cmd == "log":
            await websocket.send(check_user(login, password, "data1.json"))


start_server = websockets.serve(echo, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
