composers_data={}
while True:
    name=input("Please enter composer's name: ")
    birth=input("Please eneter composer's birth year: ")
    death=input("Please enter composer's death year: ")
    def minus(x, y):
        z=x-y
        return z
    age=minus(int(death),int(birth))
    composers_data[name]=int(age)
    q=input("if you want to finish write 'No': ")
    if q in['No','no','n','N']:
        break
for name,age in composers_data.items():
    print(f"Name: {name}, Age: {age}")
def avg(ages):
    n=0
    for x in ages:
        n=n+x
    a=n/len(composers_data)
    return a
print(f"Average age: {avg(composers_data.values())}")