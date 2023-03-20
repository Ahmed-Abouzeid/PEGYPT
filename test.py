import pickle, json
import matplotlib.pyplot as plt
import numpy as np

X = ["A", "B", "C", "E", "F"]
X_axis = np.arange(len(X))
fig, ax = plt.subplots()
ax.bar(X_axis - 0.15, [0.076, 0.051, 0.354, 0.046, 0.363], width=.3, color = "red", label="Fairness")
ax.bar(X_axis + 0.15, [0.066, 0.059, 0.333, 0.825, 0.345], width=.3, color = "royalblue", label= "Social Acceptance + Fairness")

ax.set_xlabel("Social Circles")
ax.set_ylabel("High Incentives Spending (%)")
#ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
ax.set_xticks(X_axis, X)
ax.legend()
plt.show()

X = ["A", "B", "C", "E", "F"]
X_axis = np.arange(len(X))
fig, ax = plt.subplots()
ax.bar(X_axis - 0.15, [0.474, 0.549, 0.045, 0.586, 0.034], width=.3, color="red", label="Fairness")
ax.bar(X_axis + 0.15, [0.465, 0.498, 0.065, 0.514, 0.054], width=.3, color="royalblue",
        label="Social Acceptance + Fairness")

ax.set_xlabel("Social Circles")
ax.set_ylabel("Low Incentives Spending (%)")
#ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
ax.legend()
ax.set_xticks(X_axis, X)

plt.show()
# u_ids_f= open('all_users_ids.pkl', 'rb')
# ids = pickle.load(u_ids_f)
# u_ids_f.close()
# t_ids_file = open('all_tweets_ids.pkl', 'rb')
# t_ids = pickle.load(t_ids_file)
# t_ids_file.close()
# s_ids = sorted([int(i) for i in ids])
# user_1 = s_ids[228]
# user_2 = s_ids[5057]
#
# print(user_1, user_2)
#
# lines_f = open('twitter_feed.jsonl', 'r')
# jsn = [json.loads(line) for line in lines_f]
# lines_f.close()
# tws = []
# matched = set()
# for feed in jsn:
#     for tw in feed['data']:
#         if tw['id'] in t_ids:
#             if tw['author_id'] in [str(user_1), str(user_2)] and tw['id'] not in matched:
#                 tws.append(tw)
#                 matched.add(tw['id'])
#                 if tw['public_metrics']['like_count'] > 0:# and tw['id'] not in ["978747024203046913", "978739760591228928", "978746928153415680", "978725853503901699", "978746040609275905", "978683569374507008"]:
#                     print('to check likes:', tw)
#
#
# for tw in tws:
#     if tw['author_id'] == str(user_1) or tw['author_id'] == str(user_2):
#         if 'referenced_tweets' in tw.keys():
#             for ref in tw['referenced_tweets']:
#                 for tw_ in tws:
#                     if (ref['id'] == tw_['id'] and tw_['author_id'] == str(user_2)) or (ref['id'] == tw_['id'] and tw_['author_id'] == str(user_1)):
#                         print('ref1', tw)
#                         print('ref2', tw_)
#                         print('----------------')
#
#         if 'entities' in tw.keys():
#             for e in tw['entities']:
#                 if e == 'mentions':
#                     for m in tw['entities'][e]:
#                         if m['id'] in  [str(user_1), str(user_2)]:
#                             print('men', tw)
#                             print('-----------------------------')
#
#


# mtrx_file = open('adjacency_mtrx.pkl', 'rb')
# mtrx = pickle.load(mtrx_file)
# mtrx_file.close()


# for e, row in enumerate(mtrx):
#     for e_c, c in enumerate(row):
#         if mtrx[e][e_c] != 0 and ((e == 559 and e_c == 6933) or (e == 6933 and e_c == 559)) :
#             print((e, e_c, mtrx[e][e_c]))


