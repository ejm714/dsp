# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# A few different ways to do this (not sure which one is best):

# Create a dictionary
import csv
import urllib2
data = urllib2.urlopen('https://raw.githubusercontent.com/ejm714/dsp/master/python/football.csv')
reader = csv.DictReader(data)
dict = {}
for row in reader:
    dict[row['Team']] = [abs(int(row['Goals'])- int(row['Goals Allowed']))]

print min(dict, key=dict.get)

# DictReader v2
import csv
import urllib2
data = urllib2.urlopen('https://raw.githubusercontent.com/ejm714/dsp/master/python/football.csv')
reader = csv.DictReader(data)
min_diff = None
for row in reader:
    diff = abs(int(row['Goals'])-int(row['Goals Allowed']))
    if min_diff == None or min_diff > diff:
        min_diff = diff
        team = row['Team']

print team

# Use pandas
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/ejm714/dsp/master/python/football.csv')
df['diff'] = abs(df['Goals'] - df['Goals Allowed'])
df = df.set_index(['Team'])
df['diff'].idxmin()
