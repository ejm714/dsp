## Q6
from collections import defaultdict

last_name = df['name'].str.split(' ').str[-1].tolist()
prof = df['title'].str.extract('(.*)(Professor)', expand=False)
df['prof']=prof[0] + prof[1]
df['degree']=df['degree'].str.strip()
fac_details=df[['degree', 'prof', 'email']].values.tolist()

faculty_dict = defaultdict(list)
for x, y in zip(last_name, fac_details):
    faculty_dict[x].append(y)


ffirstthree = {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}
print ffirstthree

## Q7
first_name = df['name'].str.split(' ').str[0].tolist()
name = zip(first_name, last_name)

professor_dict = defaultdict(list)
for x, y in zip(name, df.degree):
    professor_dict[x].append(y)

for x, y in zip(name, df.prof):
    professor_dict[x].append(y)

for x, y in zip(name, df.email):
    professor_dict[x].append(y)


pfirstthree = {k: professor_dict[k] for k in professor_dict.keys()[:3]}
print pfirstthree

# for k, v in professor_dict.iteritems():
#    print k, v

## Q8
professor_dict_sorted = sorted(professor_dict.items(), key=lambda x: x[0][1])
# print professor_dict_sorted[:3]

for k, v in professor_dict_sorted:
    print k, v
