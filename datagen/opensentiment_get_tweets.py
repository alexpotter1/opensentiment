#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Credit to github.com/yanofsky for basic ideas.

# Give data to this in the format of a dictionary with 'user_key', 'user_secret', 'access_key' and 'access_secret' as dictionary keys.

import tweepy
import csv

class TwitterScrape(object):
    def __init__(self, twitter_api_credentials):

        # Variable definitions here
        self.credentials = dict()

        if isinstance(twitter_api_credentials, dict):
            for credential in twitter_api_credentials.values():
                if credential is None or credential is "":
                    raise ValueError("Twitter API credential is empty/NoneType")
        else:
            raise ValueError("Twitter API credentials must be supplied as a dictionary.")

        self.credentials = twitter_api_credentials

    def get_tweets_for_user(self, user_name):
        # Max tweet count: 3240

        authentication = tweepy.OAuthHandler(self.credentials['user_key'], self.credentials['user_secret'])
        authentication.set_access_token(self.credentials['access_key'], self.credentials['access_secret'])
        api = tweepy.API(auth)

        # Twitter (like Facebook/Graph API) has a limit on maximum tweets received per API request (200 tweets)
        all_tweets = []

        tweets = api.user_timeline(screen_name=user_name, count=200)
        print("Getting tweets for user: %s" % user_name)
        all_tweets.extend(tweets)

        # Keep getting more tweets, until no more are left
        max_id_last = all_tweets[-1].id - 1
        while len(tweets) > 0:
            print("Getting more tweets before max_id=%s" % max_id)

            tweets = api.user_timeline(screen_name=user_name, count=200, max_id=max_id_last)
            all_tweets.extend(tweets)

            max_id_last = all_tweets[-1].id - 1

        tweet_output = [[tweet.id_str, tweet.created_at, tweet.text.encode('utf-8')] for tweet in all_tweets]
        with open('%s_tweets.csv' % user_name, 'wb') as file:
            writer = csv.writer(file)
            writer.writerow(["id","created_at","text"])
            writer.writerows(tweet_output)

        return
