import unittest
import os
import time
from poc.node.cli import NodeCli
from poc.sender.rest import SenderRest
from tests.data.constants import IP, PORT, MESSAGE_SUCCEED, MESSAGE_FAIL, TEST_FILE
import subprocess


node = NodeCli()
sender = SenderRest(IP, PORT+1)
client = ["python3", "tests/clients/rest_cli.py"]
process = subprocess.Popen(client)
time.sleep(2)


class RestCliTest(unittest.TestCase):
    def test_execution(self):
        node.commands = MESSAGE_SUCCEED
        node.send_commands(sender)
        self.assertTrue(os.path.isfile(TEST_FILE))

    def test_rollback(self):
        node.commands = MESSAGE_FAIL
        node.send_commands(sender)
        self.assertFalse(os.path.isfile(TEST_FILE))


if __name__ == '__main__':
    unittest.main()
    os.kill(process.pid, 9)
    process.kill()
    time.sleep(2)
