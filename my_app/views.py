from flask import Flask, render_template,url_for, request,jsonify
from my_app.api_calls import WikiCaller, MapCaller
from my_app.parser import Parser1

app = Flask(__name__)
app.config.from_object('config')





@app.route('/')
def index():
    return render_template('index.html')



@app.route('/result')
def result():
    question = request.args.get('question')
    key_word = Parser1.parse(question)
    description = WikiCaller.get_description(key_word)
    location = MapCaller.get_location(key_word)


    api_response = {'description': description, 'location': location, }
    return jsonify(api_response, question, key_word)