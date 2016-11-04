import tweepy
from textblob import TextBlob
from prettytable import PrettyTable
import sys

#Enter credentials to get Twitter access to get tweets
consumer_key= '#'
consumer_secret= '#'
access_token='#'
access_token_secret='#'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Enter a topic to search for tweets
print('Enter a topic to search tweets for: ')
input_data = raw_input()
public_tweets = api.search(q=input_data)

#Create a table to visualise tweets and sentiments
pt = PrettyTable(field_names=['Tweet', 'Sentiment'])

#Get tweets and sentiments
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    polarity = 'Positive'
    if (analysis.sentiment.polarity < 0):
        polarity = 'Negative'
    pt.add_row([tweet.text, polarity])
    print (pt)
