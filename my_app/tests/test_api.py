from my_app.views import WikiCaller, MapCaller, app
from requests import HTTPError
import requests
from unittest import mock, TestCase
from my_app.api_calls import WikiCalls





class WikiTest(TestCase):

    # def __init__(self):
    #
    #     self.server_wiki_response = None
    #
    #
    # def test_wiki_server(self):
    #     URL = "https://en.wikipedia.org/w/api.php"
    #
    #     PARAMS = {
    #         "action": "query",
    #         "prop": "extracts",
    #         "exsentences": '5',
    #         "exlimit": "1",
    #         "titles": 'Paris',
    #         "explaintext": "1",
    #         "format": "json"
    #     }
    #
    #     response = requests.get(url=URL, params=PARAMS)
    #
    #     assert response.status_code != 500
    #     if response.status_code == 500:
    #        print('server down')
    #     self.server_wiki_response = response


    @mock.patch.object(WikiCalls, 'get_description', return_value= 'test')
    def test_wiki_call_result(self, mock_get_description):
        """
        GIVEN
        WHEN
        THEN

        """

        self.assertEqual(WikiCalls.get_description(), 'test')
        mock_get_description.assert_called_once()


def test_map_call_result():
        app.config.from_object('my_app.tests.config')

        return app
        session = requests.Session()

        URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + keyword + "&key=" + app.config.GOOGLE_API_KEY

        response = session.get(URL).json()
        results = response['results']
        location = results[0]['geometry']['location']

        assert response.status_code == 200

        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'





