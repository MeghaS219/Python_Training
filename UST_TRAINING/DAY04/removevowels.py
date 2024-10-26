def removevowels(s):
    """Returns the given string after removing the vowels"""
    results =''
    vowelslist = ['a','e','i','o','u','A','E','I','O','U']
    for i in s:
        if i not in vowelslist:
            results = results+i
    return results

def ttime(s):
    result =''
    for i in range(len(s)):
        if s[i-1] == ' ':
            result += s[i]
    return result

#print(removevowels('anjubaba'))
#print(ttime('time to travel! '))

for i in range(7):
    print(i*5,end=' ')
            
