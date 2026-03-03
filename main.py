import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
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
file = 'record.csv'
def save(dict_list):
    if os.path.exists(file):
        existing = pd.read_csv(file)
        if existing['Date'].iloc[-1] == date.today().isoformat():
            print("alr done with scraping today, come back tmr")
            return
    
    df = pd.DataFrame(dict_list)
    df.to_csv(file, mode='a', header=not os.path.exists(file), index=False)
    print("Successfully scraped")
            
    
    
 
                


if __name__ == "__main__":
    res = main()
    dicts = parse(res)
    save(dicts)