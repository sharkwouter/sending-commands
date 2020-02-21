from poc.message import Message


class ClientBase:

    def __init__(self, receiver):
        self.receiver = receiver

    def __receive_message(self, message):
        message_object = Message.from_json(message)
        commands = message_object.commands
        for i in range(len(commands)):
            success = self.execute_command(commands[i])
            if not success:
                for j in range(i, 0-1, -1):
                    self.execute_rollback(commands[j])
                return False
        return True

    def run(self):
        self.receiver.run(self.__receive_message)

    def stop(self):
        self.receiver.stop()

    def execute_command(self, command) -> bool:
        raise NotImplementedError("__execute_command is not implemented")

    def execute_rollback(self, command) -> bool:
        raise NotImplementedError("__execute_command is not implemented")
