#Import the necessary methods from tweepy library
import re
import json
import pandas as pd
import matplotlib.pyplot as plt
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import threading, logging, time
import multiprocessing

from kafka import KafkaConsumer, KafkaProducer

#Variables that contains the user credentials to access Twitter API
access_token = "370015826-CmqZBgN1u9OD2SKQ8zrWuDorsMyavgt3EJ0d0BS8"
access_token_secret = "WjHEdEwnnS6ZHyLT8fF604gINDK7LuwEzQxDgKdlPP0zO"
consumer_key = "dKKqPRzuicdBaYJviGMngXwR0"
consumer_secret = "nga62iPmxZyphjIdcrLC77yosCEWr9NSGsxiNGKSFdh1VEKPYn"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        print (data)
        producer.send('test', json.dumps(data).encode('utf-8'))
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    producer.flush(30)
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    #main()
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['newyork', 'london', 'mumbai', 'berlin'])
    stream.filter(track=['python', 'javascript', 'ruby', 'london', 'berlin', 'newyork', 'dubai', 'paris', 'moscow'])
