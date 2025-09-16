import asyncio


import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        await websocket.send(message)
        print(f"Отправлено сообщение: {message}")
        response = await websocket.recv()
        print(f"Получено сообщение: {response}")

        for _ in range(5):
            response = await websocket.recv()
            print(f"Ответ от сервера: {response}")


asyncio.run(client())