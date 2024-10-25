rows = int(input("Enter number of rows: "))

current_number = 1

for number in range(1, rows + 1):
    for j in range(number):
        print(current_number, end=" ")
        current_number += 1
    print() 