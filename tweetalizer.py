# read in a tweet
# how many characters are in my tweet
# am I within the limit?
# how many hashtags are there?
# what are the hashtags
# how many @mentions are there
# what are the @mentions

import sys


def tweetalize():
    print("Welcome to the awesometastic tweetalizer! Start analyzing your tweets now!")

    while True:
        maxLength = 140
        tweet = raw_input("What tweet would you like to analyze? To quit, just enter 'q'. ") #if using python 3, use input function

        if tweet == 'q' or tweet == 'Q':
            exit()

        print("Tweet is " + str(len(tweet)) + " characters long")
        if len(tweet) > maxLength:
            print("The number of characters in this tweet is too damn high!\nThe limit is 140.")

        hashtag = 0
        for words in tweet.split(' '):
            if words[0] == "#":
                print("Tweet contains the hashtag: " + words)
                hashtag += 1
        print("The tweet has " + str(hashtag) + " total #hashtags")

        mention = 0
        for words in tweet.split(' '):
            if words[0] == "@":
                print("Tweet contains the mention: " + words)
                mention += 1
        print("The tweet has " + str(mention) + " total @mentions")


tweetalize()
