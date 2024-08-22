x=[1,"bag",2,"book",3,"pen",]
print(2)
print(type(x))
print(len(x))
print(x[2])
print(x[3:5])
print(x[5:])
print(x[-1:])
print(x[-4:-1])
print(x[-2])
print(x[-1])
print("pen" in x)
print("pen" not in x)
for i in x:
    print(i)
x[1]="apple"
print(x)
x[3]="orange"
print(x)
x.append("red")
print(x)
x.insert(2,"door")
print(x)
y=["desk","yellow"]
x.extend(y)
print(x)
x.remove("pen")
print(x)
x.pop(3)
print(x)
x.pop()
print(x)
#del x[3]
print(x)
z=x.copy()
print(x)
c=list(x)
print(c)
y=["orange","apple","banana"]
y.sort()
print(y)
y.sort(reverse=True)
print(y)
z=x+y
print(z)
del x
#print(x)
p=y.count(3)
print(p)