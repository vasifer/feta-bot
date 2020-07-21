'''
This is a twitter bot. Retrieves tweets containing keywords, then reaplces those keywords and retweets corrected tweet.
Credentials are stored in config module.
Read more here: https://realpython.com/twitter-bot-python-tweepy/
'''

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def change(api, keywords):
    logger.info("Retrieveing original tweet")
    originalTweet = api.search(q=keywords, lang="el", count=1)
    for tweet in originalTweet:
        logger.info(f"{tweet.text}")
        textNew = ((tweet.text).replace(keywords, 'φέτα'))
        print("replaced!")
        logger.info(textNew)
        api.update_status(textNew)

def main():
    api = create_api()
    while True:
        change(api, 'αγάπη')
        logger.info("Waiting...")
        time.sleep(3600)

if __name__ == "__main__":
    main()
