import praw

reddit = praw.Reddit(client_id='hkG-k_Os2mso2w',
                     client_secret='jRyIHBTcP2adPRUs0G8sA6BKMSk',
                     user_agent='Karmaxer by /u/Karmaxer')

subreddit = reddit.subreddit('funny')

def get_titles():
    thesetitles = []
    for submission in subreddit.top('day', limit=25):
        titles = submission.title
        thesetitles.append(titles)
    return thesetitles