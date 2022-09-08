#find the first most frequent character in a given string 
from collections import Counter

string = "successes"
print(string)
c = Counter(string)
print(c)
result = max(c, key=c.get)
print("most frequent character: ",result)
