a = [1,2,3,4,5]
start = 0
end = len(a)-1

while start < end:
    start_element = a[start]
    end_element = a[end]
    a[end] = start_element
    a[start] = end_element
    start += 1
    end -= 1

print(a)