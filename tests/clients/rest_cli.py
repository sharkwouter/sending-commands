#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.getcwd())
from poc.receiver.rest import ReceiverRest
from poc.client.cli import ClientCli
from tests.data.constants import PORT

receiver = ReceiverRest(PORT+1)
client = ClientCli(receiver)

client.run()
