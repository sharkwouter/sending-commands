from poc.receiver.base import ReceiverBase
from bottle import Bottle, route, request
import json

SERVER = Bottle()


class ReceiverRest(ReceiverBase):
    def run(self, action: classmethod):
        self.action = action
        self.running = True
        SERVER.run(host='0.0.0.0', port=self.port)

    @route('/', method='POST')
    def root(self):
        data = request.json()
        result = self.action(data)
        return json.dumps({'result': result})
