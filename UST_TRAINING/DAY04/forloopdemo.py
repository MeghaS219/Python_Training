def printName(name,Num):
    """Print the given string for the given number of time"""
    for i in range(Num):
        print(i)
        print(name)

print('Enter your name')
Name = input()
print('Number of times the name need to be print')
Num = int(input())
printName(Name,Num)