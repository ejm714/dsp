# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'  

from datetime import datetime  

start_date = datetime.strptime(date_start, "%m-%d-%Y")  
end_date = datetime.strptime(date_stop, "%m-%d-%Y")  
delta = (end_date - start_date).days  
print delta  

####b)  
date_start = '12312013'  
date_stop = '05282015'  

start_date = datetime.fromtimestamp(float(date_start))  
end_date = datetime.fromtimestamp(float(date_stop))  
delta = (end_date - start_date).days  
print abs(delta)  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

start_date = datetime.strptime(date_start, "%d-%b-%Y")  
end_date = datetime.strptime(date_stop, "%d-%b-%Y")  
delta = (end_date - start_date).days  
print delta  
