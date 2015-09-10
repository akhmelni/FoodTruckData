import json
import unicodedata
import pythonYelpAPI
import threading

def asyncYelp(name, location, index):
    restaurant = data[index]
    ret = pythonYelpAPI.query_api(name, location)
    if ret:
        if ret.get("phone"):
            restaurant["phone"] = ret["phone"]
        if ret["name"]!=restaurant["name"]:
            restaurant["yelpName"] = ret["name"]
    else:
        restaurant["phone"] = ""

with open('./parseOut.json') as data_file:    
    data = json.load(data_file)

i = 0

threads = []
for restaurant in data:
    name =  unicodedata.normalize('NFKD', restaurant["name"]).encode('ascii','ignore')
    t = threading.Thread(target=asyncYelp, args=(name, "Los Angeles", i,))
    threads.append(t)
    t.start()
    i+=1

[t.join() for t in threads]
with open('parsedWithPhone4.json', 'w') as outfile:
    json.dump(data, outfile)
