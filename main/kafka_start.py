from pyspark import SparkContext, SparkConf
import socket
from kafka import BrokerConnection
from kafka import KafkaConsumer, KafkaProducer
import json

#import logging; logging.basicConfig(level='INFO')
conn = BrokerConnection('localhost', '9092', socket.AF_UNSPEC)
conn.connect() # repeat until connected... should work normally
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.flush(30)
producer.send('test', json.dumps('test good bad aborted tweet1').encode('utf-8'))
producer.flush(30)
#conn.close()
#conn._gai = [] # this forces an empty dns cache
#conn.connect() # this will fail and never recover

#conf = SparkConf().setAppName("test").setMaster("local")
#sc = SparkContext(conf=conf)

#lines = sc.textFile("positive.txt")
#lines1 = sc.textFile("negative.txt")
#pairs = lines.map(lambda s: (s, 1))
#counts = pairs.reduceByKey(lambda a, b: a + b)
#print(counts)


#datas = "hello this is motherfucking test fuck fuck fuck this shit. good happy abort aborted aborts abrade abrasive accessible acclaim acclaimed"
#counts = datas.flatMap(lambda line: line.split(" ")) \
#             .map(lambda word: (word, 1)) \
#             .reduceByKey(lambda a, b: a + b)

#f = open('rowid.txt','r')
#message = f.read()
#f.close()
#f1 = open('rowid.txt','w')
#f1.write(str(int(message)+1))
#f1.close()
#f.close()
#positive_words = open("positive.txt","r")
#lines = positive_words.read().split()
#negative_words = open("negative.txt","r")
#lines1 = negative_words.read().split()

#count_positive = len([w for w in datas.split() if w in lines])
#count_negative = len([w for w in datas.split() if w in lines1])
#print(count_positive)
#print(count_negative)

#tokens = [t for t in datas.split()]
#for line in positive_words:
#    print(line)
#print(positive_words.read())
#clean_tokens = tokens[:]
#sr = stopwords.words('english')
#for token in tokens:
#    if token in stopwords.words('english'):
#        clean_tokens.remove(token)
#freq = nltk.FreqDist(clean_tokens)
#for key,val in freq.items():
#    print (str(key) + ':' + str(val))
