from flask import Flask, render_template, request
from functions.tendybot import check_tendy
from functions.bunnygetter import get_bunny
from functions.randomwiki import scrape_wiki_article
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tender')
def tender():
     # send chicken tender information
    return render_template('tender.html', tender_message=check_tendy())
    
@app.route('/bunny')
def bunny():
    get_bunny() # update bunny pic
    return render_template('bunny.html')

@app.route('/wiki')
def wiki():
    return render_template('wiki.html')

@app.route('/wikiresult',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      wikilink = scrape_wiki_article(url=result['art'], counter=0, iterations=4)
      return render_template("wikiresult.html", wikilink = wikilink)