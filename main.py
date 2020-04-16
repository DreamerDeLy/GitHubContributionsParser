# GitHub Contributions parser by DreamerDeLy

from parse import *
import codecs

import sys

from datetime import date, datetime

username = "DreamerDeLy"
year = "2020"

result_file = ""

year_range_start = 2015
year_range_end = int(year)

# ------------------------------------------------------------------------------

if len(sys.argv) == 2: 
	year = sys.argv[1]

if (len(sys.argv) > 2): 
	for i in range(len(sys.argv)):
		a = sys.argv[i]

		if a == "-y":
			year = sys.argv[i+1]
			year_range_end = int(year)
			i += 1

		if a == "-u":
			username = sys.argv[i+1]
			i += 1
		
		if a == "-sy":
			year_range_start = int(sys.argv[i+1])
			i += 1

		if a == "-s":
			result_file = sys.argv[i+1]
			i += 1

# ------------------------------------------------------------------------------

print("Parsing user \"{0}\" ({1}-{2})".format(username, year_range_start, year))

commits = parseSimpleYear(username, year)
parseFullYear(username, year)

# ------------------------------------------------------------------------------

day_number = 0

d0 = date(int(year), 1, 1)
today = date.today()

if (today.year != int(year)):
	day_number = 365
else:
	day_number_1 = today - d0
	day_number = day_number_1.days + 1

commits_per_day = commits / day_number
commits_year_forecast = commits_per_day * 365

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
		graph_str += "" + str(labels[i]) + " "

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
weekdays_name = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

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

years = []
years_name = []
years_max = 0

for y in range(year_range_start, year_range_end+1):
	i = y - year_range_start

	commits_year = parseSimpleYear(username, y) 
	years.append(commits_year)
	years_name.append(str(y))

	if commits_year > years_max:
		years_max = commits_year

if commits_year_forecast > years_max:
	years_max = commits_year_forecast

years_percent_string = ""

if (int(year) == today.year):
	years_percent_string = createGraph(years, years_name, years_max, commits_year_forecast, len(years)-1)
else:
	years_percent_string = createGraph(years, years_name, years_max, 0, 0)

# ------------------------------------------------------------------------------

result_string = "ANALYTICS\n"
result_string += "Commits per year: \t{0} \n".format(commits)
result_string += "---\n"
result_string += "Max commits per day: \t{0} ({1}) \n".format(commits_max, commits_max_day)
result_string += "Longest streak: \t{0} ({1}) \n".format(longest_streak, longest_streak_date)
result_string += "---\n"
result_string += "Days with commits: \t{0} ({1}%) \n".format(days_with_commits, round((days_with_commits/day_number)*100, 2))
result_string += "Days without commits: \t{0} ({1}%) \n".format(days_without_commits, round((days_without_commits/day_number)*100, 2))
result_string += "---\n"
result_string += "Commits per day: \t" + str(round(commits_per_day, 2)) + "\n"
result_string += "Commits forecast: \t" + str(round(commits_year_forecast)) + "\n"
result_string += "---\n"
result_string += "Commits per months:\n"
result_string += mounts_percent_string + "\n"
result_string += "---\n"
result_string += "Commits per weekdays:\n"
result_string += weekdays_percent_string + "\n"
result_string += "---\n"
result_string += "Commits per years:"
result_string += years_percent_string + "\n"
result_string += "---\n"

print("\n")
print(result_string)

if result_file != "":
	with open(result_file, "w", encoding="utf-8") as file:
		file.write("GitHub Contribution Parser by DeLy\n")
		file.write("User: {0}\nRange: {1}-{2}\n".format(username, year_range_start, year))
		file.write("Date: {0}\n\n".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")))
		file.write(str(result_string))