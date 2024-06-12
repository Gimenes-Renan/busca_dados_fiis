import json
import requests
import re

def main():
    url = 'https://www.fundsexplorer.com.br/funds/abcp11'
    headers = {
        'User-Agent': 
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        x = re.findall("(\"meta\":)(.*)(?=,\"relateds\")", str(response.content))
        jsondata = json.loads(x[0][1]+"}")
        print(jsondata.get("codigo"))        
        print(jsondata.get("name"))        
        print(jsondata.get("valorpatrimonialcota"))
        print(jsondata.get("pvp"))
    return


main()