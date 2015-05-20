__author__ = 'PRASAD PANDE'

import json
import nltk
from nltk.corpus import stopwords
import re
import MySQLdb
from pprint import pprint
import depencencyParser
import POSTagger
import sentimentClassifier
import JSONParsing


def getParsedData(fileName):
    allReviews=list()
    with open(fileName, 'r') as inFile:
        for line in inFile:
            allReviews.append(line)

    return allReviews

def polarityCalculation(dependencyDictionary):
    posSentences=[]
    negSentences=[]
    neutralSentences=[]
    polarity='neutral'

    for k1,v1 in dependencyDictionary.iteritems():
        subjectDictionary=JSONParsing.getSubjectivityDictionary(k1)
        if(len(subjectDictionary)>0):
            polarity=sentimentClassifier.calSentencePolarity(k1,subjectDictionary)
            if(polarity=='pos'):
                posSentences.append(k1)
            elif(polarity=='neg'):
                negSentences.append(k1)
            else:
                neutralSentences.append(k1)


    print("Positive Sentences:",len(posSentences))
    print("Writing positive sentences in output file")
    with open('positiveSentences.txt', 'w+') as outFile:
        for line in posSentences:
            outFile.write(line+"\n")

    outFile.close()

    print("Negative Sentences:",len(negSentences))
    print("Writing Negative sentences in output file")
    with open('NegativeSentences.txt', 'w+') as outFile:
        for line in negSentences:
            outFile.write(line+"\n")

    outFile.close()


    print("Neutral Sentences:",len(neutralSentences))
    print("Writing Neutral sentences in output file")
    with open('NeutralSentences.txt', 'w+') as outFile:
        for line in neutralSentences:
            outFile.write(line+"\n")

    outFile.close()

def main():
    print("Polarity detection")
    dependencyDictionary={}
    #Finding the polarity of the subjective sentences.
    reviewList = getParsedData('subjectiveSentences.txt')
    print(len(reviewList))
    print("Server Busy")
    for sentence in reviewList:
        dependencyDictionary[sentence]=depencencyParser.parse(sentence)

    print("Server  work done")
    polarityCalculation(dependencyDictionary)

if __name__ == '__main__':
    main()
