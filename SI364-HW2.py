## HW 2 
## SI 364 F17
## Due: September 24, 2017
## 500 points

#####

## [PROBLEM 1]

## Edit the following Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, 
##you see a form that asks you to enter your favorite number. Once you enter a number and submit it to the form, you should then see a web 
##page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says 
##"Double your favorite number is 4". Careful about types in your Python code!
## 
##You can assume a user will always enter a number only.




from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
#import requests
import re
import nltk
import json
from pyzipcode import Pyzipcode as pz
import unittest
import pyzipcode
from uszipcode import ZipcodeSearchEngine
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import sqlite3
import webbrowser  



@app.route('/')
def hello_to_you():
    return 'Hello!'

# @app.route('/question',methods= ['POST','GET'])
# def enter_data():
# 	return render_template("hw2numberform.html")


# # @app.route('/form',methods= ['POST','GET'])
# # def enter_data():
# #     return render_template("student.html")

# if __name__ == '__main__':
#     app.run()

# <form action="http://localhost:5000/form1result" method="GET">
#   <input type="radio" name="genre" value="rock" checked>Rock<br>
#   <input type="radio" name="genre" value="pop">**Pop**<br>
#   <input type="radio" name="genre" value="electronica">Electronica<br>
#   <input type="submit" value="Submit">
# </form>


@app.route('/question',methods= ['POST','GET'])
def enter_data():
    s = """<!DOCTYPE html>
<html>
<body>

<form action="http://localhost:5000/result" method="GET">
  What is your favorite number?:<br>
  <input type="number" name="someid" value="">
  <br><br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>"""



    return s

@app.route('/result',methods = ['POST', 'GET'])
def res():
    if request.method == 'GET':
        result = request.args
        favnumber = result.get('someid')
        return 'Double your favorite number is ' + str(int(favnumber) * 2) + '   ( ' + favnumber + ' X2 )'





#########################    problem 2   ######################




@app.route('/soundcloud',methods= ['POST','GET'])
def sc_account():
    s = """<!DOCTYPE html>
<html>
<body>

<form action="http://localhost:5000/scresult" method="GET">
  Enter the username of a Soundcloud artist you like (found at the end of the url of their profile): <br> <br> (Please note that this may take a few minutes to load) <br> <br>
  <input type="text" name="account" value="">
  <br><br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>"""



    return s


def parseSoundcloud(x):
  
  z = str(x)
  # chromedriver = "files/chromedriver"
  # os.environ["webdriver.chrome.driver"] = chromedriver
  # driver = webdriver.Chrome(chromedriver)
  ####Possibility of opening the window of each account that is searched through, rather than doing it through phantom
  driver = webdriver.PhantomJS()
  driver.set_window_size(1120, 550)
  url = 'https://soundcloud.com/'+str(x)+'/tracks'
  driver.get(url)
  html = driver.page_source
  soup = BeautifulSoup(html, "html.parser")
  songlinks=[]

  scheight = .1
  while scheight < 9.9:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    scheight += .01
  #scrolls through the entire webpage so that all the songs are found, not just the first 10

  elem = driver.find_element_by_tag_name('a')

  for x in driver.find_elements_by_class_name('soundTitle__title'):
  #finds the link to each song of each user
    songlinks.append(x.get_attribute('href'))
    #stores this in a list
  driver.quit()
  
  return 'Here are the links to each of the songs found on this account: <br> <br>' + str('<br>'.join(songlinks))



@app.route('/scresult',methods = ['POST', 'GET'])

def soundcloud():
  if request.method == 'GET':
        result = request.args
        x = result.get('account')
        return parseSoundcloud(x)






## [PROBLEM 2]

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, 
##  and build it into the above code for a Flask application. It should:

# - not be an exact repeat of something you did in class, but it can be similar
# - should include an HTML form (of any kind: text entry, radio button, checkbox... feel free to try out whatever you want)
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form 
##   (text entered, radio button selected, etc). So if a user has to enter a number, it should do an operation on that number. 
##    If a user has to select a radio button representing a song name, it should do a search for that song in an API.

# You should feel free to be creative and do something fun for you -- 
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a 
# simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. 
# (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a 
# user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)




if __name__ == '__main__':
    app.run()






