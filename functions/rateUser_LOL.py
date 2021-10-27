from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
import xmltodict

def rate(driver,u):

    driver.get(f"https://moshirewritten.com/services/ratings/{u}/{u}/5")
    html = driver.execute_script("return document.body.innerHTML;")

    root = xmltodict.parse(html)
    x = root['xml']['status']

    y = {
        "status": f"{x['@text']}"
    }

    return y