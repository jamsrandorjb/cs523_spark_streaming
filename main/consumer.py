
from kafka import KafkaConsumer, KafkaProducer
import sys, json
import happybase
import datetime
from pyspark import SparkContext, SparkConf


host = "localhost"
namespace = "ns_twitter"
table_name = "tb_twitter"
now = datetime.datetime.now()

connection = happybase.Connection('localhost','9000')
conn = happybase.Connection(host = host,
    table_prefix = namespace,
    table_prefix_separator = ":")
conn.open()
table = conn.table(table_name)


struct = {}

lines = open("positive.txt","r")
positive_words = lines.read().split()
lines1 = open("negative.txt","r")
negative_words = lines1.read().split()

count = 0
consumer = KafkaConsumer('test',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])
#try:
for msg in consumer:
    now = datetime.datetime.now()
    f = open('rowid.txt','r')
    message = f.read()
    count = int(message)+1
    f.close()
    datas = msg.value.decode('utf-8')
    words = datas.split()
    count_positive = len([w for w in words if w in positive_words])
    count_negative = len([w for w in words if w in negative_words])
    try:
        ratio_positive = count_positive / len(words)
    except ZeroDivisionError:
        ratio_positive = 0
    try:
        ratio_negative = count_negative / len(words)
    except ZeroDivisionError:
        ratio_negative = 0
    if ratio_positive > 0:
        f1 = open('rowid.txt','w')
        f1.write(str(count))
        f1.close()
        print (datas)
        print('ratio_positive: '+str(ratio_positive))
        print('ratio_negative: '+str(ratio_negative))
        #saving into txt file after hbase corrupted. I used this
        fh = open('calculated1.txt', 'a')
        fh.write(str(count)+'\t'+datas+'\t'+str(ratio_positive)+'\t'+str(ratio_negative)+'\t'+str(now.strftime("%Y-%m-%d %H:%M"))+'\n')
        fh.close
        #if the hbase runs following line will insert the data
        table.put(str(count),{"full_text:full_text":datas,
                   "positive_predictions:positive_predictions":str(ratio_positive),
                   "negative_predictions:negative_predictions":str(ratio_negative),
                   "created_date:created_date":str(ratio_negative)
                    })
    elif ratio_negative > 0:
        #it is doing almost same thing lack of python programming experience forced me to write following code afain. DRY
        f1 = open('rowid.txt','w')
        f1.write(str(count))
        f1.close()
        print (datas)
        print('ratio_positive: '+str(ratio_positive))
        print('ratio_negative: '+str(ratio_negative))
        fh = open('calculated1.txt', 'a')
        fh.write(str(count)+'\t'+datas+'\t'+str(ratio_positive)+'\t'+str(ratio_negative)+'\t'+str(now.strftime("%Y-%m-%d %H:%M"))+'\n')
        fh.close
        table.put(str(count),{"full_text:full_text":datas,
               "positive_predictions:positive_predictions":str(ratio_positive),
               "negative_predictions:negative_predictions":str(ratio_negative),
               "created_date:created_date":str(now.strftime("%Y-%m-%d %H:%M"))
                })
#finally:
conn.close()


    #print(ratio_positive)
    #print(ratio_negative)
    #dataform = str(datas).strip("'<>() ").replace('\'', '\"')
    #struct = json.loads(datas)
    #data = json.load(datas


KafkaConsumer(consumer_timeout_ms=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
