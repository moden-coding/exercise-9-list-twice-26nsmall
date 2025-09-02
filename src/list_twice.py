# Write your solution here
list = []
n = 1
while n != 0:
    n = int(input("New item: " ))
    if n == 0:
        print("Bye!")
    else:
        list.append(n)
        print(f"The list now: {list}")
        print(f"The list in order: {sorted(list)}")
