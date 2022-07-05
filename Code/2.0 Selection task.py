#Predetermined data
user1 = ["user1", "Pa$$w0rd"]
user2 = ["Kim", "monkey1234"]
user3 = ["kayhowe", "Ange1!"]

#create lists
user_list = [user1, user2, user3]

#user input requested step 1
#this needs a for loop to iterate through the list??
user_name = input("Enter username:\n")

if user_name in user_list:
    print("User exists.")
    user_password = input("Enter password:\n")
    if user_list[1] == user_password:
        print("login successful")
    else:
        print("login unsuccessful")
else:
    print("user does not exist")



#test
# print(type(user_list))
# print(user_list)
# print(user_list[0])
# print(user_list[1])
# print(user_list[2])


# for user in range(0, len(user_list)):
#     if user_list[user][0] == user_name:
#         print("User exists.")
#         user_password = input("Enter password:\n")
#         if user_list[user][1] == user_password:
#             print("login successful")
#         else:
#             print("login unsuccessful")
#     else:
#         print("user does not exist")