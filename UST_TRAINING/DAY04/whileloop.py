import random

count = 1
while(True):
    print('Help!')
    if random.choice(range(10000))==111:
        break
    print('Let me out!')
    count = count+1
print('At Last!',count)