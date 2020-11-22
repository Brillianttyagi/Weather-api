from flask import Flask
from bs4 import BeautifulSoup
import requests as rq

app = Flask(__name__)

@app.route("/")
def weather(string):
    URL = 'https://www.google.com/search?sxsrf=ALeKk00FRBP16pdTMTktV3Br2ENOZ1-FXA%3A1606056896061&ei=wHu6X5ysA4yP4-EPiKGbuAI&q='+string+'+weather&oq='+string+'+weather&gs_lcp=CgZwc3ktYWIQAzINCAAQsQMQyQMQRhCAAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECCMQJzoECAAQQzoKCAAQsQMQgwEQQzoICAAQyQMQkQI6BQguELEDOggIABCxAxCDAToOCC4QsQMQgwEQxwEQowI6AgguOgUIABCxAzoLCC4QsQMQxwEQrwE6CggAELEDEMkDEEM6BQgAEJECOggILhDHARCvAToSCAAQsQMQyQMQFBCHAhBGEIACOgcIABAUEIcCOgQIABADUOG9Alio6wJg8_ECaABwAXgAgAHZCYgBnimSAQsyLTkuMi4yLjctMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwicjJ2WtJbtAhWMxzgGHYjQBicQ4dUDCA0&uact=5'
    page = rq.get(URL)

if __name == "__main__":
    app.run(debug=True)
