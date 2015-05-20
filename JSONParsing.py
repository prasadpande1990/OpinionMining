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

def getSubjectivity(wordList):
    db = MySQLdb.connect("localhost","root","","lexicon" )
    cursor = db.cursor()
    dict_strength={}
    for word in wordList:
        try:
            query = "SELECT type from lexicon where word1='%s'"%sentimentClassifier.lemmatizeWord(word)
            cursor.execute(query)
            data = cursor.fetchone()
            if(data is not None):
                data = ''.join(e for e in data if e.isalnum())
                dict_strength[word]=data

        except:
            print('Ignoring: malformed line:')

    db.close()
    return dict_strength

def getParsedData(fileName):
    allReviews=list()
    with open(fileName, 'r') as inFile:
        for line in inFile:
            allReviews.append(line)

    return allReviews



def getAllReviews():
    with open('reviewData.txt', 'w+') as outFile:
        with open(r"//root//Desktop//NLP-Project//test.json") as f:
            for line in f:
                data = json.loads(line)
                review_text= data['text']
                sentences = nltk.sent_tokenize(review_text)
                for sentence in sentences:
                    outFile.write(sentence + "\n")

    outFile.close()
    reviewDataList = getParsedData('reviewData.txt')
    return reviewDataList


def getSubjectivityDictionary(sentence):
    sentence_subject=dict()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sw = stopwords.words('english')
    wordList = set(nltk.word_tokenize(sentence))
    wordList = list(wordList.difference(sw))
    wordList = [w for w in wordList if re.search('[a-zA-Z]', w) and len(w) > 1]
    dict_strength=dict(getSubjectivity(wordList))
    return dict_strength

def writeSubjectSentences(subj_sent):
    with open('subjectiveSentences.txt', 'w+') as outFile:
        for line in subj_sent:
            outFile.write(line)

    outFile.close()


def getSubjectiveSentences(dependencyDictionary):
    subj_sent=[]
    score=0.0
    isSubjective=0

    for k1,v1 in dependencyDictionary.iteritems():
        subjectDictionary=getSubjectivityDictionary(k1)
        if(len(subjectDictionary)>0):
            if v1 in subjectDictionary:
                if(subjectDictionary[v1]=='strongsubj'):
                    subj_sent.append(k1)
                else:
                    score=sentimentClassifier.getObjectSore(subjectDictionary[v1],'v')
                    #print("####",score)
                    if(score>0.5):
                        subj_sent.append(k1)
            else:
                isSubjective=sentimentClassifier.getSentenceScore(k1,subjectDictionary)
                #print("@@@@@",isSubjective)
                if(isSubjective==1):
                    subj_sent.append(k1)

    return subj_sent


def main():
    reviewList = getAllReviews()
    sentence_subject=getSubjectivity(reviewList)
    #print(len(sentence_subject))
    dependencyDictionary={}
    print("Server busy")
    for sentence in reviewList:
        dependencyDictionary[sentence]=depencencyParser.parse(sentence)
    #print(dependencyDictionary)
    #print("------------------------------------------------------------------------------")
    print("Server work done")
    #sent_score={}
    subj_sent=getSubjectiveSentences(dependencyDictionary)
    writeSubjectSentences(subj_sent)
    #print(subj_sent)
    #print(len(subj_sent))

if __name__ == '__main__':
    main()
