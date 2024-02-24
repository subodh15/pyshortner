from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['url']
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    return short_url

if __name__ == '__main__':
    app.run(debug=True)
