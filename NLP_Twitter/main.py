from flask import Flask, request, render_template
import json
import twdata as twdata

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
    print(request.form)
    pos, neg = twdata.getPopularWordList(processed_text)
    if 'positive-rev' in request.form:
        data = pos
        print("positive")
    else:
        data = neg
    return render_template("pic.html", data=data)
    
if __name__ == "__main__":
    app.run(debug=True)