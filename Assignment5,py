#Q1 Homework 5
while(1):
    try:
        j=int(input("Enter integer value"))
        print("Entered value is",j)
    except Exception as e:
        print(e)
        print("Please provide int type value")
       
#Q2 Assignment 5
from sys import argv
nameOfProgram,fileName=argv

print("Name of Program is:",nameOfProgram)
print("Name of file is:",fileName)

while True:
    try:
        f=open(fileName)
        content=f.read()
        print(content)
        fileName.close()
        break
    except:
        print("Entered file name is wrong,please provide correct name")
        try_again=input("press y if you want to try again else n ")
        if(try_again=="Y" or try_again=="y"):
            fileName=eval(input("Please provide the exact name of file"))
        else:
            break

        
#Q3 Assignment 5
gh=open("practice.txt",'w')
gh.write("Hello I am a file \nWhere you need to return the data string \nWhich is of even length \nMake sure you return the content in \nThe same link as it is present.")
gh.close()

with open("practice.txt",'r') as k:
    d=k.readlines()
    for i in d:
        print(i)
    print("Splitted words are:")
    for p in d:
        w=p.split()
        print(w)
    print("Even characters are:")
    for u in d:
        s=u.split()
        for r in s:
            if(len(r)%2==0):
                print(r)

                print(r)
             
