user_list = []
while True:
    user_name = str(input("Enter your user name  (or type 'stop' to quite) : "))
    if user_name == "stop":
        break
    else:
        user_list.append(user_name)
def swap(user_list):
    user_list[0], user_list[-1] = user_list[-1], user_list[0]
    print(user_list)

swap(user_list)






#     for i in range(user_list):
#         temp = user_list[0]
#         user_list[0] = user_list[user_name-1]
#         user_list[user_name-1] = temp
#     user_list.append(i)
# print(user_list)

