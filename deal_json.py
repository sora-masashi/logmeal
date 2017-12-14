import json

def load(file):
    try:
        json_file = open(file,"r")
        json_list = json.load(json_file)
        json_file.close()
    except:
        json_list = []
    return json_list

def awrite(data,file):
    #load json_file
    try:
        json_file = open(file,"r")
        json_list = json.load(json_file)
        json_file.close()
    except:
    #if file not exist
        json_list = []

    #write json_file
    json_file = open(file,"w")
    json_list.append(data)
    json.dump(json_list,json_file)
    json_file.close()
