import requests
import json
import codecs

import config


class WikiCalls():


    def get_description(self, research):
        session = requests.Session()

        URL = "https://en.wikipedia.org/w/api.php"

        PARAMS = {
            "action": "query",
            "prop": "extracts",
            "exsentences": '5',
            "exlimit": "1",
            "titles": research,
            "explaintext": "1",
            "format": "json"
        }


        result = session.get(url=URL, params=PARAMS)



        reponse = result.json()

        page = reponse['query']['pages']
        for key in page:
            id = key

        extract = page[id]['extract']

        return extract

class MapCalls():


    def get_location(self, research):

        session = requests.Session()

        URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + research + "&key=" + config.GOOGLE_API_KEY

        R = session.get(URL).json()
        results = R['results']
        location = results[0]['geometry']['location']


        return location



MapCaller = MapCalls()
WikiCaller = WikiCalls()