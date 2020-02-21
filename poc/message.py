from typing import List
import json
from poc.command import Command


class Message:

    def __init__(self, commands: List[Command] = []):
        self.commands = commands

    def add_command(self, command: Command):
        self.commands.append(command)

    def to_json(self):
        return_list = []
        for command in self.commands:
            data = json.loads(command.to_json())
            return_list.append(data)
        return json.dumps(return_list)

    @staticmethod
    def from_json(json_data):
        return_list = []
        data = json.loads(json_data)
        for command in data:
            result = Command.from_json(json.dumps(command))
            return_list.append(result)
        return Message(return_list)

    def __str__(self):
        return self.to_json()
