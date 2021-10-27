from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
import xmltodict

def streets(driver,id):

    driver.get(f"https://moshirewritten.com/services/rest/world/location/{id}")
    html = driver.execute_script("return document.body.innerHTML;")

    root = xmltodict.parse(html)

    x = root['xml']['status']['location']
    name = x['@name']
    x1 = x['dynamic']['actors']['pedestrians']['pedestrian']

    e = []
    try:
        for j in x1:
            e.append(j['@name'])
    except:
        e.append('couldn\'t fetch users')

    y = {
            "street": name,
            "data": e
        }

    return jsonify(y)