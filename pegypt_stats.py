import pickle
import json

data_file = open('all_feed_labels.pkl', 'rb')

data = pickle.load(data_file)
bias_ag = 0
bias_with = 0
bias_neu = 0
prop_yes = 0
prop_no = 0

bias_ag_prop_yes = 0
bias_with_prop_yes = 0

bias_ag_prop_no = 0
bias_with_prop_no = 0

tweet_ids = []
for tw in data:
    tweet_ids.append(tw['id'])
    if tw['bias'] == 0:
        bias_neu += 1
    elif tw['bias'] == 1:
        bias_with += 1
    elif tw['bias'] == -1:
        bias_ag += 1

    if tw['propaganda'] == 1:
        prop_yes += 1
    elif tw['propaganda'] == 0:
        prop_no += 1

    if tw['bias'] == 1 and tw['propaganda'] == 1:
        bias_with_prop_yes += 1
    elif tw['bias'] == 1 and tw['propaganda'] == 0:
        bias_with_prop_no += 1
    if tw['bias'] == -1 and tw['propaganda'] == 1:
        bias_ag_prop_yes += 1
    elif tw['bias'] == -1 and tw['propaganda'] == 0:
        bias_ag_prop_no += 1

jsn = [json.loads(line) for line in open('twitter_feed.jsonl', 'r')]

user_ids = set()
for feed in jsn:
    for tw in feed['data']:
        if tw['id'] in tweet_ids:
            user_ids.add(tw['author_id'])

events_num = len(data)
network_size = len(user_ids)

print('Num of Users: ', network_size)
print('Num of Events: ', events_num)
print('Perc of Propaganda: ', prop_yes/events_num)
print('Perc of Non Propaganda: ', prop_no/events_num)
print('Perc of Biased with: ', bias_with/events_num)
print('Perc of Biased against: ', bias_ag/events_num)
print('Perc of Neutral Bias: ', bias_neu/events_num)
print('Perc of Biased with + Propaganda: ', bias_with_prop_yes/events_num)
print('Perc of Biased with + Non Propaganda: ', bias_with_prop_no/events_num)
print('Perc of Biased against + Propaganda: ', bias_ag_prop_yes/events_num)
print('Perc of Biased against + Non Propaganda: ', bias_ag_prop_no/events_num)

data_file.close()



