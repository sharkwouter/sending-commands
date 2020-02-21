from poc.message import Message
from poc.command import Command


TEST_FILE = "test_file_name"

IP = "localhost"
PORT = 8888

MESSAGE_SUCCEED = Message()
MESSAGE_FAIL = Message()
__commands = [
    Command(["echo", "this is a test"], ["echo", "fine"]),
    Command(["touch", TEST_FILE], ["rm", TEST_FILE]),
    Command([""], [""])
]

MESSAGE_SUCCEED.commands = __commands.copy()
MESSAGE_SUCCEED.add_command(Command(["ls", "-l"], [""]))

MESSAGE_FAIL.commands = __commands.copy()
MESSAGE_FAIL.add_command(Command(["ls -l"], [""]))
