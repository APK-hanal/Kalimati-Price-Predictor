import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import json
import os
def main():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = "https://ramropatro.com/vegetable"
    response = requests.get(url,headers= headers,timeout= 10)
    response.raise_for_status()

    return response.text
#web scrape :>
def parse(response):
    soup = BeautifulSoup(response, "html.parser")
    rows = []

    table = soup.find('table', id= 'commodityDailyPrice')
    if table:
        row = table.find_all("tr")
        rows = row
        # list of dicts
        data_list = []
        
        for element in rows[1:]:

            #indivisual dicts of all the headings
            data = {}
            cols = element.find_all("td")
            if not cols[0].text.strip():
                continue
            com = cols[0]
            unit = cols[1]
            min_value = cols[2]
            max_value = cols[3]
            avg = cols[4]
            data['Date'] = date.today().isoformat()
            data["Commodity"] = com.text
            data['Unit'] = unit.text
            data['Minimum value'] = min_value.text
            data['Maximum value'] = max_value.text
            data['Average'] = avg.text
            data_list.append(data)
    return data_list

file = 'record.json'
def save(dict_list):
    df = pd.DataFrame(dict_list)
    df.to_json(file, orient = 'records', indent = 2)
    
    
def update(dict_list):
    with open(file, 'r') as f:
        existing = json.load(f)
    Cdate = existing[-1]['Date']
    if Cdate == date.today().isoformat():
            print("alr Done with scraping for today")
            return
    else:        
            with open(file,'w') as f2:
                existing.extend(dict_list)
                json.dump(existing,f2, indent = 2,)
        
        


if __name__ == "__main__":
    res = main()
    dicts = parse(res)
    if os.path.exists(file):
        update(dicts)
    else:
        save(dicts)