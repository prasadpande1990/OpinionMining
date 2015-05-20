import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
import sys

def parse(text):
  server = ServerProxy(JsonRpc20(),TransportTcpIp(addr=("127.0.0.1", 3624)))
  return json.loads(self.server.parse(text))

def main():
  if len(sys.argv) == 2:
    inputText=sys.argv[1]
  else:
    inputText="World is beautiful"
  result=parse(inputText)
  pprint(result)
  
if __name__ == '__main__':
  main()
