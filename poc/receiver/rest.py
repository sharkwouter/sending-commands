from poc.receiver.base import ReceiverBase
import bottle

SERVER = Bottle()


class ReceiverRest(ReceiverBase):

    def __init__(self, port):
        super().__init__(port)
        self.ip = "localhost"
        self.server = None
        self.action = None

    def run(self, action: classmethod):
        self.running = True
        self.action = action
        self.__listen()

    def __listen(self):
        self.server = websockets.serve(self.action, self.ip, self.port)
