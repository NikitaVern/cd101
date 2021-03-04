# names = (input("Enter Name: ")
# ages = int(input("Enter Age: "))
# input()
# for x in ages:
#      if  x >= 18:
# #         nim.append(x)
#     else:
#         num.append(x)
# print(f"% 2{nim}")
# # print(f"% 1{num}")
# for x in lst:
#     if  x % 2 != 0:
#         print(f"first %2: {x}")

names =[] 
ages =[]
a = 0
from statistics import mean
while True:
    user_data = input(f'Enter name and age: ').split(" ")
    names.append(user_data[0]) 
    ages.append(int(user_data[1]))
    q = input("you nead more? Y or N: ")
    if q == "N":
        break
for idx, val in enumerate(names):
    print(f"User{idx}: {val}, {ages[idx]}")
    a = a + ages[idx]
# average = int(mean(ages))
average = int(a) / len(ages)
print(f"Average age: {average}")