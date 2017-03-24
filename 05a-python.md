# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both contain a list of values and values can be referenced by an index (ex. months[0]). Lists are written in square brackets and tuples in parentheses. The main difference is that tuples are immutable while lists are mutable. This means that you cannot change (add, delete, sort, etc.) the values in a tuple. Because they are immutable, tuples can be used as keys in dictionaries but lists cannot.  

>> To be used as a dictionary key, an object must be hashable – meaning that its hash value never changes during its lifetime. Hash values are used to quickly compare dictionary keys during a look up.


---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets both contain a sequence of values. Lists are ordered and can contain duplicates while sets are unordered and require unique values.

>> Because lists are ordered, they support indexing and slicing. They are also faster for iterating over a collection of values.

>> Since sets do not support indexing (as they are unordered), they use a hash lookup. This makes sets faster than lists in determining if an object is present in the set. Sets are also often used for operations like intersection, union, and difference.

```python
# Intersection and membership testing in sets
healthy_food = {'brocolli', 'spinach', 'quinoa', 'green beans'}
food_i_like = {'cheese', 'green beans', 'peanut butter'}
liked_healthy = healthy_food & food_i_like
'quinoa' in food_i_like

# Indexing and slicing of lists
classes = ['english', 'chemistry', 'gym', 'lunch', 'seminar', 'band']
classes[:3]
classes[4]

# Iterating over a list
elements = []
for i in range(0, 4):
    elements.append(i)
```

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambdas are used to create anonymous functions (i.e. unnamed) and do not include a return statement. This is useful when a function is rather simple and is only used once, and thus can be written directly where it’s going to be used. Lambda can be used in functions that take a callable object as a parameter. 

>> For example, lambda is useful in sorting tuples by an object's index.
```python
colleagues_offices = [('emily', 303), ('jessica', 310), ('harold', 305)]
sorted(colleagues_offices, key=lambda tup: tup[1])
```


---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are an elegant way to create and define lists. It works as a substitute for map or filter with a lambda function. List comprehensions are faster than for loops, but differences between list comprehensions and map/filter seem marginal. In terms of ‘pythonic’ style, list comprehensions are preferred as they are typically easier to read.

```python
# Map applies a function to all the items in the input. This can be done with list comprehensions.

days = ['Monday', 'Tuesday', 'Wednesday', 'thursday', 'Friday']

def all_caps_lc(l):
    return [w.upper() for w in l]

def all_caps_map(l):
    return map(lambda x: x.upper(), days)

# Filter creates a list of elements for which a function returns true. This can be done with list comprehensions as well.

numbers = [1, 3, 5, 2, 6, 12]

def odds_only_lc(l):
    return [n for n in l if n % 2 != 0]

def odds_only_filter(l):
    return filter(lambda x: x % 2 != 0, l)

# Set and dictionary comprehensions work as well

s = {x*x for x in range(5)}

d = {x: x+y for x in range(4) for y in range(4) }
```


---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 82 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





