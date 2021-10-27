from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
import xmltodict
import json
import re

def shop(driver,id):


    driver.get(f"https://moshirewritten.com/services/rest/world/location/{id}")
    html = driver.execute_script("return document.body.innerHTML;")

    root1 = xmltodict.parse(html)
    name = root1['xml']['status']['location']['@name']

    e = []
    try:
        for x in html.split('<item args="" ')[1::]:
            r = re.findall(r'name=".*"', x)[0]
            j = "<item " + r + "></item>"

            root = xmltodict.parse(j)
            e.append(root['item']['@name'])
    # might not get all the items but an ok amount anyways.
    except:
        pass

    y = {
        "store": name,
        "shop": e
    }

    return jsonify(y)