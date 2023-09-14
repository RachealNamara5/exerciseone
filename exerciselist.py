#change80 to 89
student_marks=[60,80,90,98]
student_marks[1]=[89]
print(student_marks)

#add anew item(appending 55 to students marks)
student_marks=[60,80,90,98]
student_marks.append(55)
print(student_marks)

#find the size ofthe students marks after append
print(len(student_marks))

#write a python program to sum allthe items in the students marks list
total=sum(student_marks)
print(total)

#write python function that takes two lists and returns,if they have atleast one common member
list1=input("Enter items")
list2=input("Enter items")
if list1 and list2:
    print("yes,has a common item")
else:
    print("no")




