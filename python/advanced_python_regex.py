## Q1
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/ejm714/dsp/master/python/faculty.csv')
print(df.columns.tolist())
df.columns = df.columns.str.strip()
degrees = df['degree'].str.strip().str.replace('.', '')
degree_counts = Counter((',').join(degrees).replace(' ', ',').split(','))
print degree_counts
len(degree_counts)


## Q2
title = df['title'].str.replace(' is ', ' of ')
title_counts = title.value_counts()
print title_counts
len(title_counts)
