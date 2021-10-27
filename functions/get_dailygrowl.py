#!/usr/bin/env python3
import re
import requests
import json
from bs4 import BeautifulSoup

def dailygrowl():
    url = 'https://moshirewritten.com/blog/'
    links = requests.get(url)
    soup = BeautifulSoup(links.text, 'html.parser')
    
    
    # get the special user information
    # get right side
    right_side = soup.find('div',class_='right-side')
    
    get_monstar_of_the_week = right_side.find('div',id='monstar_of_the_week')
    monstar_of_the_week = get_monstar_of_the_week.find('a').text
    get_room_of_the_week = right_side.find('div',id='room_of_the_week')
    room_of_the_week = get_room_of_the_week.find('a').text
    

    
    k = {
        "stats": {
        "room_of_the_week": room_of_the_week,
        "monstar_of_the_week": monstar_of_the_week
        }
    }

    yield k
    
    # get left side
    left_side = soup.find('div',class_='left-side')
    get_category_links = left_side.find('ul',id='categorisation-nav')
    # get the category links
    for get_links in get_category_links.find_all('li'):
        links = get_links.find('a').get('href')
        category = get_links.find('a').text
        link = requests.get(links)
        soup = BeautifulSoup(link.text, 'html.parser')
        
        side = soup.find('div',class_='blog-article')
        get_article_info = side.find('div',class_='articles')
        get_article_info.find('div',class_="article-preview")
        try:
            # get the basic information
            get_article_image = get_article_info.find('img').get('src')
            get_article_link = get_article_info.find('a',class_='more').get('href')
            get_article_title = get_article_info.find('h3',class_='title').text
            get_article_description = get_article_info.find('p',class_='prev-p').text
            get_comment_amount = get_article_info.find('a',class_='comments-pre').text
            get_comment_amount = re.sub(r'\s','',get_comment_amount)
            get_comment_amount = re.sub(r'C.*','', get_comment_amount)

            # try to get the blog content if any at all.
            link = requests.get(get_article_link)
            soup = BeautifulSoup(link.text, 'html.parser')
            get_left = soup.find('div',class_='left-side')
            get_content = get_left.find('article',id='blogspot-content').text


        except AttributeError:
            continue

        
        y = {
            "link": f"{get_article_link}",
            "description": f"{get_article_description}",
            "image": f"{get_article_image}",
            "title": f"{get_article_title}",
            "category": f"{category}",
            "comment_amount": f"{get_comment_amount}",
            "content": f"{get_content}"
        }

        yield y