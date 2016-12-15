import os
import tweepy
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Word
from textblob.np_extractors import ConllExtractor
import sys
import requests
import json

consumer_key= ''
consumer_secret= ''
access_token=''
access_token_secret=''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


print('Choose an option (1 or 2): ')
print('1. Choose a topic to search tweets for. ')
print('2. Choose a Twitter Username to search tweets for. ')
input_data = raw_input()

if input_data=='1':
    print('Enter a topic: ')
    topic_name=raw_input()
    new_tweets = api.search(q=topic_name)
    for tweet in new_tweets:
        analysis = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer(), np_extractor= ConllExtractor())
        polarity = 'Positive'
        if (analysis.sentiment.p_pos < 0.50):
            polarity = 'Negative'
        print ("Sentiment Analysis and Topic of Interest")
        print ("Tweet : ",tweet.text)
        print ("Sentiment:",polarity)
        print ("Confidence :  Positive score: " ,analysis.sentiment.p_pos*100, "  Negative score: ", analysis.sentiment.p_neg*100 )
        print ("Areas of interest: ", analysis.noun_phrases)
        print "---------------------------------------------------------------------------"

else:
    print('2. Enter a Twitter Username to search tweets for: ')
    screen_name=raw_input()
    new_tweets = api.user_timeline(screen_name =screen_name,count=20)
    for tweet in new_tweets:
        analysis = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer(), np_extractor= ConllExtractor())
        polarity = 'Positive'
        if (analysis.sentiment.p_pos < 0.50):
            polarity = 'Negative'
        print ("Sentiment Analysis and Topic of Interest")
        print ("Tweet : ",tweet.text)
        print ("Sentiment:",polarity)
        print ("Confidence :  Positive score: " ,analysis.sentiment.p_pos*100, "  Negative score: ", analysis.sentiment.p_neg*100 )
        print ("Areas of interest: ", analysis.noun_phrases)
        print "---------------------------------------------------------------------------"


