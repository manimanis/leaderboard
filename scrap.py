# import libraries
from bs4 import BeautifulSoup
import urllib.request
import os
import pprint
import json

url = 'http://community.andela.com/index.php/leadership-board/'
htmlfile = 'leaderboard.html'
jsonfile = 'leaderboard.json'

if not os.path.exists(htmlfile):
    urllib.request.urlretrieve(url, htmlfile)

page = urllib.request.urlopen(f"file:///{os.path.abspath(htmlfile)}")
soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table', attrs={'id': 'table_1'})
results = table.find_all('tr')

cols_names = [col.text for col in results[0].find_all('th')]

learners_data = []
for row in results[1:]:
    drow = {}
    for idx, col in enumerate(row.find_all('td')):
        drow[cols_names[idx]] = col.text
    learners_data.append(drow)

with open(jsonfile, 'w') as f:
    f.write(json.dumps(learners_data))
