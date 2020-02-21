class SenderBase:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self._connect(ip, port)

    def _connect(self, ip, port):
        pass

    def send_commands(self, command) -> bool:
        return self._send(command.to_json())

    def _send(self, command) -> bool:
        raise NotImplementedError("__send not implemented")
