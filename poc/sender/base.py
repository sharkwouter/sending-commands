class SenderBase:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.__connect(ip, port)

    def __connect(self, ip, port):
        pass

    def send_commands(self, command):
        self._send(command.to_json())

    def _send(self, command):
        raise NotImplementedError("__send not implemented")
