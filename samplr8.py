x={"name":"rayola","age":20,"gender":"female","nation":"india"}
print(x)
print(type(x))
print(len(x))
print(x["age"])
print(x["nation"])
print(x.get("gender"))
print(x.keys())
print(x.values())
print(x.items())
print("name" in x)
print("name" not in x)
x["age"]=22
print(x)
x["name"]="daisy"
print(x)
x.update({"name":"suhana"})
print(x)
x["place"]="aluva"
print(x)
x.update({"district":"ernakulam"})
print(x)
x.pop("name")
print(x)
x.popitem()
print(x)
del x["age"]
print(x)
#x.clear()
#print(x)
#del x
#print(x);
for i in x:
    print(i)
for i in x:
    print(x[i])
for i in x.keys():
    print(i)
for i in x.items():  
    print(i)       
for i in x.values():
    print(i)
g=x.copy()
print(g)
f=dict(x)
print(f)
family={"child1":{"name":"rajena","age":21},"child2":{"name":"ashna","age":11},"child3":{"name":"suhana","age":21}}
print(family)       
print(family["child2"])  
print(family["child2"]["name"])