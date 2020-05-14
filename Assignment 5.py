
#Q1 (Run's continously so comented)
"""print("Q1")
while(1):
    try:
        j=int(input("Enter integer value"))
        print("Entered value is",j)
    except Exception as e:
        print(e)
        print("Please provide int type value")
print("----")
"""

#Q2 (Some error in the code)

"""
print("Q2")
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

print("--")
"""
#Q3 Assignment 5
print("Q3")
while(True):
    try:
        o=input("Enter the 4 digit characteer")
        if(len(o)==4):
            print(o)
            break
    except:
        print("Only 4 digits size is allowed, not more nor less values are allowed")


#Q6
print("---")
print("Q6")
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

