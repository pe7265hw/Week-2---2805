import author as aut

#Adding data to classes for both Author and Student, did not realize we would be creating another class so both are in Author file, I guess I could
#have created a seperate one for Student but I decided not to since thise won't be a larger project.
a1 = aut.Author("Stephen King")
a1.publish("Cujo")
a1.publish("IT")
a1.publish("IT")

print(a1)

student1 = aut.Student('Johnny', 7, 3.5)
student2 = aut.Student('Sally Mae', 8, 3.1)
student3 = aut.Student('Johnny Goodiegood', 2, 4.0)

print(student1)