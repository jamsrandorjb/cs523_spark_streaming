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
from pyspark import SparkContext, SparkConf
import socket
from kafka import BrokerConnection


#Variables that contains the user credentials to access Twitter API
access_token = "370015826-CmqZBgN1u9OD2SKQ8zrWuDorsMyavgt3EJ0d0BS8"
access_token_secret = "WjHEdEwnnS6ZHyLT8fF604gINDK7LuwEzQxDgKdlPP0zO"
consumer_key = "dKKqPRzuicdBaYJviGMngXwR0"
consumer_secret = "nga62iPmxZyphjIdcrLC77yosCEWr9NSGsxiNGKSFdh1VEKPYn"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        full_tweet = json.loads(data)
        tweet_text = full_tweet['text']
        tweet_followers = full_tweet['user']['followers_count']
        tweet_friends = full_tweet['user']['friends_count']
        if tweet_followers > 100:
            if tweet_friends > 100:
                print("tweet_text: " + tweet_text)
                print("tweet_followers: " + str(tweet_followers))
                print("tweet_friends: " + str(tweet_friends))
                send_data = {
                    "tweet_text": tweet_text,
                    "tweet_followers": tweet_followers,
                    "tweet_friends": tweet_friends
                    }
                print (send_data)
                producer.send('test', json.dumps(tweet_text).encode('utf-8'))
#                producer.flush(30)
#        return True

        return True

    def on_error(self, status):
        print (status)




if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    stream.filter(track=['#london', '#newyork', '#melbourne', '#vancouver', '#wellington', '#dublin', '#nyc'])






#if __name__ == '__main__':
#    conn = BrokerConnection('localhost', '9092', socket.AF_UNSPEC)
#    conn.connect() # repeat until connected... should work normally
    #This handles Twitter authetification and the connection to Twitter Streaming API
#    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
#    producer.flush(30)
#    l = StdOutListener()
#    auth = OAuthHandler(consumer_key, consumer_secret)
#    auth.set_access_token(access_token, access_token_secret)
#    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(locations=[-6.38,49.87,1.77,55.81])
    #

    #stream.filter(lang=['en'])
