#linear search

numbers=[5,10,15,20,25,30]

target = int(input("Enter the number for search-  "))
found = False

for i in range(len(numbers)):
    if numbers[i] ==  target:
        print("Element is found in index", i)
        found = True
        break

if not found:
    print("The Element can not be found.")