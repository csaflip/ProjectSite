from flask import Flask, render_template, request, url_for, flash, redirect
from functions.tendybot import check_tendy
from functions.bunnygetter import get_bunny
from functions.randomwiki import scrape_wiki_article
import sqlite3

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'yeet'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

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
      inputform = request.form
      print(inputform['iterations'])
      wikiscrape = scrape_wiki_article(url=inputform['art'], counter=0, iterations=int(inputform['iterations']))
      wikititle = wikiscrape.split(': ')[0]
      wikilink = wikiscrape.split(': ')[1]
      return render_template("wikiresult.html", wikilink = wikilink, wikititle = wikititle)


@app.route('/budget', methods=('GET', 'POST'))
def budget():
    if request.method == 'GET':
        conn = get_db_connection()
        columns = conn.execute('SELECT * FROM budget').fetchall() # commit not needed because fetching values
        total = conn.execute('SELECT SUM(dollar) from budget').fetchone()[0]
        conn.close()
        return render_template('budget.html', columns=columns, total=total)
    elif request.method == 'POST':
        if 'reset button' in request.form:
            conn = get_db_connection()
            conn.execute('DELETE FROM budget')
            conn.commit() # must commit changes to database
            conn.close()
            return redirect(url_for('budget'))

        category = request.form['category']
        item = request.form['item']
        cost = request.form['cost']

        if not category: # if category not entered
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO budget (category, notes, dollar) VALUES (?, ?, ?)',
                         (category, item, cost))
            conn.commit()
            conn.close()
            return redirect(url_for('budget'))
