x={"apple","banana","tomato","papaya"}
print(x)
print(type(x))
print(len(x))
for i in x:
    print(i)
print("tomato" in x)
print("tomato"not in x)
x.add("red")
print(x)
y={"blueberry","blackberry"}
x.update(y)
print(x)
x.remove("tomato")
print(x)
#x.remove("potato")
#print(x)
x.discard("potato")
print(x)
x.discard("apple")
print(x)
x.pop()
print(x)
x.clear()
print(x)
#del x
#print(x)
z=x.union(y)
print(z)
d={"door","bag","pen",}
c={"door","desk","cup"}
f=d.intersection(c)
print(f)
h=d.difference(c)
print(h)
g=d.copy()
print(g)