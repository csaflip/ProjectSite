from flask import Flask, render_template, request, url_for, flash, redirect
from functions.tendybot import check_tendy
from functions.bunnygetter import get_bunny
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

@app.route('/budget')
def budget():
    conn = get_db_connection()
    columns = conn.execute('SELECT * FROM budget').fetchall()
    total = conn.execute('SELECT SUM(dollar) from budget').fetchone()[0]
    conn.close()
    return render_template('budget.html', columns=columns, total=total)