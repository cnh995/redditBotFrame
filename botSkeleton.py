#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Above lines are added for Linux compatibility

#import
import praw
import time
import os
import pdb
import re
from RedditBot import *

#INSERT FILE CREATOR
#INSERT FILE CREATOR
#INSERT FILE CREATOR
#INSERT FILE CREATOR
#INSERT FILE CREATOR

#logging in to reddit
r = praw.Reddit(user_agent = "Test bot")
r.login("", "") #("USER", "PASS")

#words to test for in post name or comment body
words = ['build', 'debug', 'post', 'comment']

def run_bot():
    subreddit = r.get_subreddit("") #insert subreddit in double quotes
    #INSERT FUNCTION HERE
    #INSERT FUNCTION HERE
    #INSERT FUNCTION HERE
    #INSERT FUNCTION HERE
    #INSERT FUNCTION HERE

#puts bot to sleep after running out of posts or comments to look for
while True:
    run_bot()
    time.sleep(10)
