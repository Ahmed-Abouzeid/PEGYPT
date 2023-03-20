import pickle, json
import pandas as pd


def get_temporal_circle(current_time_bound, user_id, tweets_with_authors, network_user_ids,  tweet_to_tweet_engagements, tweet_to_user_engagement, all_feed):
    time_stamp = None
    circles = []


    def time(rows):
        return (pd.Timestamp(rows.year, rows.month,
                             rows.day, rows.hour, rows.minute))

    split_time_stamp = current_time_bound.split('T')
    yr1 = int(split_time_stamp[0].split('-')[0])
    mn1 = int(split_time_stamp[0].split('-')[1])
    dy1 = int(split_time_stamp[0].split('-')[2])
    hr1 = int(split_time_stamp[1].split(':')[0])
    min1 = int(split_time_stamp[1].split(':')[1])
    sc1 = int(split_time_stamp[1].split(':')[2].split('.')[0])

    for t_id, user_ids in tweet_to_user_engagement.items():
        if user_id in user_ids:
            mentioning_u_id, time_stamp = get_tweet_author_with_timing(t_id, tweets_with_authors, network_user_ids)
            if mentioning_u_id != user_id and time_stamp is not None:
                split_time_stamp = time_stamp.split('T')
                yr0 = int(split_time_stamp[0].split('-')[0])
                mn0 = int(split_time_stamp[0].split('-')[1])
                dy0 = int(split_time_stamp[0].split('-')[2])
                hr0 = int(split_time_stamp[1].split(':')[0])
                min0 = int(split_time_stamp[1].split(':')[1])
                sc0 = int(split_time_stamp[1].split(':')[2].split('.')[0])

                df = pd.DataFrame({
                    'year': [yr0, yr1],
                    'month': [mn0, mn1],
                    'day': [dy0, dy1],
                    'hour': [hr0, hr1],
                    'minute': [min0, min1],
                    'second': [sc0, sc1]})
                df['new_time'] = df.apply(time, axis='columns')
                if df['new_time'][0] < df['new_time'][1]:
                    bias = all_feed[t_id][0]
                    is_propaganda = all_feed[t_id][1]
                    circles.append((time_stamp, bias, is_propaganda))

    for t_id, t_ids in tweet_to_tweet_engagements.items():
        citing_author_id, time_stamp = get_tweet_author_with_timing(t_id, tweets_with_authors, network_user_ids)
        split_time_stamp = time_stamp.split('T')
        yr0 = int(split_time_stamp[0].split('-')[0])
        mn0 = int(split_time_stamp[0].split('-')[1])
        dy0 = int(split_time_stamp[0].split('-')[2])
        hr0 = int(split_time_stamp[1].split(':')[0])
        min0 = int(split_time_stamp[1].split(':')[1])
        sc0 = int(split_time_stamp[1].split(':')[2].split('.')[0])
        df = pd.DataFrame({
            'year': [yr0, yr1],
            'month': [mn0, mn1],
            'day': [dy0, dy1],
            'hour': [hr0, hr1],
            'minute': [min0, min1],
            'second': [sc0, sc1]})
        df['new_time'] = df.apply(time, axis='columns')
        if citing_author_id == user_id and time_stamp is not None and df['new_time'][0] < df['new_time'][1]:
            for cited_tweet_id in t_ids:
                cited_author_id, _ = get_tweet_author_with_timing(cited_tweet_id, tweets_with_authors, network_user_ids)
                if cited_author_id != user_id:
                    bias = all_feed[cited_tweet_id][0]
                    is_propaganda = all_feed[cited_tweet_id][1]
                    circles.append((time_stamp, bias, is_propaganda))

        matched = set()
        for cited_tweet_id in t_ids:
            cited_author_id, _ = get_tweet_author_with_timing(cited_tweet_id, tweets_with_authors,
                                                                             network_user_ids)
            if citing_author_id != user_id and cited_author_id == user_id and time_stamp is not None and cited_tweet_id not in matched:
                matched.add(cited_tweet_id)
                if df['new_time'][0] < df['new_time'][1]:
                    citing_author_id, _ = get_tweet_author_with_timing(t_id, tweets_with_authors,
                                                                       network_user_ids)
                    bias = all_feed[t_id][0]
                    is_propaganda = all_feed[t_id][1]
                    circles.append((time_stamp, bias, is_propaganda))


    # to do: add the opposite way also for tweet_with_tweets, means when a user in a references tweet, not referencing herself.
    # because the circules are defined as the exposures: when you are mentioned in a content, when you cite a content, when your content is cited!
    return circles


def get_tweet_author_with_timing(to_fetch_tweet_id, tweets_with_authors, network_users_ids):
    for t_id, au_id, t in tweets_with_authors:
        if t_id == to_fetch_tweet_id and au_id in network_users_ids:
            return au_id, t
    return None, None

n_ids_file = open('all_users_ids.pkl', 'rb')
network_users_ids = pickle.load(n_ids_file)
n_ids_file.close()

t_ids_file = open('all_tweets_ids.pkl', 'rb')
t_ids = pickle.load(t_ids_file)
t_ids_file.close()

tweets_with_authors = []

lines_f = open('twitter_feed.jsonl', 'r')
jsn = [json.loads(line) for line in lines_f]
lines_f.close()

tweet_to_tweet_engagements = dict()
tweet_to_user_engagements = dict()

matched_ids = set()
for feed in jsn:
    for tw in feed['data']:
        mentions_u_ids = []
        other_u_ids = []
        if tw['id'] in matched_ids:
            continue
        if tw['id'] in t_ids:
            tweets_with_authors.append((tw['id'], tw['author_id'], tw['created_at']))

        matched_ids.add(tw['id'])
matched_ids = set()
for feed in jsn:
    for tw in feed['data']:
        mentions_u_ids = set()
        other_u_ids = []
        if tw['id'] in matched_ids or tw['id'] not in t_ids:
            continue

        if 'referenced_tweets' in tw.keys():
            tweet_to_tweet_engagements.update({tw['id']:set()})
            for ref in tw['referenced_tweets']:
                if ref['id'] in t_ids:
                    tweet_to_tweet_engagements[tw['id']].add(ref['id'])
                    u_id, time_stamp = get_tweet_author_with_timing(ref['id'], tweets_with_authors, network_users_ids)
                    if u_id is not None:
                        other_u_ids.append(u_id)

        if 'entities' in tw.keys():
            for e in tw['entities']:
                if e == 'mentions':
                    for m in tw['entities'][e]:
                        if m['id'] not in other_u_ids and m['id'] in network_users_ids:
                            mentions_u_ids.add(m['id'])
        tweet_to_user_engagements.update({tw['id']: mentions_u_ids})

        matched_ids.add(tw['id'])



all_feed_labels_file = open('all_feed_labels.pkl', 'rb')
all_feed_labels = pickle.load(all_feed_labels_file)

all_feed_labels_dict = dict()
for record in all_feed_labels:
    all_feed_labels_dict.update({record['id']: [record['bias'], record['propaganda']]})

citing_temporal_circles_network = dict()
for e, record in enumerate(all_feed_labels):
    print(e)
    u_id, time_stamp = get_tweet_author_with_timing(record['id'], tweets_with_authors, network_users_ids)
    temporal_circles = get_temporal_circle(time_stamp, u_id, tweets_with_authors, network_users_ids, tweet_to_tweet_engagements, tweet_to_user_engagements, all_feed_labels_dict)
    #print(u_id, time_stamp, record['text'], record['bias'], record['propaganda'], temporal_circles)
    citing_temporal_circles_network.update({record['id']: [time_stamp, u_id, record['text'], record['bias'], record['propaganda'], temporal_circles]})
temp_pkl_f = open('temporal_circles.pkl', 'wb')
pickle.dump(citing_temporal_circles_network, temp_pkl_f)
temp_pkl_f.close()
