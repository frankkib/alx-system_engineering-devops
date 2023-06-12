#!/usr/bin/python3
"""module that finds the number of hot posts"""
import json
import requests


def top_ten(subreddit):
    """class that queries Reddit API and prints out the
    first ten hot post
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Custom User Agent"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            if len(posts) > 0:
                for post in posts:
                    title = post["data"]["title"]
                    print(title)
            else:
                print("No posts found.")
        elif response.status_code == 302:
            print("None")
        else:
            print("Error: {}".format(response.status_code))
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
