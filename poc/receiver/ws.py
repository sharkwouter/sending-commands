from poc.receiver.base import ReceiverBase
import json
import asyncio
import websockets


class ReceiverWebsocket(ReceiverBase):

    def __init__(self, port):
        super().__init__(port)
        self.ip = "0.0.0.0"
        self.server = None
        self.action = None

    async def __perform_action(self, websocket, path):
        async for message in websocket:
            print(message)
            message_result = self.action(message)
            await websocket.send(json.dumps({"result": message_result}))

    def run(self, action: classmethod):
        self.running = True
        self.action = action
        self.__listen()

    def __listen(self):
        self.server = websockets.serve(self.__perform_action, self.ip, self.port)
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()
