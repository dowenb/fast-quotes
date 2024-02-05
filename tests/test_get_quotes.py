import requests

def test_random_quote():
    r = requests.get('http://localhost:8000/quote')
    assert r.status_code == 200
