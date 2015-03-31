# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


class Twitter_methods(object):

    """
    Methods for scrapping twitter.com
    """

    def __init__(self, username, password):
        """
        Retrieving data
        """
        self.username = str(username)
        self.password = str(password)
        self.session = requests.Session()

    def auth(self):
        """
        Authorizing on twitter.com
        """
        r = self.session.get('https://mobile.twitter.com/session/new')
        s = r.content
        token = BeautifulSoup(s).find("input", {"name": "authenticity_token"}).get('value')
        data = {"authenticity_token": token,
                "username": self.username,
                "password": self.password,
                "remember_me": "1",
                "commit": "Log+in"}
        url = "https://mobile.twitter.com/session"
        r = self.session.post(url, data=data)

    def get_user_tweets(self, user_name, number_of_tweets):
        """
        Return list of users tweets
        """
        url = 'https://mobile.twitter.com/{}'.format(user_name)
        tweets_list = list()
        while True:
            r = self.session.get(url)
            soup = BeautifulSoup(r.content)
            temp = soup.findAll("table", {"class": "tweet"})
            tweets_list.extend([x.get('href').split('/')[-1][:-4] for x in temp])
            if len(tweets_list) >= number_of_tweets:
                break
            url = soup.find("div", {"class": "w-button-more"})
            url = BeautifulSoup(str(url)).find('a').get('href')
        return tweets_list[:number_of_tweets]

    def get_followers(self, user_name):
        """
        Returns list of users followers
        """
        url = 'https://mobile.twitter.com/{}/followers'.format(user_name)
        followers_list = list()
        while True:
            r = self.session.get(url)
            soup = BeautifulSoup(r.content)
            temp = soup.findAll("span", {"class": "username"})
            followers_list.extend(list(filter(lambda x: x != user_name, [x.text[1:] for x in temp])))
            url = soup.find("div", {"class": "w-button-more"})
            if not url:
                break
            url = BeautifulSoup(str(url)).find('a').get('href')
        return followers_list

    def get_following(self):
        """
        Return list of users who are followed by the user
        """
        url = 'https://mobile.twitter.com/{}/following'.format(user_name)
        following_list = []
        while True:
            r = self.session.get(url)
            soup = BeautifulSoup(r.content)
            temp = soup.findAll("span", {"class": "username"})
            following_list.extend(filter(lambda x: x != user_name, map(lambda x: x.text[1:], temp)))
            url = soup.find("div", {"class": "w-button-more"})
            if not url:
                break
            url = 'https://mobile.twitter.com{}'.format(BeautifulSoup(str(url)).find('a').get('href'))
        return following_list
