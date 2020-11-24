from flask import Flask,jsonify
from bs4 import BeautifulSoup
import requests as rq

app = Flask(__name__)

@app.route("/<string:string>")
def weather(string):
    URL = 'https://www.google.com/search?q='+string+' weather'
    page = rq.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results=soup.find('div', class_='BNeawe iBp4i AP7Wnd')
    temp = results.text
    result=soup.find('div', class_='BNeawe tAd8D AP7Wnd')
    time = result.text
    return jsonify(temperature = temp,time = time)

if __name__ == "__main__":
    app.run(debug=True)
