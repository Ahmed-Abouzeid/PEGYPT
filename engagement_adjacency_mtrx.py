import os
import pickle
import json
import subprocess
import numpy as np


def get_tweet_author(to_fetch_tweet_id, tweets_with_authors, network_users_ids):
    for t_id, au_id in tweets_with_authors:
        if t_id == to_fetch_tweet_id and au_id in network_users_ids:
            return au_id


def get_needed_users_ids(author_id, all_passed_ids, network_ids):
    needed_ids = []
    for id in all_passed_ids:
        if id != author_id and id in network_ids:
            needed_ids.append(id)

    return needed_ids


def store_engagements(idx1, eng_ids, adj_mtrx, sorted_ids):

    for id in eng_ids:
        if id is not None:
            idx2 = sorted_ids.index(int(id))
            adj_mtrx[idx1][idx2] += 1

    return adj_mtrx


print('Acquiring Feed Data from File...')
t_ids_file = open('all_tweets_ids.pkl', 'rb')
t_ids = pickle.load(t_ids_file)
t_ids_file.close()

n_ids_file = open('all_users_ids.pkl', 'rb')
network_users_ids = pickle.load(n_ids_file)
n_ids_file.close()

tweets_with_authors = []
lines_f = open('twitter_feed.jsonl', 'r')
jsn = [json.loads(line) for line in lines_f]
lines_f.close()

tweet_with_other_engagements = dict()
matched_ids = set()

for feed in jsn:
    for tw in feed['data']:

        if tw['id'] in matched_ids:
            continue
        if tw['id'] in t_ids:
            tweets_with_authors.append((tw['id'], tw['author_id']))
            if 'referenced_tweets' in tw.keys():
                tweet_with_other_engagements.update({tw['id']:[]})
                for ref in tw['referenced_tweets']:
                    tweet_with_other_engagements[tw['id']].append(ref['id'])

            matched_ids.add(tw['id'])

print('Needed Tweet Feed Has Been Filtered and Stored...')

files = os.listdir('likes/')
l = len(files)
eng_info_all = dict()
for e, f in enumerate(files):
    tweet_id = f.split('_')[0]
    liking_info = [json.loads(line) for line in open('./likes/'+f, 'r')]
    liking_ids = []
    for info in liking_info[0]['data']:
        liking_ids.append(str(info['id']).strip('\n'))
        author_id = get_tweet_author(tweet_id, tweets_with_authors, network_users_ids)
        liking_ids = get_needed_users_ids(author_id, liking_ids, network_users_ids)
    eng_info_all.update({author_id: liking_ids})


for t_id, ref_t_ids in tweet_with_other_engagements.items():
    key_id = get_tweet_author(t_id, tweets_with_authors, network_users_ids)
    ref_ids = []
    for ref_id in ref_t_ids:
        ref_ids.append(get_tweet_author(ref_id, tweets_with_authors, network_users_ids))
    if key_id in eng_info_all.keys():
        eng_info_all[key_id] += ref_ids
    else:
        eng_info_all.update({key_id: ref_ids})


matched_ids = set()
for feed in jsn:
    for tw in feed['data']:
        if tw['id'] in matched_ids or tw['author_id'] not in network_users_ids or tw['id'] not in t_ids:
            continue
        mentions_u_ids = []
        other_u_ids = []
        if 'referenced_tweets' in tw.keys():
            for ref in tw['referenced_tweets']:
                other_u_ids.append(get_tweet_author(ref['id'], tweets_with_authors, network_users_ids))

        if 'entities' in tw.keys():
            for e in tw['entities']:
                if e == 'mentions':
                    for m in tw['entities'][e]:
                        if m['id'] not in other_u_ids and m['id'] in network_users_ids:
                            mentions_u_ids.append(m['id'])
        if tw['author_id'] in eng_info_all.keys():
            eng_info_all[tw['author_id']] += mentions_u_ids
        else:
            eng_info_all.update({tw['author_id']: mentions_u_ids})
        matched_ids.add(tw['id'])


u_ids_sorted = sorted([int(i_d) for i_d in network_users_ids])
#print(u_ids_sorted)
adj_mtrx = np.zeros((len(u_ids_sorted), len(u_ids_sorted)), dtype=int)
print('Final Adjacency Matrix Creation Started...')

added = []
for e, u_id in enumerate(u_ids_sorted):
    print('Processing User ', e + 1, 'Out Of ', len(u_ids_sorted))
    adj_mtrx = store_engagements(e, eng_info_all[str(u_id)], adj_mtrx,  u_ids_sorted)

adj_mtrx_f = open('final_symmetric_mtrx.pkl', 'wb')
pickle.dump(adj_mtrx, adj_mtrx_f)
adj_mtrx_f.close()



