num = 5

for i in range(1, num+1):
    current_num = num
    for j in range(1, num+1):
        print(current_num, end="")
        current_num -= 1
    num -= 1
    print()