

# DICTIONARY
(
    " Data type in python .. key value format       keys must be unique     ordered   heterogeneous(store multiple values)   for list,tuple where the index number act as key      \n"
    "  ")

a={'name': 'Pavi',"age": "22","job": "testing"}
print(f'name = {a["name"]}')
a["name"]="Priya"
print(a)
for z in a.items():
    print(z)

stu={"names":["Pavi","Praveen","Janagi","Govind"] , "marks":[94,90,85,75] , "std":[5,7,8,4]}
print(stu)
stu["marks"][0]=96
print(stu.keys())
print(stu.values())
print(stu.items())   # combo of key and value
stu.popitem()
print(stu)
















