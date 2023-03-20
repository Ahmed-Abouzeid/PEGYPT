import json, pickle

## to do yet


jsn = [json.loads(line) for line in open('twitter_feed.jsonl', 'r')]
tweet_ids_file = open('all_tweets_ids.pkl', 'rb')

tweet_ids = pickle.load(tweet_ids_file)
tweet_ids_file.close()

no_likes_tweets_ids = set()
test = []
for feed in jsn:
    for tw in feed['data']:
        if tw['id'] in tweet_ids:
            if tw['public_metrics']['like_count'] == 0:
                no_likes_tweets_ids.add(tw['id'])
                print('Tweet Indexed -->', tweet_ids.index(tw['id']), ' Had no likes')

t_no_likes_ids_file = open('tweet_ids_with_no_likes.pkl', 'wb')

pickle.dump(no_likes_tweets_ids, t_no_likes_ids_file)
print('Total Tweets with no likes -->', len(no_likes_tweets_ids),  ' out of-->', len(tweet_ids))

t_no_likes_ids_file.close()