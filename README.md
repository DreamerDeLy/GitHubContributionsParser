# GitHub Contributions parser
![license](https://img.shields.io/github/license/DreamerDeLy/GitHubContributionsParser)

Simple contributions parser. A script that parses the contributions calendar on a GitHub profile page and provides data analysis.

## Features
- Parse text with the number of commits
- Parse data from calendar
- Display graphs
- Monthly / yearly forecast

## Arguments
Simple version (uses standart username): 
- `main.py [year]`

All:
- `-u [username]` username
- `-sy [year]` start year for analysis (2015)
- `-y [year]` base year (2020)
- `-s [path]` path to saving analytics to file

Example: `/main.py -u AlexGyver -sy 2010`

## Output:
```
> main.py 2020 ivankravets

Parsing user "ivankravets" (2020)

ANALYTICS
Commits per year:       581
---
Max commits per day:    60 (2020-02-12)
Longest streak:         13 (2020-02-23)
---
Days with commits:      79 (74.53%)
Days without commits:   27 (25.47%)
---
Commits per day:        5.48
Commits forecast:       2001
---
Commits per months:
Jan ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [123]
Feb ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [201]
Mar ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [208]
Apr ■■■■■■■■■■■□□□□□□□□□□□ [49]
May
Jun
Jul
Aug
Sep
Oct
Nov
Dec
---
Commits per weekdays:
Mon ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [80]
Tue ■■■■■■■■■■■■■■■■■■■ [49]
Wed ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [126]
Thu ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [120]
Fri ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [88]
Sat ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [94]
Sun ■■■■■■■■■ [24]
---
Commits per years:
2016 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [3447]
2017 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [2754]
2018 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [3046]
2019 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ [2460]
2020 ■■■■■■■■□□□□□□□□□□□□□□□□□□□□ [581]
---
```