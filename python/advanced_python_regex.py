## Q1
import pandas as pd
from collections import Counter

df = pd.read_csv('https://raw.githubusercontent.com/ejm714/dsp/master/python/faculty.csv')
print(df.columns.tolist())
df.columns = df.columns.str.strip()
degrees = df['degree'].str.strip().str.replace('.', '').str.split()
degree_counts = Counter(degrees.sum())
print degree_counts
len(degree_counts)


## Q2
title = df['title'].str.replace(' is ', ' of ')
title_counts = title.value_counts()
print title_counts
len(title_counts)

## Q3
emails = df['email'].tolist()
print emails
txt_file = open('q3.txt', 'w')
txt_file.write('%s' % emails)
txt_file.close()
