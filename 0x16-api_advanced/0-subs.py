#!/usr/bin/python3
""""module for finding the number of subbs"""
import json
import requests


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
        return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return 0
