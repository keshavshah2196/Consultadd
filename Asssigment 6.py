#Q1.

n=filter(lambda x:x%3!=0,filter(lambda x:x%7==0,range(25)))
print(list(n))

# Q2.
from functools import reduce
l=reduce(lambda x,y:x*y,list(map(lambda x:x,range(1,8))))
print(l)

#Q3.
h=[u for u in "ConSultaDd" if(u>=chr(65)) and u<=chr(90)]
print(h)

#Q4.

student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

dict(zip(student,capital))
print(dict(zip(student,capital)))
