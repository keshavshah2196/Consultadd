#Q1
print("Q1")
n=eval(input("Enter any number"))
if(n%3==0 and n%5==0):
    print("Consulatdd Python Training")
elif(n%3==0):
    print("Consultadd")
elif(n%5==0):
    print("c")
print("-----------")

#Q2
print("Q2")
a=int(input("Enter 1st integer"))
b=int(input("Enter 2nd integer"))
operator=int(input("Enter operation to be done by typing any value between 1 to 5"))

if(operator==1):
    answer=a+b
    print("You selected Addition, your answer=",answer)
elif(operator==2):
    answer=a-b
    print("You selected Subtraction, your answer=",answer)
elif(operator==3):
    answer=a*b
    print("You selected Multiplication, your answer=",answer)
elif(operator==4):
    answer=a/b
    print("You selected Division, your answer=",answer)
elif(operator==5):
    print("You need to enter 2 more values")
    c=int(input("Enter 3rd inbteger"))
    d=int(input("Enter 4th nteger"))
    answer=(a+b+c+d)/4
    print("You selection was Average,and the answer =",answer)
else:
    print("You entered an invalid operation, only 1-5 are valid range")
if(answer<0):
    print("NEGATIVE")
    
print("-----")


#Q3
print("Q3")
a=10
b=20
c=30
avg=(a+b+c)/3
print("Average is:",avg)

if(avg>a and avg>b and avg>c):
    print("Avg is higher than a,b,c")
elif(avg>a and avg>b):
    print("Avg is higher than a and b")
elif(avg>a and avg>c):
    print("Avg is higher than a and c")
elif(avg>b and avg>c):
    print("Avg is higher than b and c")
elif(avg>a):
    print("Avg is higher than a")
elif(avg>b):
    print("Avg is higher than b")
elif(avg>c):
    print("Avg is higher than c")
    
print("-----------")

#Q4 Doubt(with infinite
"""
print("Q4")
n=eval(input("enter any number"))
print("You entered",n)
while(1):
    if(n<0):
        print("It's over")
        break

    elif(n>0):
        continue
    print("Good Going")

print("-----")
"""

#Q5
print("Q5")
num=2000
while(num<=3200):
    if(num%7==0 and num%5!=0):
        print("Number divisible by 7 is",num)
    num+=1

print("------")

#Q6
print("Q6")
print("Ans. 6a.  Output will show error since int is not iterable")
print("Ans 6b. 0 1 2 will be displayed vertically")
print("Ans 6c. 0 1 2 3 4 5 will be displayed vertically")

print("----------")


#Q7
print("Q7")
num=-1
while(num<6):
    num+=1
    if(num==3 or num==6):
        continue
    print(num)
print("---------")

#Q8
print("Q8")
s=input("Enter the string")
print("Entered string is:",s)
digits=0
letters=0
for i in s:
    if(i.isalpha()):
        letters+=1
    elif(i.isdigit()):
        digits+=1
print("Number of Digits =",digits,"Number of Letters=",letters)


print("-----------")

#Q9
print("Q9a.")
p=78
q=eval(input("Guess the number"))
while(q!=p):
    print("Guess the number")
    q=eval(input("Guess the correct number"))
else:
    print("Number is correct")
print("--")
print("Q9b.")
p=87
q=eval(input("Guess the number"))
while(q!=p):
    print(q,"is not correct, do you want to gess again?")
    s=eval(input("Press 1 for yes or 0 for no"))
    if(s==0):
        break
    elif(s==1):
        q=eval(input("Guess the number"))
    else:
        print("Enter only 0 or 1 for yes or not")
        continue
else:
    print("Well done",q,"is the correct answer")

    
print("_-----------")

#Q10
print("Q10")
luckyNumber=83
count=1

while(count<=5):
    guess=eval(input("Guess the lucky number"))
    if(guess==luckyNumber):
        print("Good guess")
        print("Entered number is correct",guess)
        break
    else:
        print("Try again!")
        count+=1
print("Game Over")

print("-----------")

#Q11
print("Q11")
luckyNumber=36
count=1

while(count<=5):
    guess=eval(input("Guess the lucky number"))
    if(guess==luckyNumber):
         print("Good guess")
         print("Entered number is correct",guess)
         break
    else:
        print("Try again!")
    count+=1
if(guess!=luckyNumber):
    print("Sorry but that was not very successful")
    
print("---------")
