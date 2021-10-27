from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
import functions.getUserID
import xmltodict
import json
import base64
import re


def pinboard(driver,u):
    uid = functions.getUserID.user(u=u,driver=driver)['id']

    driver.get(f"https://moshirewritten.com/services/comments/{uid}")
    html = driver.execute_script("return document.body.innerHTML;")

    root = xmltodict.parse(html)

    core = root['xml']['status']
    try:
        for x in core['messages']['message']:
            status = x['@status']
            watermark = x['@watermark']
            sent = x['@sentdate']
            username = x['user']['@username']
            message = x['#text']
            # e = base64.b64decode(message)

            y = {
                "status": status,
                "watermark": int(watermark),
                "sent": int(sent),
                "username": username,
                "message": message
            }
            yield y
    except KeyError:
        y = {
            "error": "no messages"
        }
        
        yield y