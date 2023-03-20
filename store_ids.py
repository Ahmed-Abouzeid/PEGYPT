import json, pickle

jsn = [json.loads(line) for line in open('twitter_feed.jsonl', 'r')]
data_file = open('all_feed_labels.pkl', 'rb')
user_ids_file = open('all_users_ids.pkl', 'wb')
tweet_ids_file = open('all_tweets_ids.pkl', 'wb')

data = pickle.load(data_file)

tweet_ids = []
for tw in data:
    tweet_ids.append(tw['id'])

user_ids = set()
for feed in jsn:
    for tw in feed['data']:
        if tw['id'] in tweet_ids:
            user_ids.add(tw['author_id'])

pickle.dump(tweet_ids, tweet_ids_file)
pickle.dump(user_ids, user_ids_file)

user_ids_file.close()
tweet_ids_file.close()
