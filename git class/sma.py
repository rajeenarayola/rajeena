# x=lambda y:y+10
# print(x(7)) 

# x=lambda z,y,a:y+z+a
# print(x(2,4,5)) 

# x=lambda z,y:z*y
# print(x(1,3))

# x=["apple","banana","papaya"]
# print(x)
# print(type(x))
# print(len(x))
# x[1]="kiwi"
# print(x)
# x.append("red")
# print(x)
# x.insert(2,"yellow")
# print(x)
# y=["door","desk"]
# x.extend(y)
# print(x)
# x.remove("desk")
# print(x)
# x.pop(3)
# print(x)
# x.pop()
# print(x)
# z=x.copy()
# print(x)
# c=list(x)
# print(c)
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)
# z=y+x
# print(z)
# p=z.count(3)
# print(z)
# # x.clear()
# # print(x)
# a=["apple","papaya"]
# b=list(map(lambda i:i.upper(),a))
# print(b)
# x=["APPLE","PAPAYA"]
# y=list(map(lambda i:i.lower(),x))
# print(y)
# x=[1,2,3,4,5,6,7,8,9]
# y=list(filter(lambda i:i>2,x))
# print(y)

x=[1,2,3,4,5,6,7,8,9,]
y=list(filter(lambda i:i%2==0,x))
print(y)

x=[1,2,3,4,5,6,7,8,9]
y=list(filter(lambda i:i%2!=0,x))
print(y)
