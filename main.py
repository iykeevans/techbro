import tweepy
import requests
import random
from time import sleep

# X API credentials (replace with yours)
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Authenticate with X
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Content bank
tips = [
    "Pro tip: Use Ctrl+Shift+F in VS Code to search like a boss.",
    "Debugging 101: Print statements > fancy tools sometimes."
]
memes = [
    "When your code works on the first try... suspicious.",
    "Me at 2 AM: 'One more line' — now it's 5 AM."
]
hot_takes = [
    "AI is 90% hype, 10% magic — prove me wrong.",
    "Low-code platforms are just training wheels for real devs."
]

# Function to post a tweet
def post_tweet(content):
    try:
        api.update_status(content)
        print(f"Tweeted: {content}")
    except tweepy.TweepyException as e:
        print(f"Error posting: {e}")

# Function to engage with tech posts
def engage_with_network():
    try:
        # Search for recent tech-related tweets
        tweets = api.search_tweets(q="#WebDev OR #AI -filter:retweets", lang="en", count=5)
        for tweet in tweets:
            reply = f"Cool take! I'd add: {random.choice(tips)}"
            api.update_status(reply, in_reply_to_status_id=tweet.id)
            print(f"Replied to @{tweet.user.screen_name}")
            sleep(60)  # Avoid rate limits
    except tweepy.TweepyException as e:
        print(f"Error engaging: {e}")

# Function to get a tech trend (using News API as an example)
def get_tech_trend():
    NEWS_API_KEY = "your_news_api_key"  # Get from newsapi.org
    url = f"https://newsapi.org/v2/top-headlines?category=technology&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json()["articles"]
        return articles[0]["title"] if articles else "No trend found"
    return "Tech trend fetch failed"

# Main run
if __name__ == "__main__":
    # Test posting
    post_tweet(random.choice(memes))
    
    # Test engagement
    engage_with_network()
    
    # Test trend
    trend = get_tech_trend()
    post_tweet(f"Hot off the press: {trend} — thoughts?")