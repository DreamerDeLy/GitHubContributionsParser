# GitHub Contributions parser by DreamerDeLy

from bs4 import BeautifulSoup
import requests as req
import sys

from datetime import date, datetime

username = "DreamerDeLy"
year = "2020"

if (len(sys.argv) > 1): 
	year = sys.argv[1]

if (len(sys.argv) > 2): 
	username = sys.argv[2]

resp = req.get("https://github.com/" + username + "?tab=overview&from="+year+"-01-01&to="+year+"-12-31")
soup = BeautifulSoup(resp.text, 'lxml')

print("read page: \"" + soup.title.text + "\"")

text = soup.find('h2', 'f4 text-normal mb-2').text.strip()
commits = int(text.split()[0])

# ------------------------------------------------------------------------------

day_number = 0

d0 = date(int(year), 1, 1)
today = date.today()

if (today.year != int(year)):
	day_number = 365
else:
	day_number_1 = today - d0
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

days_with_commits = 0

for i in range(len(dates)):
	commits_ = int(counts[i]) 

	if commits_ > 0:
		days_with_commits = days_with_commits + 1

days_without_commits = day_number - days_with_commits

# ------------------------------------------------------------------------------

def createGraph(values, labels, max_value, forecast_value, forecast_index):
	graph_str = ""

	graph_p = 50

	values_percent = list(values)

	for i in range(len(values)):
		values_percent[i] = values[i] / max_value

	forecast_percent = forecast_value / max_value


	for i in range(len(values)):
		graph_str += "" + labels[i] + " "

		for x in range(int(values_percent[i]*graph_p)):
			graph_str += "■"

		if ((i == forecast_index) & (forecast_value > 0)):
			for x in range(int((forecast_percent - values_percent[i])*graph_p)):
				graph_str += "□"

		if values[i] > 0:
			graph_str += " [" + str(round(values[i], 2)) + "]"
		graph_str += "\n"

	graph_str = graph_str[0:-1]
	return graph_str

# ------------------------------------------------------------------------------

months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(dates)):
	dt = datetime.strptime(dates[i], '%Y-%m-%d')
	m = dt.month
	months[m-1] += int(counts[i])

months_max = 0

for m in months:
	if m > months_max: 
		months_max = m

# ------------------------------------------------------------------------------

month_start = date(today.year, today.month, 1)
month_day_number = (today - month_start).days + 1
month_forecast = (months[int(today.month-1)]/month_day_number)*30

# ------------------------------------------------------------------------------

months_name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

months_max_graph = months_max
if (month_forecast > months_max_graph) & (int(year) == today.year):
	months_max_graph = month_forecast

mf = 0
if (int(year) == today.year):
	mf = month_forecast

mounts_percent_string = createGraph(months, months_name, months_max_graph, mf, int(today.month - 1))

# ------------------------------------------------------------------------------

weekdays = [0, 0, 0, 0, 0, 0, 0]
weekdays_name = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "НД"]

for i in range(len(dates)):
	dt = datetime.strptime(dates[i], '%Y-%m-%d')
	wd = dt.weekday() 
	weekdays[wd] += int(counts[i])

weekday_max = 0

for w in weekdays:
	if (w > weekday_max): 
		weekday_max = w

weekdays_percent_string = createGraph(weekdays, weekdays_name, weekday_max, 0, 0)

# ------------------------------------------------------------------------------

print("\nANALITYCS")
print("Commits per year: \t"+str(commits))
print("---")
print("Max commits per day: \t{0} ({1})".format(commits_max, commits_max_day))
print("Longest streak: \t{0} ({1})".format(longest_streak, longest_streak_date))
print("---")
print("Days with commits: \t{0} ({1}%)".format(days_with_commits, round((days_with_commits/day_number)*100, 2)))
print("Days without commits: \t{0} ({1}%)".format(days_without_commits, round((days_without_commits/day_number)*100, 2)))
print("---")
print("Commits per day: \t" + str(round(commits_per_day, 2)))
print("Commits forecast: \t" + str(round(commits_year_forecast)))
print("---")
print("Commits per months:")
print(mounts_percent_string)
print("---")
print("Commits per weekdays:")
print(weekdays_percent_string)
print("---")
print("\n")

