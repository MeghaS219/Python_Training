try:
    num1 = int(input('number one'))
    num2 = int(input('number two'))
    result = num1/num2
    print(result)
except ZeroDivisionError as e:
    print('you cannot divide by 0')
print('completed successfully')