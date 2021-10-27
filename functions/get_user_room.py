from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
import xmltodict
import json
import re

def room(driver,u):

    driver.get(f"https://moshirewritten.com/services/rest/world/location/friends/{u}")
    html = driver.execute_script("return document.body.innerHTML;")
    

    ro = []
    # part 1
    for g in html.split('<rooms style=')[1::]:
        g1 = re.findall(r'".*"', g)[0]
        e = g1.split('><')
        room_style = e[0].strip('"')
    # part 2
    for x in html.split('<room ')[1::]:
        r = re.findall(r'id=".*"', x)[0]
        e = "<room " + r + "></room>"  
        root = xmltodict.parse(e)
        ro.append(root['room']['@id'])

    room = {
        "rooms": ro,
        "style": room_style
    }

    # part 3
    room1 = []
    room2 = []
    room3 = []
    room4 = []
    room5 = []
    inventory = []

    for x in html.split('<item ')[1::]:
        try:
            r = re.findall(r'name=".*"', x)[0]
            j = "<item " + r + "></item>"
            root = xmltodict.parse(j)

            if root['item']['@roomid'] == '-1':
                inventory.append(root['item']['@id'])
            elif root['item']['@roomid'] == str(room['rooms'][0]):
                room1.append(root['item']['@id'])
            elif root['item']['@roomid'] == str(room['rooms'][1]):
                room2.append(root['item']['@id'])
            elif root['item']['@roomid'] == str(room['rooms'][2]):
                room3.append(root['item']['@id'])
            elif root['item']['@roomid'] == str(room['rooms'][3]):
                room4.append(root['item']['@id'])
            elif root['item']['@roomid'] == str(room['rooms'][4]):
                room5.append(root['item']['@id'])
        except:
            continue

    mos = []
    # part 4
    r = html.split('</moshlingstats></moshlings></stats></gifts></comments></friends>')[0]
    for x in r.split('<moshling ')[1::]:
        try:
            r = re.findall(r'name=".*"', x)[0]
            q = "<moshling " + r + "></moshling>"

            root = xmltodict.parse(q)  
            mos.append(root['moshling']['@name'])
        except: 
            continue


    y = {
        "inventory": inventory,
        "room1": room1,
        "room2": room2,
        "room3": room3,
        "room4": room4,
        "room5": room5,
        "house": room,
        "moshlings": mos
    }
    return y