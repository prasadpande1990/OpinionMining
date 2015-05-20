import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
import sys

class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 3624)))
   
    def parse(self, text):
        return json.loads(self.server.parse(text))
 
if len(sys.argv) == 2:
  inputText=sys.argv[1]
else:
  inputText="World is beautiful"

nlp = StanfordNLP()
result = nlp.parse(inputText)
pprint(result)


def parse(text):
  if len(sys.argv) == 2:
    inputText=sys.argv[1]
  else:
    inputText="World is beautiful"
  server = ServerProxy(JsonRpc20(),TransportTcpIp(addr=("127.0.0.1", 3624)))
  return json.loads(self.server.parse(text))
