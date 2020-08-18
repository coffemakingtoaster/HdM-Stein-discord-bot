import os
import json
import random
import string
from datetime import datetime
import glob

class events:
    def list(PATH):
        event_list = {}
        for file in os.listdir(PATH):
            if file.endswith(".json"):
                json_file = open(os.path.join(PATH,file))
                loader = json.load(json_file)
                print(loader)
                event_list[loader["uID"]]= { key:loader[key] for key in ["event_date","event_name","event_participants"]}
                json_file.close()
        return event_list
    
    def generate_event(PATH,event_name,event_date):
        while True:
            uID = "".join(random.choice(string.ascii_letters) for i in range(8))+".json"
            new_path = os.path.join(PATH,uID)
            if os.path.isfile(PATH+"/"+uID+".json") is False:
                break
        event_data = {"event_name":event_name,"event_date":event_date,"event_participants":[],"uID":uID}   
        f = open(new_path,"w+")
        json.dump(event_data,f)
        f.close()
        return uID
    
    def garbage_collect(PATH):
        curr_day,curr_month,curr_year = datetime.now().strftime('%d/%m/%Y').split("/")
        cnt = 0
        to_remove = []
        os.chdir(PATH)
        for file in glob.glob("*.json"):
            print(file)
            json_file = open(os.path.join(PATH,file))
            loader = json.load(json_file)
            event_time = str(loader["event_date"])
            print(event_time)
            day,month,year =event_time[0:event_time.find(":")].split("/")
            print(f'{day},{month},{year}')
            if int(curr_year)>int(year):
                cnt+=1
                to_remove.append(file)
            elif int(curr_month)>int(month):
                cnt+=1
                to_remove.append(file)
            elif int(curr_day)>int(day):
                print("found outdated file")
                cnt+=1
                to_remove.append(file)
        return to_remove
                    