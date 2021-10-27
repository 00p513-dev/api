from selenium import webdriver
from flask import Flask, request, jsonify, render_template, url_for
import xmltodict

def users(driver,u):

    driver.get(f"https://moshirewritten.com/services/rest/world/location/friends/{u}")
    html = driver.execute_script("return document.body.innerHTML;")

    k = html.split('</user></friend>')[0]
    a = k + "</user></friend></dynamic></location></status></xml>"
    root = xmltodict.parse(a)
    x = root['xml']['status']['location']['dynamic']['friend']['user']

    y = {
        "id": f"{x['@id']}",
        "age": f"{x['@age']}",
        "country": f"{x['@country']}",
        "gender": f"{x['@gender']}",
        "health": f"{x['monster']['@health']}",
        "happiness": f"{x['monster']['@happiness']}",
        "highest_puzzle_score": f"{x['monster']['@highestpuzzlescore']}",
        "pinboard_messages": f"{x['monster']['friends']['comments']['@comments']}",
        "pending_pinboard_messages": f"{x['monster']['friends']['comments']['@pendingcomments']}",
        "pending_friend_requests": f"{x['monster']['friends']['@pendingfriends']}",
        "gifts": f"{x['monster']['friends']['comments']['gifts']['@count']}"
    }

    return y