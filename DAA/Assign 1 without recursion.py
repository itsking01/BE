first = 0
second = 1
#n = 20
print(first)
print(second)

nterm = int(input("Enter the string count :")) 
for i in range(1, nterm):
    third = first+second
    first,second = second,third
    print(third)