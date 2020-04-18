def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        print('in loop', i)
        result = digits[i%10] + result
        print('digits[i%10] + result', result)
        i = i//10
        print('i = i//10', result)
    return result

# O(log n) 