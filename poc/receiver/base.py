class ReceiverBase:

    def __init__(self, port):
        self.running = False
        self.port = port

    def run(self, action: classmethod):
        self.running = True
        while self.running:
            message = self.__listen()
            result = action(message)
            self.__return_result(result)

    def stop(self):
        self.running = False

    def __listen(self):
        raise NotImplementedError("__listen was not implemented")

    def __return_result(self, result: bool):
        raise NotImplementedError("__return_result was not implemented")
