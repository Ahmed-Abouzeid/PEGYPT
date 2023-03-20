import os
import pickle
import time
import subprocess

ids_file = open('all_tweets_ids.pkl', 'rb')
tw_ids = pickle.load(ids_file)
ids_file.close()

no_likes_ids_file = open('tweet_ids_with_no_likes.pkl', 'rb')
no_likes_ids = pickle.load(no_likes_ids_file)
no_likes_ids_file.close()

fetched_already_ids = []
files = os.listdir('likes/')
for f in files:
    fetched_already_ids.append(f.split('_')[0])

for i, id in enumerate(tw_ids):
    if id not in fetched_already_ids and id not in no_likes_ids:
        print('collecting liking users of tweet indexed: ', i, ' -- ', id)
        command_str = 'twarc2 liking-users '+id+ ' ./likes/' + id+'_liking_users.jsonl'
        p = subprocess.Popen(command_str, shell=True, close_fds=True)
        p.wait()
    else:
        print('Already Fetched! or Has no Likes')
