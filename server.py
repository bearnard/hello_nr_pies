initialize('./newrelic.ini', 'integration')

from bottle import Bottle, run
import urllib2

app = Bottle()

@app.route('/hello')
def hello():
    r = urllib2.urlopen('https://www.google.com/')
    return "Hello World!"

run(app, host='localhost', port=8080)
