import datetime


print(24*7);

print("Learning varible in python")

mynow = datetime.datetime.now()
myNuber=10
myText = "hello"

print(mynow,  myNuber, myText);


x=10;
y="10"
z=10.4
sum1 = x + x;
sum2 = y+y



print(sum1)
print(sum2)

print(type(x), type(y), type(z))


print()
print("----------------------")
student_grades = [9.1, 8.8, 7.5]
mysum =sum(student_grades)
length  = len(student_grades)

print( mysum/length )

print()
print("-----------distionary-----------")

student_grades_dic = {"Marry" : 9.1, "sim": 8.8, "John": 9.4}

print(student_grades_dic.values())
keys = student_grades_dic.keys()
value = student_grades_dic.values()


print("-----------tuple-----------")
monday_temperature = (1,2,3,4,5)     #tuples are immutable but list are mutable



