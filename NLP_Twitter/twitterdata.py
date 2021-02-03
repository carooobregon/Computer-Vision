from flask import Flask, request, render_template
import os
import tweepy as tw
import pandas as pd
import sentiment_mod as s
import json
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 

consumer_key="RMwN469nFVYLhLk38JsgGjaLg"
consumer_secret="LTiNnztJOmZDbYcVZQeM53GiTCGJAiv1HxVFj1Z8nWVluTX6v9"
access_key="80962536-TesurxqdCeFDdMWQycsEWMfVIdeyoTNhNGb2npr6Y"
access_secret="DyEWGEIZ5scsnbq6uvwSule0YAN5RXZFP21TnLX2ElcsU"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tw.API(auth)

stwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "like"]

def deleteMentions(line):
    split_line = line.split(" ")

    final_split_string = []

    for word in split_line:
        skip_word = False
        if word in stwords:
            skip_word = True
        for letter in word:
            if letter == '@':
                #check if the current word contains a mention
                skip_word = True

        if not skip_word:
            #skip a word if it contains mention
            final_split_string.append(word)

    final_string = " ".join(final_split_string)
    return final_string

def cleanData(txt):
    txt = deleteMentions(txt)
    txt = txt.replace("\n", "").replace("RT", "").replace("https","").replace("co", "").replace("McDonald", "").replace("Twitter", "").replace("mcdonald", "")
    return txt

def getTweetsDictionary(search_words):
    # Define the search term and the date_since date as variables
    date_since = "2020-02-01"
    neg_tweets = {}
    pos_tweets = {}
    # Collect tweets
    tweets = tw.Cursor(api.search,
                  q=search_words,
                  lang="en",
                  since=date_since).items(100)
    for tweet in tweets:
        sentiment_value, confidence = s.sentiment(tweet.text)
        
        if 'RT' not in tweet.text:
            tweet.text = cleanData(tweet.text)
            tweetWords = tweet.text.split()
       #     print(tweet.text, sentiment_value, confidence)
            if confidence*100 >= 80 and sentiment_value == 'pos':
                for word in tweetWords:
        #            print(word)
         #           print("..")
                    pos_tweets[word] = pos_tweets[word] + 1 if word in pos_tweets else 1
            if confidence*100 >= 80 and sentiment_value == 'neg':
                for word in tweetWords:
          #          print(word)
           #         print("..")
                    neg_tweets[word] = neg_tweets[word] + 1 if word in neg_tweets else 1
    return (pos_tweets, neg_tweets)

def wordReps(dic):
    output = []
    for key in dic:
        temp_dic = {}
        temp_dic["x"] = key
        temp_dic["value"] = dic[key]
        output.append(temp_dic)
    return output
  #  print(output)

def getPopularWordList(word):
    pos, neg = getTweetsDictionary(word)
    pos_dic, neg_dic = wordReps(pos), wordReps(neg)
    print(pos_dic)
    return (pos_dic, neg_dic)