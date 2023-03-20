import pickle
import json


def get_labels(tweet_id, labels):
    for record in labels:
        if tweet_id == record['id']:
            return record['bias'], record['propaganda']
    return None, None

labels = pickle.load(open('labels_no_retweet.pkl', 'rb'))
labels_retweets = []

jsn = [json.loads(line) for line in open('twitter_feed.jsonl', 'r')]
for feed in jsn:
    for tw in feed['data']:
        if 'referenced_tweets' in tw.keys():
            for x in tw['referenced_tweets']:
                if x['type'] == 'retweeted':
                    main_tweet_id = x['id']
                    bias, propaganda = get_labels(main_tweet_id, labels)
                    if bias != None:
                        print(tw['id'], tw['text'], main_tweet_id, bias, propaganda)
                        print('--------------------------------------------------------------------')
                        labels_retweets.append({'id': tw['id'], 'text': tw['text'], 'bias': bias, 'propaganda': propaganda})

labels_file = open('labels_retweets.pkl', 'wb')
pickle.dump(labels_retweets, labels_file)
print('Matched : ', len(labels_retweets))
labels_file.close()
