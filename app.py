from flask import Flask, render_template
import requests



app = Flask(__name__)


NEWS_API_KEY = '18fcf7b8357444d4bcf94d9d80a735bb'
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
INDIA_NEWS_PARAMS = {'country': 'in', 'category': 'general'}



@app.route('/')
def index():
    response = requests.get(NEWS_API_ENDPOINT, params={**INDIA_NEWS_PARAMS, **{'apiKey': NEWS_API_KEY}})
    articles = response.json()['articles'][:10]
    return render_template('index.html', articles=articles)


if __name__ == '__main__':
    app.run()