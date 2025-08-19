"# creat dictonary
student={"age":21,"name":"krish","grade":'A'}
print(student)
print(student['grade'])
print(student['age'])
student['age']=32
print(student)
student['address']='india'
print(student)
del student['grade']
print(student)
keys=student.keys()
print(keys)
values=student.values()
print(values)
items=student.items()
print(items)
#creat nested dictionarry
student={
    "student1":{"name":'akshat',"age":21},
    "student2":{'name':'taru',"age":20}
}


