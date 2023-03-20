import pickle
import collections

temp_circles_f = open('temporal_circles.pkl', 'rb')
all_feed_labels_f = open('all_feed_labels.pkl', 'rb')
temp_circles_dict = pickle.load(temp_circles_f)
all_feed_labels = pickle.load(all_feed_labels_f)
final_labeled_dataset_f = open('final_labeled_dataset.pkl', 'wb')


def get_tweet_text(tweet_id):
    for dict_entry in all_feed_labels:
        if dict_entry['id'] == tweet_id:
            return dict_entry['text']


def create_circles_edges(circles_info_list):
    circles = []
    for bias, is_propaganda in circles_info_list:
        if bias == 0 and is_propaganda == 0:
            circles.append('A')
        elif bias == -1 and is_propaganda == 0:
            circles.append('B')
        elif bias == 1 and is_propaganda == 0:
            circles.append('C')
        elif bias == 0 and is_propaganda == 1:
            circles.append('D')
        elif bias == -1 and is_propaganda == 1:
            circles.append('E')
        elif bias == 1 and is_propaganda == 1:
            circles.append('F')
    return collections.Counter(circles)


final_dataset = []
for k, v in temp_circles_dict.items():
    print(k, v[4])
    row = dict({'tweet_time': v[0], 'tweet_user_id': v[1], 'tweet_id': k, 'tweet_text': get_tweet_text(k),
                'tweet_bias_label': v[2], 'tweet_is_propaganda_label': v[3], 'tweet_temporal_circles_edges': create_circles_edges(v[4])})
    print(row)
    exit()
    final_dataset.append(row)

pickle.dump(final_dataset, final_labeled_dataset_f)

final_labeled_dataset_f.close()
all_feed_labels_f.close()
temp_circles_f.close()
