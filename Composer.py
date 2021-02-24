from statistics import mean
composers = []
age = []
n = int(input("Enter number of composers: "))
for i in range(n):
    com_data = input(f'Enter full name, year of birth and death of composer number {i + 1}: ')
    composers.append(com_data)
for i in range(n):
    vozrast = int(composers[i].split(" ")[3]) - int(composers[i].split(" ")[2])
    print(f'First Name: {composers[i].split(" ")[0]}, Last Name: {composers[i].split(" ")[1]}, Age: {vozrast}')
    age.append(vozrast)
average = int(mean(age))
print(f"Average age: {average}")