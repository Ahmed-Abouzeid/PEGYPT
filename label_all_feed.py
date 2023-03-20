import pickle

labels_no_retweet_file = open('labels_no_retweet.pkl', 'rb')
labels_retweets_file = open('labels_retweets.pkl', 'rb')

labels_no_retweets = pickle.load(labels_no_retweet_file)
labels_retweets = pickle.load(labels_retweets_file)

all_feed_labels = []
matched_ids = set()

for e, record_main in enumerate(labels_no_retweets):
    print(e + 1)
    if record_main['id'] not in matched_ids:
        all_feed_labels.append(record_main)
        matched_ids.add(record_main['id'])

for e_, record_rt in enumerate(labels_retweets):
    print(e_ + e + 1 + 1)
    if record_rt['id'] not in matched_ids:
        all_feed_labels.append(record_rt)
        matched_ids.add(record_rt['id'])


all_feed_labels_file = open('all_feed_labels.pkl', 'wb')
pickle.dump(all_feed_labels, all_feed_labels_file)

print('Matched: ', len(all_feed_labels))
labels_retweets_file.close()
labels_no_retweet_file.close()
all_feed_labels_file.close()