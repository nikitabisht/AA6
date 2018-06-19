#question1

for i in range(10):
    a=int(input("enter the values:"))
    print(i)

#end

#question2

while(True):
    print("nikita")



#end

#question3
l=[]
a=int(input("enter the input"))
b=int(input("enter the input"))
l.append(a)
l.append(b)
for i in l:
    print(i**2)

#question4

l=(([1,2],("string"),[1.2,1.3]))
for i in (l):
    a=[]
    b=[]
    c=[]
    print(*l,sep="\n")
    break

#end

#question5

even_number=[]
odd_number=[]
for number in range (1,101):
    if number % 2 == 0:
        even_number.append(number)
    else :
        odd_number.append(number)
print("even number :",even_number)
print("odd number :",odd_number)

#question6

for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()

#question7

dictionary={'niki':'name','shivi':'name2'}
for i in dictionary:
    dictionary.get(i)
    print(i)

#question8
l=[]
for i in range(0,5):
    num=int(input("enter the number:"))
    l.append(num)
print(l)
l2=[]
a=int(input("enter the value:"))
x=l.index(3)
x=l.remove(3)
print(l)







