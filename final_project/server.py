""" package installed in your venv, globally, user space"""
from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, request
from flask_cors import CORS

app = Flask("Web Translator")
CORS(app)

@app.route("/englishToFrench")
def english_to_french_get():
    text_to_translate = request.args.get('text')

    return english_to_french(text_to_translate)

@app.route("/frenchToEnglish")
def french_to_english_get():
    text_to_translate = request.args.get('text')

    return french_to_english(text_to_translate)

@app.route("/englishToFrench",methods=['POST'])
def english_to_french_post():
    text_to_translate = request.json['text']
    return english_to_french(text_to_translate)

@app.route("/frenchToEnglish",methods=['POST'])
def french_to_english_post():
    text_to_translate = request.json['text']
    # Write your code here
    return french_to_english(text_to_translate)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
