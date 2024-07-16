#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If not a valid subreddit, returns 0.
    """
    # Define the URL for the subreddit's about endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/username)'}
    
    # Make a request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response and return the subscriber count
        return response.json().get('data', {}).get('subscribers', 0)
    else:
        # If the subreddit is not valid or any other error, return 0
        return 0
