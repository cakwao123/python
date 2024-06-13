courses =["Computer science","IT","BIT","Software Engineering"]
print(courses)
# Accessing an element in an array
print(courses[2])
# looping through an array
for x in courses:
    print(x)

    # Adding a new element in an array
    courses.append("Datascience")
    print(courses)

    # Deleting an element in an array
    courses.remove("IT")
    print(courses)
