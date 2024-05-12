lst = [1,4,2,3,2]
val = 5
count = 0
i = 0
while i < len(lst):
    j = i + 1
    while j < len(lst):
        if lst[i] + lst[j] == val:
            count += 1
        j += 1
    i += 1
print(count)