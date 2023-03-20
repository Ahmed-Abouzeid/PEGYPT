import json, pickle

## to do yet

jsn = [json.loads(line) for line in open('twitter_feed.jsonl', 'r')]
users_ids_file = open('all_users_ids.pkl', 'rb')

users_ids = pickle.load(users_ids_file)
users_ids_file.close()

no_followers_users_ids = set()

c1 = 0
c2 = 0

matched_ids = set()
for feed in jsn:
    for meta in feed['includes']['users']:
        if meta['id'] in users_ids and meta['id'] not in matched_ids:
            if meta['public_metrics']['followers_count'] == 0:
                c1 += 1
            if meta['public_metrics']['following_count'] == 0:
                c2 += 1
            matched_ids.add(meta['id'])
            print(c1, c2)