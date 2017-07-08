#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datagen/opensentiment_get_tweets as twitter
from textblob.classifiers import NaiveBayesClassifier
import csv

class SimpleSentimentAnalysis(object):
    def __init__(self, train_sample_percentage, tweet_csv):
        self.train_sample_percentage = 0.0
        self.tweet_csv = ""
        try:
            self.train_sample_percentage = float(train_sample_percentage)
        except ValueError:
            print("Unable to read input train sample percentage, setting to 1/5 of the dataset")
            self.train_sample_percentage = 0.20

        if tweet_csv is not None or tweet_csv is not "":
            self.tweet_csv = tweet_csv
        else:
            raise ValueError("Unable to set tweet csv path!")

    def get_data_from_csv(self):
        pass
