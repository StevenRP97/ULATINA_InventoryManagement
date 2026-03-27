from database import users, pcs, assignments
from validations import userValidation, serialNumberValidation 

user_id = input("Insert the user ID you want to assing to: ")
serialNumber = input("Insert the serialNumber you want to assign: ")

if userValidation(user_id) == False or serialNumberValidation(serialNumber) == False: print("Something doesn't exist") 

assignments.append({"user_id":user_id, "serialNumber":serialNumber, "is_active":"1"})

for i in assignments: print(i)

print(userValidation(user_id))
