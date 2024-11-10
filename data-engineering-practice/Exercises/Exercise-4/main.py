import os
import json
import csv
import pandas as pd


def flatten(data,key,curr_row):
    if type(data) == dict:
        for obj in data:
            flatten(data[obj],f"{key}.{obj}",curr_row)
    else:
        if not key in headers:
            headers.append(key)
        curr_row.append(data)
    
    
def json_to_csv(json_path):   
    with open(json_path,"r") as file:
        content = file.read()
        
        if not content.strip():
            print("파일이 비어있습니다")
        else:
            read_file = json.loads(content)
            # df = pd.json_normalize(read_file)
            # df.to_csv(f"./results/{file_name}")
                
            with open(f"results.csv", "a") as ouput_file, open(f"results.csv", "r") as check_file:
                
                f = csv.writer(ouput_file)
                
                curr_row = []
                for obj in read_file:
                    flatten(read_file[obj],obj,curr_row)


                if not any(csv.reader(check_file)):
                    print("첫번째 파일")
                    f.writerow(headers) 
                    
                f.writerow(curr_row)
                    
            

def get_jsons(path):
    files = os.listdir(f"./{path}")
    for f in files:
        if os.path.isdir(f"./{path}/{f}"):
            get_jsons(f"{path}/{f}")
        else:
            if f.split(".")[-1] =="json":
                # json to csv
                json_files.append(f)
                json_to_csv(f".{path}/{f}")
    

def main():
    global json_files, headers
    json_files = []
    headers = []
    
    with open("results.csv", "w") as output:
        f = csv.writer(output)
    
    get_jsons("")    
    
    pass


if __name__ == "__main__":
    main()
