							
									Opinion Mining on Yelp DataSet
										Program Instructions

Author:
PRASAD SUNIL PANDE
psp150030@utdallas.edu

Platforms Used:
Operating System: Linux CentOS 6.2
Programming Language: Python 2.7
MySQL Database: MySQL 5.1.73
IDE: PyCharm Community Edition 4.0.4
Additional Package: numpy-1.6.1 for Linux 

Installation:
1. Creating Lexicon Database and Data Insertion.
	a. Inside MySQL create database lexicon.
	b. once the database is created. Create table lexicon as follows:
		CREATE TABLE `lexicon` (
	  `type` varchar(32) NOT NULL,
	  `len` int(11) DEFAULT NULL,
	  `word1` varchar(128) NOT NULL,
	  `pos1` varchar(16) NOT NULL,
	  `stemmed1` char(1) DEFAULT NULL,
	  `priorpolarity` varchar(16) NOT NULL)
	c. Insert the data in the table using lexicon.sql
		mysql> source lexicon.sql
	d. Verify if data is properly inserted in the table
	
2. Installing Dependency parser API
	a. sudo pip install pexpect unidecode
	b. git clone git://github.com/dasmith/stanford-corenlp-python.git
	c. cd stanford-corenlp-python
	d. wget http://nlp.stanford.edu/software/stanford-corenlp-full-2014-08-27.zip
	e. unzip stanford-corenlp-full-2014-08-27.zip
	f. Replace client.py with new file.
	g. python corenlp.py -p 3624
	h. python client.py "Review text"

	Note: In one terminal window, perform step g and keep it running while execution of the code. This program will act as a server and response to all dependency parser call will come from this package.

3. Execution of the program
	a. Execute JSONParsing.py file as follows:
		python JSONParsing.py
	b. Once this step is completed, subjectiveSentences.txt will be generated which contains the  	subjective sentences for the given data. This file will be used as input for the next program of polarity detection.
	
	c. Execute PolarityDetection.py file as follows:
		python PolarityDetection.py
		
	d. Once the execution of the sentences is completed successfully, it will create 3 output files namely NegativeSentences.txt, NeutralSentences.txt and positiveSentences.txt which will contain the sentences for the respective polarity.