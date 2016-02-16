#PASTE INTO FILE CREATION AREA OF BOT.PY
if not os.path.isfile("commentsRepliedTo.txt"):
    commentsRepliedTo = []
else:
    with open("commentsRepliedTo.txt", "r") as f:
        commentsRepliedTo = f.read()
        commentsRepliedTo = commentsRepliedTo.split("\n")
        #commentsRepliedTo = filter(None, commentsRepliedTo)
        #python doesn't like the line above


#PASTE INTO FUNCTION AREA OF BOT.PY
    comments = subreddit.get_comments(limit = 50)  #searches comments
    keywords = [''] #sets up keywords to look for
    for comment in comments:
        comment_text = comment.body.lower()
        commentMatch = any(string in comment_text for string in keywords) #searches for matches between comment body and keywords list
        if commentMatch and comment.id not in commentsRepliedTo:
            comment.reply('') #enter comment reply in quotes
            commentsRepliedTo.append(comment.id)
            with open("commentsRepliedTo.txt", "w") as f: #adds comment id to a list, so it will never be replied to again
                for comment_id in commentsRepliedTo:
                    f.write(comment_id + "\n")
