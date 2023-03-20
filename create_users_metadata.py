import json, pickle

jsn = [json.loads(line) for line in open('twitter_feed.jsonl', 'r')]
user_ids_file = open('all_users_ids.pkl', 'rb')

u_ids = pickle.load(user_ids_file)
ordered_u_ids = sorted([int(id) for id in u_ids])
user_ids_file.close()
edges_dict = {}

users_meta_data = []
matched_users = set()

c = 0
for feed in jsn:
    for u_meta in feed['includes']['users']:
        if u_meta['id'] in u_ids:
            if u_meta['id'] not in matched_users:
                c += 1
                users_meta_data.append(u_meta)
                matched_users.add(u_meta['id'])
                print('user metadata add, index: ', c)

meta_data_file = open('users_meta_data.pkl', 'wb')
pickle.dump(users_meta_data, meta_data_file)
meta_data_file.close()

