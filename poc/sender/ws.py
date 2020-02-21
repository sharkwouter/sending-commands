from poc.sender.base import SenderBase
import asyncio
import websockets


class SenderWebsocket(SenderBase):
    async def __send_ws(self, command):
        async with websockets.connect("ws://{}:{}".format(self.ip, self.port)) as websocket:
            await websocket.send(command)
            result = await websocket.recv()
            print(result)

    def _send(self, command):
        return asyncio.get_event_loop().run_until_complete(self.__send_ws(command))
