__author__ = 'root'

import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
import sys


def getPOSTag(wordLists):

    POSTagDict = dict()
    for i in range(0,len(wordLists)):
        wordList = wordLists[i]
        word = wordList[0]
        posTag = wordList[1]['PartOfSpeech']
        POSTagDict[word] = posTag
    return POSTagDict

def parse (text):
    server = ServerProxy(JsonRpc20(),TransportTcpIp(addr=("127.0.0.1", 3624)))
    try:
        jsonResult=json.loads(server.parse(text))
    except:
        return list()

    POSTagDictionary = getPOSTag(jsonResult['sentences'][0]['words'])
    return POSTagDictionary

def main():
  if len(sys.argv) == 2:
    inputText=sys.argv[1]
  else:
    inputText="World is beautiful"
  result=parse(inputText)
  pprint(result)

if __name__ == '__main__':
  main()
