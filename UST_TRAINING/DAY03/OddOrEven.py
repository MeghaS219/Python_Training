def OddOrEven(num):
    if not (num == 0):
        if num%2 == 0:
            return 'Even'
        else:
            return 'Odd'
    else:
        return 'zero'
    
#print('number is ',OddOrEven(4))
#print('number is ',OddOrEven(5))
#print('number is ',OddOrEven(0))

print('Please enter the number')
user_input = int(input())
print(user_input)
print('number is ',OddOrEven(user_input))
