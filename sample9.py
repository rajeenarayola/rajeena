x={"name":"suhana","age":56,"gender":"female"}
print(x)
print(type(x))
print(len(x))
print(x["age"])
print(x["gender"])
print(x.get("name"))
print(x.keys())
print(x.values())
print(x.items())
x.update({"name":"rajeena"})
print(x)
x["place"]="aluva"
print(x)
x.update({"district":"wayanad"})
print(x)
x["age"]=27
print(x)
#x.clear()
#print(x)
del x["age"]
print(x)
for i in x:
    print(i)
for i in x.keys():
    print(i)
for i in x.items():
    print(i) 
for i in x.values():
    print(i)
f=dict(x)
print(f) 
family={"child1":{"name":"rajeena","age":10},"child2":{"name":"suhana","age":21}}
print(family)
print(family["child1"])
print(family["child2"])           