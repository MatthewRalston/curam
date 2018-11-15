#!/usr/bin/env python3

import sys
import urllib.request
import xmltodict
import re
from dateutil.parser import parse


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def upgrade_alerts(last_upgrade = False):

    url = 'https://www.archlinux.org/feeds/news/'
    file = urllib.request.urlopen(url)
    data = file.read()
    file.close()

    arch_news = xmltodict.parse(data)

    exit_code = 0
    for news_post in arch_news['rss']['channel']['item']:
        if last_upgrade == False or parse(news_post['pubDate']).replace(tzinfo=None) >= parse(last_upgrade):
            exit_code = 1
            print('~' * 75)
            print("TITLE: ", news_post['title'])
            print("DATE: ", news_post['pubDate'])
            print("DESCRIPTION: ", clean_html(news_post['description']))
            print("\n")
    
    return exit_code


if __name__ == '__main__':
    sys.exit(upgrade_alerts(sys.argv[1])) if len(sys.argv) > 1 else upgrade_alerts()