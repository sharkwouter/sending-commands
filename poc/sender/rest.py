from poc.sender.base import SenderBase
import requests


class SenderRest(SenderBase):
    def _send(self, command):
        requests.post("http://{}:{}".format(self.ip, self.port), data=command)
