from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
import xmltodict

def user(driver,u):

    driver.get(f"https://moshirewritten.com/services/rest/world/location/friends/{u}")
    html = driver.execute_script("return document.body.innerHTML;")

    k = html.split('</user></friend>')[0]
    a = k + "</user></friend></dynamic></location></status></xml>"
    root = xmltodict.parse(a)
    x = root['xml']['status']['location']['dynamic']['friend']['user']

    y = {
        "id": f"{x['@id']}"
    }

    return y