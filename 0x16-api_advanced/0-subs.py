#!/usr/bin/python3
import json
import requests
""""module for finding the number of subbs"""


def number_of_subscribers(subreddit):
    """class that finds the number of subscribers in Reddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        elif response.status_code == 302:
            return 0
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return 0
