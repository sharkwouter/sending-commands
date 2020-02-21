#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.getcwd())
from poc.receiver.ws import ReceiverWebsocket
from poc.client.cli import ClientCli
from tests.data.constants import PORT

receiver = ReceiverWebsocket(PORT)
client = ClientCli(receiver)

client.run()
