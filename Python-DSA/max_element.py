lst = [4,1,7,5,10]
max_element=0
for i in range(len(lst)):
    if lst[i] > max_element:
        max_element = lst[i]
print(max_element)