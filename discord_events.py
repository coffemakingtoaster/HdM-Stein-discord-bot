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
                print(os.path.isfile(os.path.join(PATH,file)))
                json_file = open(os.path.join(PATH,file),"r")
                loader = json.load(json_file)
                print(loader)
                event_list[loader["uID"]]= { key:loader[key] for key in ["event_date","event_name","event_participants"]}
                json_file.close()
        return event_list
    
    def generate_event(PATH,event_name,event_date,id):
        while True:
            uID = "".join(random.choice(string.ascii_letters) for i in range(8))+".json"
            new_path = os.path.join(PATH,uID)
            if os.path.isfile(PATH+"/"+uID+".json") is False:
                break
        event_data = {}   
        event_data["event_name"] = event_name
        event_data["event_date"] = event_date
        event_data["event_participants"] = []
        event_data["uID"] = str(uID[:8])
        event_data["creator"] = id
        f = open(new_path,"w")
        json.dump(event_data,f)
        f.close()
        return uID[:8]
    
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
                    
                    
    def alter_description(PATH,new_description,event_id,creator):
        filepath = os.path.join(PATH,event_id+".json")
        print(os.path.isfile(filepath))
        try:
            f = open(filepath,"r")
        except:
            raise ("Invalid ID: Eventfile not found!")
        json_data = json.load(f)
        if json_data["creator"] != creator:
            f.close()
            return 1
        json_data["description"] = new_description
        f.close()
        f = open(filepath,"w")
        json.dump(json_data,f)
        f.close()
        return 0
    
    
    def add_participant(PATH,new_participant,event_id):
        try:
            f = open(os.path.join(PATH,event_id+".json"),"r+")
        except:
            raise "Invalid Event ID: Event file not found!"
        json_data = json.load(f)
        json_data["event_participants"].append(new_participant)
        f.truncate(0)
        json.dumps(json_data,f)
        f.close()
        return
            
                    