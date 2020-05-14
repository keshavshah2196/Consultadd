
print("Q1")
lis1=[89,9.86,7/3,7.8+06j,"List_Struct","16","Welcime",76,45.8,7+9j]
print(lis1)
print("---------")

print("Q2")
y=["StingData",86,8.9j+7/5,7.99,45.9]
print("List=",y)
print("y[:]=",y[:])
print("y[::]=",y[::])
print("y[::-1]=",y[::-1])
print("y[2:]=",y[2:])
print("---------")


print("Q3")
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
y=x[5]
print("y[:4]=",y[:4])
print("x[6:8]=",x[6:8])
print("x[0:len(x):2]=",x[0:len(x):2])
print("x[::-1]=",x[::-1])
print("x[5][5][0]=",x[5][5][0])
print("---------")


print("Q4")
print("---------")
"""

"""

print("Q5")
print("---------")
print("The main advantage of Tuple over list is that when only Read operation is requireTuple retrieves and reads the data very fastly as compared to list because the size of memory of Tuple is smaller as compared to List so its easy to retrive the data fastly in Tuple.")

print("Q6")
print("---------")
for i in range(1,101):
    if(i%3==0 and i%2==0):
        print("Number=",i)

print("Q7")
print("---------")
a="Consultadd Training"
s=""
vow=''
k=len(a)
while(k>0):
    s+=a[k-1]
    k-=1
print("Reverse string=",s)

for i in range(len(s)):
    if(s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='i' or s[i]=='u'):
        vow+=s[i]
print("Vowels in reverse string are:",vow)


print("Q8")
s="hello my name is Keshav !!"
print("Actual string=",s)
print("Even characters are")
w=s.split()
for i in w:
    if(len(i)%2==0):
        print(i)

print("------")
print("Q9")
x=[1,2,3,4,5,6,7,8,9,-1]
for i in range(0,len(x)):
    for j in range(0,i):
        if(x[i]+x[j]==8):
            print("Two number making sum 8 are:=",x[i],x[j])
print("_______")
            
print("Q10")
evenL=[]
oddL=[]
e=len(evenL)
o=len(oddL)
soo=0
soe=0

while(True):
    n=eval(input("enter number between 1 & 50 only"))
    if(n>1 and n<50):
        if(n%2==0 and e<5):
            evenL.append(n)
            e+=1
            soe+=n
            print("Even list=",evenL,"length=",e,"Sum=",soe)

        elif(n%2!=0 and o<5):
            oddL.append(n)
            o+=1
            soo+=n
            print("Odd list=",oddL,"Sum=",soo,"Length=",o)
    if(e==o==5):
        break
print("Even number list=",evenL,"Sum=",soe,"MAximmum=",max(evenL))
print("Odd number Lis",oddL,"Sum-",soo,"MAx value=",max(oddL))
print("---------")


print("Q11 ")
n=input("Enter character string")
count_dict={}
for i in n:
    if i.isalpha():
        if i in count_dict:
            count_dict[i]+=1
        else:
            count_dict[i]=1
print(count_dict)

print("--------")


print("Q12")
li=[]
tu=(1,2,3,4,5,6,7,8,9,10)
a=list(tu)
print("Original tuple=",tu)

for i in a:
    if(i%2==0):
        li.append(i)
tupNew=tuple(li)
print("New Tuple=",tupNew)

print("---------")

print("Q13")
print("---------")
