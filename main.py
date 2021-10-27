import functions.get_street_users
import functions.get_users
#import functions.get_users_cloths
import functions.get_shop_stock
import functions.get_user_moshlings
import functions.rateUser_LOL
import functions.get_user_room
import functions.get_user_gifts
import functions.get_users_profile
import functions.get_dailygrowl
import functions.get_user_pinboard
from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
from waitress import serve
import json
import random
import time

app = Flask(__name__)


fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
driver = webdriver.Firefox(options=fireFoxOptions)
driver.get("http://moshirewritten.com/login")


with open('accounts.json') as s:
    data = json.load(s)
    info = random.choice(data)


driver.find_element_by_id("username").send_keys(info['username'])
driver.find_element_by_id("password").send_keys(info['password'])
driver.find_element_by_id("login-btn").click()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/whoamiloggedinas123/', methods=['GET'])
def check():
    return render_template('logged.html',info=info)


@app.route('/gifts/<u>', methods=['GET'])
def gift(u):
    return jsonify(list(functions.get_user_gifts.gifts(driver=driver,u=u)))

@app.route('/room/<u>', methods=['GET'])
def ro(u):
    return functions.get_user_room.room(driver=driver,u=u)

@app.route('/rate/<u>', methods=['GET'])
def rat(u):
    return functions.rateUser_LOL.rate(driver=driver,u=u)

@app.route('/zoo/<u>', methods=['GET'])
def zo(u):
    return functions.get_user_moshlings.moshlings(driver=driver,u=u)

@app.route('/dailygrowl/', methods=['GET'])
def da():
    return jsonify(list(functions.get_dailygrowl.dailygrowl()))

@app.route('/profile/<u>', methods=['GET'])
def n(u):
    return functions.get_users_profile.profile(driver=driver,u=u)

@app.route('/player/<u>', methods=['GET'])
def player(u):
    return functions.get_users.users(driver=driver,u=u)

@app.route('/pinboard/<u>', methods=['GET'])
def pb(u):
    return jsonify(list(functions.get_user_pinboard.pinboard(driver=driver,u=u)))

@app.route('/shop/<id>', methods=['GET'])
def store(id):
    return functions.get_shop_stock.shop(driver=driver,id=id)

@app.route('/street/<id>', methods=['GET'])
def road(id):
    return functions.get_street_users.streets(driver=driver,id=id)

#functions.get_newest_users.newest_users(driver=driver)
#functions.get_users.users(driver=driver)
#functions.get_users_cloths.cloths(driver=driver)
#functions.get_shop_stock.shop(driver=driver)
#functions.get_street_users.streets(driver=driver)

#application = app

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
