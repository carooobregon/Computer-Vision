from flask import Flask, request, render_template
import json
import twitterdata as twdata

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['tw_handle']
    processed_text = text.upper()
    print("text")
    print(processed_text)
    pos, neg = twdata.getPopularWordList(processed_text)
    return render_template("pic.html", data=pos)
    
if __name__ == "__main__":
    app.run(debug=True)