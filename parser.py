# GitHub Contributions parser by DreamerDeLy

from bs4 import BeautifulSoup
import requests as req

username = "DreamerDeLy"

resp = req.get("https://github.com/" + username + "?tab=overview&from=2020-01-01&to=2020-12-31")
soup = BeautifulSoup(resp.text, 'lxml')

print("read page: \"" + soup.title.text + "\"")

text = soup.find('h2', 'f4 text-normal mb-2').text.strip()
commits = int(text.split()[0])

# ------------------------------------------------------------------------------

from datetime import date
d0 = date(2020, 1, 1)
d1 = date.today()
day_number_1 = d1 - d0
day_number = day_number_1.days

commits_per_day = commits / day_number
commits_year_forecast = commits_per_day * 365

# ------------------------------------------------------------------------------ 

text_calendar = "" 
add_text = "0"

dates = []
counts = []

for tag in soup.find_all("rect", "day"):
	#print("Date: {0}, Count: {1}".format(tag["data-date"], tag["data-count"]))
	dates.append(tag["data-date"])
	counts.append(tag["data-count"])

#for i in range(len(dates)):
#	print("Date: {0}, Count: {1}".format(dates[i], counts[i]))

# ------------------------------------------------------------------------------

commits_max = 0
commits_max_day = ""

for i in range(len(dates)):
	commits_ = int(counts[i]) 

	if (commits_ > commits_max):
		commits_max = commits_
		commits_max_day = dates[i]

# ------------------------------------------------------------------------------

current_streak = 0
longest_streak = 0
longest_streak_date = ""

for i in range(len(dates)):
	commits_ = int(counts[i]) 

	if commits_ > 0:
		current_streak = current_streak + 1
	else:
		if current_streak > longest_streak:
			#print("st:"+str(current_streak))
			#print("dt:"+str(dates[i]))
			longest_streak = current_streak
			longest_streak_date = str(dates[i])
			current_streak = 0
		current_streak = 0



# ------------------------------------------------------------------------------

print("\nANALITICS")
print("Commits per year: \t"+str(commits))
print("---")
print("Max commits per day: \t{0} ({1})".format(commits_max, commits_max_day))
print("Longest streak: \t{0} ({1})".format(str(longest_streak), str(longest_streak_date)))
print("---")
print("Commits per day: \t" + str(round(commits_per_day, 2)))
print("Commits forecast: \t" + str(round(commits_year_forecast)))
print("\n")

