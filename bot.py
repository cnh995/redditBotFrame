#import
import praw
import time
import os
import pdb
import re
from RedditBot import *

#create a text file to store which posts have been replied to
if not os.path.isfile("postsRepliedTo.txt"):
    postsRepliedTo = []
else:
    with open("postsRepliedTo.txt", "r") as f:
        postsRepliedTo = f.read()
        postsRepliedTo = postsRepliedTo.split("\n")
        #postsRepliedTo = filter(None, postsRepliedTo)
        #python does not like the above line, so it can be excluded

#logging in to reddit
r = praw.Reddit(user_agent = "Test bot")
r.login("", "") #("USER", "PASS")

#words to test for in post name or comment body
words = ['build', 'debug', 'post', 'comment']

def run_bot():
#INSERT CODE HERE DEPENDING ON COMMENT OR POST SEARCH
#
#

#puts bot to sleep after running out of posts or comments to look for
while True:
    run_bot()
    time.sleep(10)
