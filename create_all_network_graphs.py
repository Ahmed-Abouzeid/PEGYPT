import pickle
import collections

data_f = open('final_labeled_dataset.pkl', 'rb')
data = pickle.load(data_f)

adj_f = open('final_symmetric_mtrx.pkl', 'rb')
adj = pickle.load(adj_f)


users_f = open('sorted_all_users_ids.pkl', 'rb')
users = pickle.load(users_f)

users_propaganda = set()
users_non_propaganda = set()

users_bias_for = set()
users_bias_against = set()
users_neutral_bias = set()


def classify_user(bias, is_propaganda, id):

    if is_propaganda == 0:
        users_non_propaganda.add(id)
    if is_propaganda == 1:
        users_propaganda.add(id)
    if bias == 1:
        users_bias_for.add(id)
    if bias == -1:
        users_bias_against.add(id)
    if bias == 0:
        users_neutral_bias.add(id)


def create_colored_graphs():

    node_bias = open('./graphs/bias_nodes.csv', 'a')
    edge_bias = open('./graphs/bias_edges.csv', 'a')
    node_propaganda = open('./graphs/propaganda_nodes.csv', 'a')
    edge_propaganda = open('./graphs/propaganda_edges.csv', 'a')

    node_bias.write('id, node_color' + '\n')

    edge_bias.write('source, target' + '\n')

    node_propaganda.write('id, node_color' + '\n')
    edge_propaganda.write('source, target' + '\n')

    for e, user_id in enumerate(users):

        if str(user_id) in users_bias_for and str(user_id) not in users_bias_against and str(user_id)  not in users_neutral_bias:
            node_bias.write(str(user_id) + ', FOR' + '\n')
            for index, entry in enumerate(adj[e]):
                if entry > 0:
                    edge_bias.write(str(user_id) + ', ' + str(users[index])+ '\n')
        elif str(user_id) in users_bias_against and str(user_id)  not in users_bias_for and str(user_id)  not in users_neutral_bias:
            node_bias.write(str(user_id) + ', AGAINST' + '\n')
            for index, entry in enumerate(adj[e]):
                if entry > 0:
                    edge_bias.write(str(user_id) + ', ' + str(users[index]) + '\n')
        elif str(user_id) in users_neutral_bias and str(user_id)  not in users_bias_for and str(user_id)  not in users_bias_against:
            node_bias.write(str(user_id) + ', NEUTRAL' + '\n')
            for index, entry in enumerate(adj[e]):
                if entry > 0:
                    edge_bias.write(str(user_id) + ', ' + str(users[index]) + '\n')
        else:
            node_bias.write(str(user_id) + ', DIVERSE' + '\n')
            for index, entry in enumerate(adj[e]):
                if entry > 0:
                    edge_bias.write(str(user_id) + ', ' + str(users[index]) + '\n')

        if str(user_id) in users_propaganda and str(user_id) not in users_non_propaganda:
            node_propaganda.write(str(user_id) + ', PROPAGANDA' + '\n')
            for index, entry in enumerate(adj[e]):
                if entry > 0:
                    edge_propaganda.write(str(user_id) + ', ' + str(users[index]) + '\n')
        elif str(user_id) in users_non_propaganda and str(user_id) not in users_propaganda:
            node_propaganda.write(str(user_id) + ', NON_PROPAGANDA' + '\n')
            for index, entry in enumerate(adj[e]):
                if entry > 0:
                    edge_propaganda.write(str(user_id) + ', ' + str(users[index]) + '\n')
        else:
            node_propaganda.write(str(user_id) + ', DIVERSE' + '\n')
            for index, entry in enumerate(adj[e]):
                if entry > 0:
                    edge_propaganda.write(str(user_id) + ', ' + str(users[index]) + '\n')

    node_propaganda.close()
    edge_bias.close()
    node_bias.close()
    edge_propaganda.close()


for row in data:
    classify_user(row['tweet_bias_label'], row['tweet_is_propaganda_label'], row['tweet_user_id'])

create_colored_graphs()
