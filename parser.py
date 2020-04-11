from bs4 import BeautifulSoup
import requests as req

resp = req.get("https://github.com/DreamerDeLy?tab=overview&from=2020-01-01&to=2020-12-01")
 
soup = BeautifulSoup(resp.text, 'lxml')
 
#print(soup.title)
print("read page: \"" + soup.title.text + "\"")

text = soup.find('h2', 'f4 text-normal mb-2').text.strip()

print("text of block: \"" + text + "\"")

commits = int(text.split()[0])

print("number: \"" + str(commits) + "\"")

from datetime import date
d0 = date(2020, 1, 1)
d1 = date.today()
day_number_1 = d1 - d0
day_number = day_number_1.days

commits_per_day = commits / day_number
commits_year_forecast = commits_per_day * 365

print("\nAnalitics")
print("Commits per day: \t" + str(round(commits_per_day, 2)))
print("Commits forecast: \t" + str(round(commits_year_forecast)))

