# def myfunc(a,b):
#     return a+b
    
# def hello():
#     z= myfunc(6,1)
#     print(z)
# myfunc()


# x=10 
# def myfunc(a,b):
#     x=10
#     return a+b

# myfunc(5,1)
# print(z)


# class User:
#     def __init__(self, first_name, last_name, birth, sex):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birth = birth
#         self.sex = sex

#     def grit(self):
#         print (f"Name: {self.first_name}, {self.last_name}, age: {self.birth}")

#     def calc_age(self, curr_year):
#         return curr_year - self.birth    
#     @staticmethod
#     def calc_avg(self, other):
#         z= (self.calc_age(2021)+ other.calc_age(2021)) / 2
#         return z
# user1 = User("pop", "dod", 1988, "male")
# user2 = User("ptep", "drd", 1980, "male")
# User.calc_avg(user1, user2)
# user1.grit()
# print(user1.calc_age(2026))


# import math

# x= 10
# y= math.pow(x,2)

# print(y)

# def avg_age(ages):
#     return sum(ages) / len(ages)
# if __name__ == "__main__":
# print(avg_age([12, 34, 54, 54,34533]))

import pop
birth = int(input("Enter birth year: "))
print(pop.calc_age(birth))
