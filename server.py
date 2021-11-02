# Flask is python microframework for servers
import flask
from flask import Flask
from flask import render_template
# BeautifulSoup is html parser
from bs4 import BeautifulSoup
# request - module to work with request and responses on server
import requests

# define app
app = Flask(__name__)

# default route
@app.route("/")
def hello():
    return "<p>Hello! <br> This message is for the default route</p>"

# route for /quote - shows the best quote from bash.im 25 random quotes
@app.route("/quote")
def quote():
    resp = requests.get('https://bash.im/random')
    soup = BeautifulSoup(resp.text, 'lxml')
    quotes = soup.find_all("div", {"class": "quote__body"}) #get divs with quotes
    total = soup.find_all("div", {"class": "quote__total"}) #get marks for this quotes
    # map array with marks to integer, sometimes mark is '...'
    mapped_total = list(map(lambda x: 0 if x.contents[0] == '...' else int(x.contents[0]), total))
    # get the index of the best quote
    max_index = mapped_total.index(max(mapped_total))
    # return html template with inserted quote
    return render_template('index.html', quote=quotes[max_index])
# start server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8081"), debug=True)

# changes to test auto-build on dockerhub 0
