list=[]
a=int(input("enter the number to add in list :"))
for i in range (a):
    num=int(input("enter the number :"))
    list.append(num)
print(list)
rot=int(input("enter the rotation number :"))
f=list[rot:a+1]
g=list[0:rot]
v=f+g
print(v)
