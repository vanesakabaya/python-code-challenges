marks = [[56,89,70,92,67,100],
         [60,70,100,45,70,76], 
         [60,95,90,85,93,45],
         [55,80,56,45,51,76],
         [78,100,65,77,91,87], 
         [45,78,65,50,45,87],
         [32,50,45,67,40,80]
        ] 
students = ["Pelin","Dominique","Valentin","Christine","John Paul","Patrick","Kellen"] 

subjects = ["Algorighms and Data Structures","Java","Web App Development","Databases", 
            "Human Computer Interaction"," Information Retrieval"]
# calculating toatal and average marks of students in School of computing science
total_marks = []
average_marks = []
for i in range(0, len(marks)):
    total_marks.append(sum(marks[i]))
    average_marks.append(sum(marks[i])/len(subjects))
    #printing total marks and average marks of students
print(total_marks)
print(average_marks)

#checking the maximum marks in array
max_marks = 0
min_marks = max(average_marks)
for n in average_marks:
    if n > max_marks:
        max_marks = n
    elif n < min_marks:
        min_marks = n

    


for name in students:
    for i in range(0, len(students)-1):
        print(f"{name} studied {subjects[i]} has got {marks[students.index(name)][i]} marks")
    print(f"{name} total marks {total_marks[students.index(name)]}")
    print(f"{name} Average marks {average_marks[students.index(name)]}")
print(f"{students[average_marks.index(max_marks)]} is the highest achieving student")

