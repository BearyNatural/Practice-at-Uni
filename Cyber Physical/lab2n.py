# What is the output of this?  Here we added the condition that if item match with student3 then exit the loop. 

name = ["student1", "student2", "student3", "student4", "student5"]
for item in name:
    print(item)
    if item=="student3":
        continue
