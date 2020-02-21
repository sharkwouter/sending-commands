from typing import List
import json


class Command:

    def __init__(self, command: List[str], rollback: List[str] = None):
        if rollback is None:
            rollback = ['']
        self.command = command
        self.rollback = rollback

    def to_json(self):
        data = {"command": self.command, "rollback": self.rollback}
        return json.dumps(data)

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        return Command(data['command'], data['rollback'])
