import json
import csv

f = open('../../gen/data-preparation/temp/fortnite_astronomical_dataset/fortnite_allevent.json','r', encoding='utf-8')

con = f.readlines()

with open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding='utf-8') as outfile:
    g = csv.writer(outfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    g.writerow(['tweet_id', 'timestamp', 'text'])

    cnt = 0
    for line in con:
        if (len(line)<=5): continue

        cnt+=1
    
        obj = json.loads(line.replace('\n',''))
        id = obj.get('id_str').replace('\t',' ').replace('\n','')
        timestamp = obj.get('created_at').replace('\t',' ').replace('\n','')
        text = obj.get('text').replace('\t',' ').replace('\n','')

        g.writerow([id, timestamp, text]) 

        #if (cnt>1000): break

print('done.')
