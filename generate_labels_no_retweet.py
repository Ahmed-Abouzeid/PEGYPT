import pandas as pd
import json
import time
import pickle


jsn = [json.loads(line) for line in open('twitter_feed.jsonl', 'r')]
texts = {}
for feed in jsn:
    for tw in feed['data']:
        texts.update({tw['id']: tw['text']})


df = pd.read_excel("annotated_propaganda_final.xlsx", usecols=["index", "id", "text", "polarization", "propaganda"])
matched_already = set()
l = len(texts.keys())
c = 0
labels = []
for id, text in texts.items():
    c += 1
    print(c, ' out of ', l)
    for e, txt in enumerate(df['text']):
        if text == txt:
            if id not in matched_already:
                labels.append({'id': id, 'text': text, 'bias':df['polarization'][e], 'propaganda': df['propaganda'][e] })
                matched_already.add(id)

labels_file = open('labels_no_retweet.pkl', 'wb')
pickle.dump(labels, labels_file)

print('Matched : ', len(labels))
#print('Matched by Text: ', y)
print('---------------------------')
labels_file.close()

