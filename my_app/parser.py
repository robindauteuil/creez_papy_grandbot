import re
import json


class Parser:

    def parse(self, sentence):
        sentence = re.sub("[^\w ]", ' ', sentence)
        with open('my_app/stopwords-json/dist/fr.json') as stopwords :
            stop_array = json.load(stopwords)


        lower_sentence = sentence.lower().split(' ')
        parse_reponse = []
        for word in lower_sentence:

            if word not in stop_array:
                parse_reponse.append(word)

        return parse_reponse





Parser1 = Parser()


