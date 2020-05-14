

#Q1.
print("Q1")
def rev_str(strl):
    rstr=" "
    l=len(strl)
    while(l>0):
        rstr+=strl[l-1]
        l-=1
    return rstr
    print("Original String",strl)
    print("Reverse string",rstr)
print(rev_str("I am Keshav"))
        
#Q2.
print("-----")
print("Q2")
def countUpperLower(st):
    count_upper=0
    count_lower=0
    for i in st:
        if(i.isalpha()):
            if(i.isupper()):
                count_upper+=1
                print(i,"is capital letter")
            elif(i.islower()):
                count_lower+=1
                print(i,"is a small lettr")
    return count_upper,count_lower
    print("Lower case ciunt:=",count_lower)
    print("Upper case count:=",count_upper)
    
print(countUpperLower("Hello!! Welcome2PythonTraining"))

#Q3.
print("-----")
print("Q3")
def uniqu_list(av):
    print("Original list",av)
    c=set(av)
    print("New list:= ",c)
    return c

print(uniqu_list([12,76,54.6,9/35,"hello","asc","asc",34,6+7j]))


#Q4. Doubt in example wit hyphen

#Q5.
print("---")
print("Q5")
def low2upp(stri):
    l=len(stri)
    up=""
    for i in range(l):
        if(stri[i].islower()):
            p=stri[i].upper()
            up+=p
        else:
            up+=stri[i]
    print("New string",up)
    return up
print(low2upp("Hello Welcome"))

#Q6.
print("--")
print("Q6")
def rks(a,b):
    a=input("enter value for input 1")
    b=input("Enter input 2")
    print("result adter addig two strings is")
    return a + b
print(rks("rth","j"))
#Q7.
print("-------")
print("Q7")
def comp2(str1,str3):
    le1=len(str1)
    le2=len(str3)
    print("String 1=",str1,"String 2=",str3)
    if(le1>le2):
        return le1,str1
    elif(le1<le2):
        return le2,str3
    elif(le1==le2):
        print("Equal sizes")
        return 1
print(comp2("Lucky","Height"))
#Q8
print("-----")
print("Q8")
def squ(r,k):
    a=[]
    if(r<=k):
        for i in range(r,k):
            a.append(i*i)
    elif(r>k):
        for j in range(k,r):
            append(j*j)
    print("Ol list:-",a)
    print("New List:=",tuple(a))
    return a,tuple(a)
print(squ(5,34))
print(squ(1,21))

#Q9
print("-----")
print("Q9")
def n(p):
    p=int(input("Enter the value of last number"))
    d=dict()
    for i in range(p):
        if(i%2==0):
            d[i]="EVEN"
        elif(i%2!=0):
            d[i]="ODD"
    return d
print(n(8))

#Q10
print("-----")
print("Q10")
print(list(filter(lambda x:x%2==0,range(21))))

#Q11.
print("---")
print("Q11")
print(list(filter(lambda x:x%2==0,list(range(1,11)))))
print(list(map(lambda x:x**2,list(filter(lambda x:x%2==0,list(range(1,11)))))))


#Q12.
print("---")
print("Q12")
try:
    print(50/0)
except:
    print("Operation not permitted")

#Q13
print("-------")
print("Q13")
from functools import reduce
print(reduce(lambda x,y:x+y,([1,2,3],[4,5],[6,7,8])))

#Q14.
print("---")
print("Q14")
""""(i) def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
Ans.)=2


(ii) def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()
Ans.)= after f?
"""
