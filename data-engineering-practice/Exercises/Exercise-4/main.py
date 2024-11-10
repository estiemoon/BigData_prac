import os
import json
import pandas as pd

def json_to_csv(json_path):
    json_file_name = json_path.split("/")[-1]
    print(json_file_name)
    file_name = f"{json_file_name.split('.')[0]}.csv"
    
    with open(json_path,"r") as file:
        content = file.read()
        
        if not content.strip():
            print("파일이 비어있습니다")
        else:
            read_file = json.loads(content)
            df = pd.json_normalize(read_file)
            df.to_csv(f"./results/{file_name}")
    

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
    global json_files
    json_files = []
    
    if not (os.access("./results",os.F_OK)):
        os.mkdir("results")
    
    get_jsons("")

            

       
            
    
    #1 json파일을 찾아서 - > 폴더 구석구석 봐야해
    #2 csvf로 변환해서
    #3 그럴려면 flatten out some of the nested json strucutre
    
    
    
    
    pass


if __name__ == "__main__":
    main()
