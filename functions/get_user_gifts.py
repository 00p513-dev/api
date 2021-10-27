from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
import functions.getUserID
import xmltodict
import json
import re


def gifts(driver,u):

    uid = functions.getUserID.user(u=u,driver=driver)['id']

    driver.get(f"https://moshirewritten.com/services/rest/user/gifts/{uid}")
    html = driver.execute_script("return document.body.innerHTML;")
    

    for x in html.split('<gift ')[1::]:
        # e = re.sub(r'gift name=', 'gift item=', x)
        r = re.findall(r'sendername=".*"', x)[0]
        e = "<gift " + r + "></gift>"

        root = xmltodict.parse(e)


        y = {
            "sender": root['gift']['@sendername'].rstrip('!'),
            "date": int(root['gift']['@receiveddate']),
            "message": root['gift']['@message'],
            "gift": root['gift']['@name'],
            "opened": root['gift']['@viewed']
        }

        yield y
