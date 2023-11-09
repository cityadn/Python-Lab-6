lst = []
for i in range(0, numbers-1):
    num = int(input("Enter a number:\n"))
    lst.append(num)
lst = [lst[-2], lst[-1], lst[0]]
print(lst)

