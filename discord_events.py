import os
import json
import random
import string

class events:
    def list(PATH):
        event_list = {}
        for file in os.listdir(PATH):
            if file.endswith(".json"):
                json_file = open(PATH,file)
                loader = json.load(json_file)
                event_list[loader["uID"]]= { key:loader[key] for key in ["event_date","event_name","event_participants"]}
                json_file.close()
        return event_list
    
    def generate_event(PATH,event_date,event_name):
        event_data = {"event_name":event_name,"event_date":event_data,"event_participants":[]}
        uID = ""
        while True:
            uID = "".join(random.choice(string.ascii_letters) for i in range(8))
            if os.path.isfile(PATH,uID+".json") is False:
                break
        f = open(PATH,uID+".json")
        json.dump(event_data,f)
        f.close()
        return uID