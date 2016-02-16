#PASTE INTO FILE CREATION AREA OF BOT.PY
if not os.path.isfile("postsRepliedTo.txt"):
    postsRepliedTo = []
else:
    with open("postsRepliedTo.txt", "r") as f:
        postsRepliedTo = f.read()
        postsRepliedTo = postsRepliedTo.split("\n")
        #commentsRepliedTo = filter(None, postsRepliedTo)
        #python doesn't like the line above


#PASTE INTO FUNCTION AREA OF BOT.PY
    submissions = subreddit.get_hot(limit = 50) #can change to find new post, hot posts, controversial, etc
    keywords = [''] #looks for keywords in post title
    for submission in submissions:
        post_text = submission.title.lower()
        postMatch = any(string in post_text for string in keywords) #checks for match between post title and keywords
        if postMatch and submission.id not in postsRepliedTo:
            submission.add_comment('') #enter comment text in quotes
            postsRepliedTo.append(submission.id)
            with open("postsRepliedTo.txt", "w") as f: #adds comment id to a list, so it will never be replied to again
                for post_id in postsRepliedTo:
                    f.write(post_id + "\n")
