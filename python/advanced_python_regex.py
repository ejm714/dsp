# Q1
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/ejm714/dsp/master/python/faculty.csv')
print(df.columns.tolist())
df.columns = df.columns.str.strip()
degrees = df['degree'].str.strip().str.replace('.', '')
counts = Counter((',').join(degrees).replace(' ', ',').split(','))
len(counts)
