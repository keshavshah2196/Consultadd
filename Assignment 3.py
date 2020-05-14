#Q1
print("Q1")

rk=[1,65,7.9,9+8j,"stringses",89,9.86,56+7.6j,65,433,"Welcome"]
print("List=",rk)
print("----")

#Q2
print("Q2")
ls=["How're you?",57,7/78,9+0.67j,9/63]
print("Original list, ls=",ls)
print("Length of list=",len(ls))
print("ls[:4]=",ls[:4])
print("ls[2:3]=",ls[2:3])
print("ls[2:]=",ls[2:])
              

print("----")


#Q3
print("Q3")
total=0
product=1
lst=[78,87,7/6+9.8j,89,0.87]
for i in lst:
    total+=i
    product*=i
print("Sum is:",total)
print("Multiplication =",product)
print("----")


#Q4
print("Q4")
sma_lar=[45,76,9/8,95,87]
print("Original list=",sma_lar)
print("Maximmum number=",max(sma_lar))
print("Minnimum value=",min(sma_lar))

print("----")

#Q5
print("Q5")
for i in range(0,34):
    if(i%2==0):
        continue
    else:
        print(i)


print("----")

#Q6
print("Q6")
a=range(1,31)
p=[]

for i in a[-5:] and a[:5]:
    p=i**2
    print("Square value is:",p)
    
print("----")


#Q7
print("Q7")
t=[1,3,5,7,9,10]
print("Original list=",t)
t[-1]=[2,4,6,8]
print("New list after modification =",t)
print("----")

#Q8
print("Q8")
a={1:67,'strings':"Hello Welcome !!!"}
b={4:'Fine','q':7/5+9.8j}
print("Origial Dictionary No.1 =",a)
print("Original Dictionary No.2 =",b)
a.update(b)
print("New dictionaries after concatenatin=",a)

print("----")

#Q9
print("Q9")
p={}
n=eval(input("Enter the range"))
for i in range(n+1):
    p={i:i*i}
    print(p)
    
print("----")


#Q10
print("Q10")
p=[]
for count in range(0,5):
    a=eval(input("Enter the value"))
    p.append(a)
    print("p is",p)
print("List=",p)
q=tuple(p)
print("Tuple=",q)


    

print("----")
