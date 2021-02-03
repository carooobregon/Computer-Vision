from flask import Flask, request, render_template
import os
import tweepy as tw
import pandas as pd
import sentiment_mod as s
import json
import pickle
import twitterdata as twdata
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 

app=Flask(__name__,template_folder='templates')
@app.route("/")
def home():
    pos, neg = twdata.getPopularWordList("mcdonalds")
    print(pos)
    return render_template("pic.html", data=pos)
 
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    print(processed_text)
    return render_template("pic.html", data=pos)
    
if __name__ == "__main__":
    app.run(debug=True)