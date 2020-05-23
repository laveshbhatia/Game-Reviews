from typing import Any

from datetime import date
from flask import Flask, redirect, request, url_for, render_template, session  # multiple import statement
import sys
import sqlite3
from bs4 import BeautifulSoup
from requests import get
from array import *

app = Flask(__name__)
COMMENTS = 'comments.db'  # setting up the database html has to link to
app.secret_key = "super secret key"


def insertdallas(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database #connecting with the database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into dallascomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def insertguestbook(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database #connecting with the database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into guestbook VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database #closing the connection


def insertfaze(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database #connecting with the database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into fazecomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def insertoptic(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into opticcomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def inserttoronto(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into torontocomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def insertflorida(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into floridacomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def insertlondon(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into londoncomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def inserthuntsmen(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into huntsmencomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def insertparis(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into pariscomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def insertseattle(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into seattlecomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def insertnewyork(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into newyorkcomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def insertla(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into lacomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


def insertregister(username, email, password):  # Creating a function

    params = {'username': username, 'email': email, 'password': password, }  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into users VALUES (:username, :email, :password)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


@app.route('/lacomments', methods=['POST'])
def lacomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertla(request.form['name'], request.form['comment'])  # enterting the params
        return redirect(url_for('losangeles'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


def insertminnesota(name, comment):  # Creating a function
    """
    put a new entry in the database
    """
    params = {'name': name, 'comment': comment}  # enterting the params
    connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
    cursor = connection.cursor()  # initiating connection
    cursor.execute("insert into minnesotacomments VALUES (:name, :comment)",
                   params)  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database


@app.route('/minnesotacomments', methods=['POST'])
def minnesotacomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertminnesota(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('minnesota'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/home')
def home():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        stock()
        cdl()
        actual_content=cdl()
        stock_price = stock()
        return render_template('index.html',content=actual_content,stock=stock_price)
    except:  # What condition should be initiated if there an error
        error = "Please reload the page"
        return render_template('index.html', error = error)  # Exception case


@app.route('/')
def index():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        stock()
        cdl()
        actual_content=cdl()
        stock_price = stock()
        return render_template('index.html',content=actual_content,stock=stock_price)
    except:  # What condition should be initiated if there an error
        error = "Please reload the page"
        return render_template('index.html', error=error)
        # Exception case


@app.route('/dallascomments', methods=['POST'])
def dallascomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertdallas(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('dallas'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/huntsmencomments', methods=['POST'])
def huntsmencomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        inserthuntsmen(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('chicago'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/fazecomments', methods=['POST'])
def fazecomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertfaze(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('faze'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/floridacomments', methods=['POST'])
def floridacomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertflorida(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('florida'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/opticcomments', methods=['POST'])
def opticcomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertoptic(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('optic'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/seattlecomments', methods=['POST'])
def seattlecomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertseattle(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('seattle'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/londoncomments', methods=['POST'])
def londoncomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertlondon(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('london'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/pariscomments', methods=['POST'])
def pariscomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertparis(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('paris'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/newyorkcomments', methods=['POST'])
def newyorkcomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertnewyork(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('newyork'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/torontocomments', methods=['POST'])
def torontocomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        inserttoronto(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('toronto'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/guestbookcomments', methods=['POST'])
def guestbookcomments():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        insertguestbook(request.form['name'], request.form['comment'])  # getting the values from html
        return redirect(url_for('aboutus'))
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/registerpage', methods=['POST'])
def registerpage():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        query = "select username from users where username = '" + request.form[
            'username'] + "';"  # getting the values from html
        connection = sqlite3.connect(COMMENTS)
        cur = connection.execute(query)
        rv = cur.fetchall()
        cur.close()  # Ending connection with the database
        if len(rv) == 0:
            insertregister(request.form['username'], request.form['email'], request.form['password'])
            return redirect(url_for('login'))
        else:
            return render_template('login.html',
                                   wrong="Sorry, '" + request.form['username'] + "' username already exists")
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/login', methods=['POST', 'GET'])
def login():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        if request.method == 'POST':
            query = "select * from users where username = '" + request.form['username']
            query = query + "' and password = '" + request.form['password'] + "';"
            connection = sqlite3.connect(COMMENTS)  # Initiating a connection with the database comments
            cur = connection.execute(query)  # Initiating the query entered above in the database.
            rv = cur.fetchall()  # Fetching all entries for the query entered above
            cur.close()  # Ending connection with the database
            if len(rv) == 1:  # If there is an entry of such a username and password in the table, it will login
                session['username'] = request.form['username']  # Setting the username in session cookies
                session['logged in'] = True  # Stating the user is logged in which would allow them to post comments
                return redirect('/')  # If the username matches, the user is redirected to the home page
            else:
                return render_template('login.html',
                                       msg="Username/Password Incorrect!")  # If the database is not able to match the username or password it prints the error
        else:
            return render_template('login.html')  # Returning the homepage
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/logout')
def logout():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        session.pop('logged in', None)  # It removes the session cookies related to logged in
        session.pop('username', None)  # It removes the usersame from the cookies
        return redirect('/')  # Redirects to the homepage if the user click logout
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/aboutus')
def aboutus():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        try:
            url = 'https://weather.com/weather/today'
            response = get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            weather = soup.find("div", {"class": "today_nowcard-temp"}).span.text
            insert = insertWeather
            insert.insertWeather(weather)
        except:
            error = "Please reload the page"
            return render_template('about.html', error=error)  # Exception case
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM guestbook")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template("about.html",entries=allentries, weather=weather)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/teams')
def teams():  # Creating a function
    try:

        url = 'https://cod-esports.gamepedia.com/'
        response = get(url)
        news = []
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find("table", {"class": "news-table"}).tbody
        for table in table.findAll("tr"):
            for team in table.findAll("td"):
                news.append(team.text)  # this code gets for top 4 teams

        counter = 0
        while (counter < 3):
            country = news[counter]
            counter += 1
            league = news[counter]
            counter += 1
            news_now = news[counter]
            counter += 1

        callNews = insertNews()
        callNews.insertNews(country, league, news_now)
        return render_template("teams.html", country=country, league=league, news=news_now)
    except:
        error = "Please reload the page"
        return render_template('teams.html', error = error)  # Exception case



@app.route('/dallas', methods=['POST', 'GET'])
def dallas():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        dallasUpdate()
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM dallascomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        update = dallasUpdate()
        return render_template("dallas.html",
                               entries=allentries,update=update)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/faze', methods=['POST', 'GET'])
def faze():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM fazecomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('faze.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/florida', methods=['POST', 'GET'])
def florida():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated

        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM floridacomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('florida.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/chicago', methods=['POST', 'GET'])
def chicago():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM huntsmencomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('chicago.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/london', methods=['POST', 'GET'])
def london():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM londoncomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('london.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/losangeles', methods=['POST', 'GET'])
def losangeles():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM lacomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('losangeles.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/minnesota', methods=['POST', 'GET'])
def minnesota():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM  minnesotacomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('minnesota.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/newyork', methods=['POST', 'GET'])
def newyork():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM newyorkcomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('newyork.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/optic', methods=['POST', 'GET'])
def optic():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM opticcomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('optic.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/paris', methods=['POST', 'GET'])
def paris():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM pariscomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('paris.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/seattle', methods=['POST', 'GET'])
def seattle():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM seattlecomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('seattle.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route('/toronto', methods=['POST', 'GET'])
def toronto():  # Creating a function
    try:  # Putting the code in try, incase there is an error in the code below, except statement wil be initiated
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute("SELECT * FROM torontocomments")  # Getting the values from the table in the database
        allentries = cursor.fetchall()  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template('toronto.html',
                               entries=allentries)  # Sending the values from the database to display on the website
    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case


@app.route("/player", methods=["POST", "GET"])

def player():
    if request.method == "POST":
        try:
            name = request.form["playerteam"]
            playerinfo(name)
            image(name)
            info = playerinfo(name)
            real_name = info[2]
            Age = info[6]
            Country = info[8]
            Team = info[10]
            role = info[12]
            content = insertPlayer()
            content.insertPlayer(real_name, Age, Country, Team, role)
            img_src = image(name)
            return render_template("player_info.html", input=name, name=real_name, age=Age, country=Country, team=Team, life=role, image=img_src)
        except:
            error = "Please enter the correct player's name and try again"
            return render_template("player_info.html",error=error,input=name)
    else:
        return render_template("player_info.html")  # Exception case

class insertPlayer:
    def insertPlayer(self, name, age, country, team, role):
            parmas = {"name": name, "age": age, "country": country, "team": team, "role":role}
            connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
            cursor = connection.cursor()  # initiating connection
            cursor.execute(
                "insert into playerinfo VALUES (:name, :age, :country, :team, :role)", parmas
            )
            connection.commit()
            cursor.close()

def playerinfo(name):
    playername = name
    actual_url = "https://cod-esports.gamepedia.com/"
    url = actual_url + playername
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    leaderboard_table = soup.find("table", {"class": "infobox infobox-player-narrow InfoboxPlayer"}).tbody
    standings = []

    for name in leaderboard_table.findAll("tr"):
        for td in name.findAll("td"):
            standings.append(td.text)
    return standings

def image(name):
    playername = name
    actual_url = "https://cod-esports.gamepedia.com/"
    url = actual_url + playername

    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    leaderboard_table = soup.find("table", {"class": "infobox infobox-player-narrow InfoboxPlayer"}).tbody
    img_src = leaderboard_table.find("div", {"class": "floatnone"}).img['src']
    return img_src


@app.route("/leaderboard", methods=["POST", "GET"])
def scrapLeaderboard():
    try:
        scrapingLeaderboard()
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute(
            "SELECT * FROM leaderboard order by rank asc"
        )  # Getting the values from the table in the database
        connection.commit()
        allentries = (
            cursor.fetchall()
        )  # Fetching the entries and storing it in allentries
        cursor.close()  # Ending connection with the database
        return render_template("leaderboard.html" , entries=allentries)
    except:
        error = "We are sorry but we cannot retrieve the leaderboard. Please try again after few minutes"
        return render_template("leaderboard.html", error=error)
def scrapingLeaderboard():
    url = 'https://en.wikipedia.org/wiki/Template:2020_Call_of_Duty_League_standings' #scraping site
    response = get(url) #getting the url
    standings = [] #Creating an array
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("table", {"class": "wikitable"}).tbody #Finding elements
    for standing in table.findAll("tr", {"style": "background-color:#ccffcc;"}):
        for team in standing.findAll("td"):
            standings.append(team.text) #this code gets for top 4 teams
    for standing1 in table.findAll("tr", {"style": "background-color:#ffebcd;"}):
        for team1 in standing1.findAll("td"):
            standings.append(team1.text) #this code gets for top 5-8 teams
    for standing2 in table.findAll("tr", {"style": "background-color:#;"}):
        for team2 in standing2.findAll("td"):
            standings.append(team2.text)  # this code gets for top 8-12 teams
    counter = 0
    while (counter<len(standings)): #Checks length of array
        rank = standings[counter] #Retrieves values from array with index number
        counter+=1
        team = standings[counter] #Retrieves values from array with index number
        counter+=1
        points = standings[counter] #Retrieves values from array with index number
        counter+=1
        matches = standings[counter] #Retrieves values from array with index number
        counter+=1
        wins = standings[counter] #Retrieves values from array with index number
        counter+=1
        losses = standings[counter] #Retrieves values from array with index number
        checkLeaderboard(rank, team, points, matches, wins, losses) # Sends the values to add or update in table
        counter = counter + 5


class addTable:
    def updateLeaderboard(rank, teams, points, matches, wins, losses):
        params = (rank , teams , points , matches , wins , losses, teams)  # enterting the params
        connection = sqlite3.connect(
            COMMENTS
        )  # Connecting to the comments.db database #connecting with the database
        cursor = connection.cursor()  # initiating connection
        update = ''' UPDATE leaderboard SET rank = ? ,team = ? ,points = ?, matches = ?, wins = ?, losses = ? WHERE team = ?'''
        cursor.execute(update, params)  # inserting values to the table in database
        connection.commit()
        cursor.close()

    def insertLeaderboard(rank, teams, points, matches, wins, losses):  # Creating a function
        """
        put a new entry in the database
        """
        params = {"rank": rank, "team": teams, "points": points, "matches": matches, "wins": wins, "losses": losses}  # enterting the params
        connection = sqlite3.connect(
            COMMENTS
        )  # Connecting to the comments.db database #connecting with the database
        cursor = connection.cursor()  # initiating connection
        cursor.execute(
            "insert into leaderboard VALUES (:rank, :team, :points, :matches, :wins, :losses)", params
        )  # inserting values to the table in database
        connection.commit()
        cursor.close()  # Ending connection with the database #closing the connection


def checkLeaderboard(rank, teams, points, matches, wins, losses):
    try:
        content = addTable
        connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
        cursor = connection.cursor()  # initiating connection
        cursor.execute(
            "SELECT * FROM leaderboard")  # Getting the values from the table in the database
        connection.commit()
        allentries = cursor.fetchall()
        cursor.close
        if len(allentries) == 0:
            content.insertLeaderboard(rank, teams, points, matches, wins, losses)
        else:
            params = {"name": teams}
            connection = sqlite3.connect(COMMENTS)  # Connecting to the comments.db database
            cursor = connection.cursor()  # initiating connection
            cursor.execute("SELECT (:name) FROM leaderboard",params)  # Getting the values from the table in the database
            connection.commit()
            rv = cursor.fetchall()  # Fetching the entries and storing it in allentries
            cursor.close()
            if len(rv) == 0:
                content.insertLeaderboard(rank, teams, points, matches, wins, losses)
            else:
                content.updateLeaderboard(rank, teams, points, matches, wins, losses)

    except:  # What condition should be initiated if there an error
        return render_template('error.html', msg=sys.exc_info())  # Exception case



class insertNews:
    def insertNews(self, country, league, news_now):
        params = {"country": country, "league": league, "news": news_now}  # enterting the params
        connection = sqlite3.connect(
            COMMENTS
        )  # Connecting to the comments.db database #connecting with the database
        cursor = connection.cursor()  # initiating connection
        cursor.execute(
            "insert into news VALUES (:country, :league, :news)", params
        )  # inserting values to the table in database
        connection.commit()
        cursor.close()  # Ending connection with the database #closing the connection

class insertWeather:
    def insertWeather(weather):
        params = {"weather": weather}  # enterting the params
        connection = sqlite3.connect(
            COMMENTS
        )  # Connecting to the comments.db database #connecting with the database
        cursor = connection.cursor()  # initiating connection
        cursor.execute(
            "insert into weather VALUES (:weather)", params
        )  # inserting values to the table in database
        connection.commit()
        cursor.close()  # Ending connection with the database #closing the connection

def cdl():
    url = 'https://en.wikipedia.org/wiki/Call_of_Duty_League' #Getting values for static content
    response = get(url)
    activision = [] #Array
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find("div", {"class": "mw-parser-output"})
    for activision_content in content.findAll("p"): #Finds all P tags on the site
        activision.append(activision_content.text)

    a = activision[1] # Selects only the index number 1
    b = a.replace("[1]", "")  #Filtering Data to remove unwanted characters
    c = b.replace("[2]", "") #Filtering Data to remove unwanted characters
    actual_content = c.replace("[3]", "") #Filtering Data to remove unwanted characters
    insertCdl(actual_content) #Calling the insert table function
    return actual_content

def insertCdl(cdl):
    params = {"cdl": cdl}  # enterting the params
    connection = sqlite3.connect(
        COMMENTS
    )  # Connecting to the comments.db database #connecting with the database
    cursor = connection.cursor()  # initiating connection
    cursor.execute(
        "insert into cdl VALUES (:cdl)", params
    )  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database #closing the connection

def stock(): #Retrieving the value of stock
    url = 'https://www.cnbc.com/quotes/?symbol=ATVI' #Launching the url
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    a = soup.find("div", {"class": "quote-leftrail"})
    b = a.find("div", {"class": "quotestrip"})
    c = b.find("span", {"class": "last original"})
    stock_price = c.text #getting the text from the scraped elements
    insertStock(stock_price)
    return stock_price

def insertStock(stock):
    params = {"stock": stock}  # enterting the params
    connection = sqlite3.connect(
        COMMENTS
    )  # Connecting to the comments.db database #connecting with the database
    cursor = connection.cursor()  # initiating connection
    cursor.execute(
        "insert into stock VALUES (:stock)", params
    )  # inserting values to the table in database
    connection.commit()
    cursor.close()  # Ending connection with the database #closing the connection

def dallasUpdate():
    url = 'https://www.dallasempire.com/'
    response = get(url)
    team = []
    soup = BeautifulSoup(response.text, 'html.parser')
    d = soup.find("body", {"id": "collection-5dec171b5704156dcbe9bde7"})
    for a in d.findAll("img"):
        team.append(a.get("src"))
    dallas_update = team[2]
    return dallas_update