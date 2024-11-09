import requests
import os
import urllib.request
import shutil

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def mk_dir():
    current_path = os.getcwd()
    if not (os.access(f"{current_path}/downloads",os.F_OK)):
        print("directory doesn't exist")
        os.mkdir(f'{current_path}/downloads')

        
def download(urls):
    path = f"{os.getcwd()}/downloads"
    
    for url in urls:
        file_name = url.split('/')[-1].split('.')[0]
        r = requests.get(url)
        with open(f"{file_name}","wb") as file:
            file.write(r.content)
        # urllib.request.urlretrieve(url, file_name)

        os.system("unzip "+file_name+" -d "+path)
        os.remove(file_name)
    shutil.rmtree("/Users/munseung-eun/Documents/PRAC/data1/data-engineering-practice/Exercises/Exercise-1/downloads/__MACOSX")
        
    
    
def main():
    # your code here
    mk_dir()
    download(download_uris)
    pass


if __name__ == "__main__":
    main()
