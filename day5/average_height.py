student_height = input("height of students").split()

for n in range(0 ,len(student_height)):
  student_height[n] = str(student_height[n])
print(student_height)

total_height = 0
for height in student_height:
  total_height +=int(height)
print(total_height)
  
number_of_students = 0 
for _student in student_height:
  number_of_students = number_of_students + 1

average_height = round(total_height / number_of_students)
print(average_height)
  