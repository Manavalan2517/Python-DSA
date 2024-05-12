num = 5
current_num = 0

for i in range(1, num+1):
    current_num = i
    for j in range(1, i+1):
        print(current_num, end=" ")
    print()