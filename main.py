from time import sleep
import instaloader

print("Start")
L = instaloader.Instaloader()
# Login or load session
#
try: L.load_session_from_file("spider_modelsx")
except: L.login("spider_modelsx", "Idan05423")        # (login)

from datetime import datetime
from itertools import dropwhile, takewhile
from datetime import date, timedelta
import instaloader

print("Start")
L = instaloader.Instaloader()

# for post in instaloader.Hashtag.from_name(L.context, 'cat').get_posts():
for post in instaloader.Profile.from_username(L.context, "stabilo").get_posts():
    L.download_post(post, target='stabilo')
    break

# posts = instaloader.Profile.from_username(L.context, "stabilo").get_posts()
# print(posts.count)
#
# SINCE = datetime(2020, 1, 1)
SINCE = date.today() - timedelta(days=1)
# UNTIL = datetime(2021, 1, 1)
UNTIL = date.today()
#
