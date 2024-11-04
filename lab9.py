rows = int(input("Enter number of rows: "))

current_num = 1

for number in range(1, rows + 1):
    for j in range(number):
        print(current_num, end=" ")
        current_num += 1
    print() 
