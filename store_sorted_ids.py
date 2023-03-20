import pickle

u_ids_f= open('all_users_ids.pkl', 'rb')
ids = pickle.load(u_ids_f)
u_ids_f.close()

s_ids_file = open("sorted_all_users_ids.pkl", "wb")
s_ids = sorted([int(i) for i in ids])

pickle.dump(s_ids, s_ids_file)
s_ids_file.close()
