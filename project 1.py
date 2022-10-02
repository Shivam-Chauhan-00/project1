def round1():
    print("This is round 1.\nYou have to enter the corret meaning of giving word")
    l1=["NOUTRYC","SSBUNEIS","MENARGUT","RABHSAU ISR","OPALBH"]
    l2=["COUNTRY","BUSINESS","ARGUMENT","SAURABH SIR","BHOPAL"]
    a=0
    l3=[]
    c=0
        
    while a<=4:
        print(l1[a])
        b=input("arrange the letters to a correct word: ")
        l3.append(b.upper())
        
        if l3[a]==l2[a]:
            c=c+1
            print("+1")
        else:
            c=c-1
            print("-1")
        a=a+1
        
    print("Your scoure is ",c)
    return c

def round2():
    print("This is round 2.\nYou have to enter the corret meaning of giving word")
    l1=["YTHONP","AAJV","NGODJA","ORKWAMEFR","ACTRE"]
    l2=["PYTHON","JAVA","DJANGO","FRAMEWORK","REACT"]
    a=0
    l3=[]
    c=0 
    
        
    while a<=4:
        print(l1[a])
        b=input("arrange the letters to a correct word: ")
        l3.append(b.upper())
    
        if l3[a]==l2[a]:
            c=c+1
            print("+1")
        else:
            c=c-1
            print("-1")
        a=a+1
        
    print("Your scoure is ",c)
    return c

def round3():
    print("This is round 3.\nYou have to enter the corret meaning of giving word")
    l1=["NDIAI","ANJPA","TAIINBR","ISSURA","THESLANDNER"]
    l2=["INDIA","JAPAN","BRITAIN","RUSSIA","NETHERLANDS"]
    a=0
    l3=[]
    c=0
        
    while a<=4:
        print(l1[a])
        b=input("arrange the letters to a correct word: ")
        l3.append(b.upper())

        if l3[a]==l2[a]:
            c=c+1
            print("+1")
        else:
            c=c-1
            print("-1")
        a=a+1
        
    print("Your scoure is ",c)
    return c

print("This is WORD PUZZLE ")
r1=round1()
r2=round2()
r3=round3()
t=r1+r2+r3


print("Your Final Scoure is:",t)
if t>10:
    print("EXELENT")
elif 10>=t and t>5:
    print("AVERAGE")
else:
    print("BAD")




