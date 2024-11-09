import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

def get_file():
    file_path=""
    res = requests.get("https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/")

    if res.status_code == 200:
        html = res.content
        soup = BeautifulSoup(html,'html.parser')
    
    lists = soup.select("tr")[4:]
    for li in lists:
        if len(li.select("td")) == 0:
            continue
        if li.select("td")[1].text.strip() == "2024-01-19 10:27":
            file_path = li.select("td a")[0].attrs["href"]
            break

    
    return file_path

def load_file(path):
    base_url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    
    res = requests.get(f"{base_url}/{path}")
    if res.status_code == 200:
        with open(f"weather.csv", "wb") as file:
            file.write(res.content)

def process_data():
    df = pd.read_csv("weather.csv")
    
    print(df["HourlyDryBulbTemperature"].max())

def main():
    current_path = os.getcwd()
    if not (os.path.exists(f"{current_path}/weather.csv")):
        file_path = get_file()
        load_file(file_path)
        
    process_data()
    
    
    pass


if __name__ == "__main__":
    main()
