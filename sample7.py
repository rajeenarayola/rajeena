x={"red","blue","balck"}
print(x)
print(type(x))
print(len(x))
for i in x:
    print(i)
x.add("yellow")
print(x)
y={"apple","banana","papaya"}
x.update(y)
print(x)
z=x.union(y)
print(z)
x.discard("blue")
print(x)
a={"pen","door","book"}
b={"desk","door","door"}
c=a.intersection(b)
print(c)
d=a.difference(b)
print(d)
f=a.copy()
print(f)