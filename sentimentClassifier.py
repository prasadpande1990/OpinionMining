__author__ = 'root'

import pprint as pprint
import sys
from nltk.corpus import sentiwordnet as wn
import POSTagger
import nltk
import operator

def lemmatizeWord(word):
    wnl = nltk.WordNetLemmatizer()
    lemma = wnl.lemmatize(word)
    return word

def calWordPolarity(word,tag):
    verb_tags=['VBZ','VBP','VBD','VBN','VBG','v']
    noun_tags=['NN','NNS','NNP','NNPS']
    adj_tags=['JJ','JJR','JJS']
    adv_tags=['RB','RBR','RBS']
    word=lemmatizeWord(word)
    score=0
    wordPolarity={}
    if(tag in adv_tags):
        try:
            sn = wn.senti_synsets(word,'r')[0]
            objScore=sn.obj_score()
            posScore=sn.pos_score()
            negScore=sn.neg_score()
            #wordPolarity['neutral']=objScore
            wordPolarity['pos']=posScore
            wordPolarity['neg']=negScore
        except IndexError:
            #print("Here")
            wordPolarity['neutral']=0.0

    elif (tag in adj_tags):
        try:
            sn = wn.senti_synsets(word,'a')[0]
            objScore=sn.obj_score()
            posScore=sn.pos_score()
            negScore=sn.neg_score()
            #wordPolarity['neutral']=objScore
            wordPolarity['pos']=posScore
            wordPolarity['neg']=negScore
        except IndexError:
            #print("Here")
            wordPolarity['neutral']=0.0

    elif(tag in noun_tags):
        try:
            sn = wn.senti_synsets(word,'n')[0]
            objScore=sn.obj_score()
            posScore=sn.pos_score()
            negScore=sn.neg_score()
            #wordPolarity['neutral']=objScore
            wordPolarity['pos']=posScore
            wordPolarity['neg']=negScore
        except IndexError:
            #print("Here")
            wordPolarity['neutral']=0.0

    elif(tag in verb_tags):
        try:
            sn = wn.senti_synsets(word,'v')[0]
            objScore=sn.obj_score()
            posScore=sn.pos_score()
            negScore=sn.neg_score()
            #wordPolarity['neutral']=objScore
            wordPolarity['pos']=posScore
            wordPolarity['neg']=negScore
        except IndexError:
            #print("Here")
            wordPolarity['neutral']=0.0

    else:
        wordPolarity['neutral']=0.0

    #print(wordPolarity)
    #print("------------------------------------------")
    return wordPolarity


def calSentencePolarity(sentence,subjectDictionary):
    POSTagDictionary = POSTagger.parse(sentence)
    wordPolarity={}
    global SentencePolarity
    SentencePolarity={}
    print(sentence)
    print(subjectDictionary)
    for key,value in subjectDictionary.iteritems():
        if(value=='strongsubj'):
            tag = POSTagDictionary[key]
            wordPolarity=calWordPolarity(key,tag)
            polarity=max(wordPolarity.iteritems(), key=operator.itemgetter(1))[0]
            #print("-->",polarity)
            SentencePolarity[polarity]=wordPolarity[polarity]
            #print("###",SentencePolarity)

    if(len(SentencePolarity)==1):
        for key,value in SentencePolarity.iteritems():
            polar=key
    else:
        polar=max(SentencePolarity.iteritems(), key=operator.itemgetter(1))[0]

    return polar


def getObjectSore(word,tag):
    verb_tags=['VBZ','VBP','VBD','VBN','VBG','v']
    noun_tags=['NN','NNS','NNP','NNPS']
    adj_tags=['JJ','JJR','JJS']
    adv_tags=['RB','RBR','RBS']
    word=lemmatizeWord(word)
    score=0


    if(tag in adv_tags):
    	try:
        	sn = wn.senti_synsets(word,'r')[0]
        	objScore=sn.obj_score()
        	posScore=sn.pos_score()
        	negScore=sn.neg_score()
        	score=max(objScore,posScore,negScore)
        except IndexError:
        	score=0.0
        
    elif (tag in adj_tags):
    	try:
        	sn = wn.senti_synsets(word,'a')[0]
        	objScore=sn.obj_score()
        	posScore=sn.pos_score()
        	negScore=sn.neg_score()
        	score=max(objScore,posScore,negScore)
        except IndexError:
        	score=0.0

    elif(tag in noun_tags):
    	try:
        	sn = wn.senti_synsets(word,'n')[0]
        	objScore=sn.obj_score()
        	posScore=sn.pos_score()
        	negScore=sn.neg_score()
        	score=max(objScore,posScore,negScore)
        except IndexError:
        	score=0.0

    elif(tag in verb_tags):
        try:
        	sn = wn.senti_synsets(word,'v')[0]
        	objScore=sn.obj_score()
        	posScore=sn.pos_score()
        	negScore=sn.neg_score()
        	score=max(objScore,posScore,negScore)
        except IndexError:
        	score=0.0

    else:
    	score=0.0
    	
    return score


def getSentenceScore(sentence,subjectDictionary):
	POSTagDictionary = POSTagger.parse(sentence)
	#print(POSTagDictionary)
	score=0.0
	for key,value in subjectDictionary.iteritems():
		if(value=='strongsubj'):
			tag = POSTagDictionary[key]
			score = score + getObjectSore(key,tag)
	
	if(score > 0.5):
		return 1
	else:
		return 0
			 

def main():
  if len(sys.argv) == 2:
    inputText=sys.argv[1]
  else:
    inputText="World is beautiful"

  pprint(inputText)
  print(wn.synsets('Frustrating'))
  sn=wn.senti_synsets('Highest','a')
  print(sn)
  
  
  

if __name__ == '__main__':
  main()
