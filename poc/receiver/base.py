class ReceiverBase:

    def __init__(self, port):
        self.running = False
        self.port = port
        self.action = None

    def run(self, action: classmethod):
        self.running = True
        self.action = action
        while self.running:
            message = self.listen()
            result = action(message)
            self.return_result(result)

    def stop(self):
        self.running = False

    def listen(self):
        raise NotImplementedError("__listen was not implemented")

    def return_result(self, result: bool):
        raise NotImplementedError("__return_result was not implemented")
