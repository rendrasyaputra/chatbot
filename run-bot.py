import aiml
import random
from library.preprocessing import preprocess
from flask import Flask, render_template, request

app = Flask(__name__)

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml")

@app.route("/")
def home():
    return render_template("home.html")

DEFAULT_RESPONSES = ["Maaf, kami tidak mengerti maksud pertanyaan anda",
                     "Maaf, kami tidak dapat mengerti pertanyaan anda, silakan ketikkan ulang pertanyaan anda",
					 "Pertanyaan yang anda inputkan tidak ada pada database kami, mohon masukkan pertanyaan lain",
                     ]

@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    print ("Inputan User : ", query )
    sentence = query
    preprocessed_text = preprocess(sentence)
    response = kernel.respond(preprocessed_text)
    x = response.replace("((", "<").replace("))", ">")
    print ("Jawaban Bot : ", x)
    if x is None or x == "":
        print (random.choice(DEFAULT_RESPONSES))
        return (random.choice(DEFAULT_RESPONSES))
        
    return x

if __name__ == "__main__":
    app.run(debug=True)