from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
import functions.getUserID
import xmltodict
import json


def moshlings(driver,u):

    uid = functions.getUserID.user(u=u,driver=driver)['id']

    driver.get(f"https://moshirewritten.com/services/rest/moshling/sets/{uid}")
    html = driver.execute_script("return document.body.innerHTML;")
    y = json.loads(html)

    a = []
    for x in y['moshlingSets']:
        for j in x['moshlings']:
            if j['quantity'] > 0:
                a.append(j['name'])
            
    y = {
        "moshlings": a
    }

    return jsonify(y)