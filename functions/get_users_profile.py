from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
import functions.getUserID
import xmltodict
import json


def profile(driver,u):
    f = open('profile_values.json','r')
    e = json.load(f)

    uid = functions.getUserID.user(u=u,driver=driver)['id']

    driver.get(f"https://moshirewritten.com/services/rest/user/profile/{uid}/inroomothersprofile")
    html = driver.execute_script("return document.body.innerHTML;")

    root = xmltodict.parse(html)

    value = root['profile']['usermonsterprofile']['userprofile']

    colors = e['colors'][int(value['@favouritecolour'])]
    food = e['food'][int(value['@favouritefood'])]
    music = e['music'][int(value['@favouritemusic'])]
    moods = e['moods'][int(value['@currentmood'])]
    
    try:
        moshlings = e['moshlings'][int(value['@favouritemoshling'])-1]
    except IndexError:
        moshlings = ''

    y = {
        "rooms": rooms,
        "fav_color": colors,
        "fav_food": food,
        "fav_music": music,
        "mood": moods,
        "fav_moshling": moshlings
        
    }

    return jsonify(y)