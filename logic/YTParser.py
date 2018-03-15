import urllib.request
import urllib.parse
import requests
from bs4 import BeautifulSoup
import re


class YTParser:

    def __init__(self):
        pass

    def get_queries(self, input):

        mozhdr = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}

        requests.get("https://www.youtube.com", headers=mozhdr)

        query_string = "search_query=" + input
        web_page = "http://www.youtube.com/results?" + query_string

        sb_get = requests.get(web_page, headers=mozhdr)

        souped_data = BeautifulSoup(sb_get.content, "html.parser")
        yt_links = souped_data.find_all("a", class_="yt-uix-tile-link")
        list_of_videos = {}

        for x in yt_links:
            list_of_videos[x.get("title")] = "https://www.youtube.com/" + x.get("href")

        return list_of_videos
