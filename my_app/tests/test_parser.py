from my_app.parser import Parser1

def test_parser():
    parse_sentence = Parser1.parse('Tu connais Paris')
    assert parse_sentence == 'paris'