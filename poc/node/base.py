from poc.message import Message
from poc.command import Command


class NodeBase:

    def __init__(self):
        self.commands = Message()

    def send_commands(self, sender) -> bool:
        result = sender.send_commands(self.commands)
        return self.__parse_result(result)

    def add_command(self, command: Command) -> None:
        self.commands.add_command(command)

    def __parse_result(self, result) -> bool:
        return result
