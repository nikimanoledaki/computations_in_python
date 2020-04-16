# Find the cube root of a perfect cube
x = int(input('Enter an integer:'))
answer = 0  #  answer**3 starts at zero and gets larger each time through loop
while answer**3 < abs(x):
    answer = answer + 1
    print('Value of the decrementing function abs(x) - ans**3 is',
          abs(x) - answer**3)
    if answer**3 != abs(x):
        print(x, 'is not a perfect cube')
    else:  # If it reaches or exceeds X, the loop terminates
        if x < 0:
            answer = -answer
        print('Cube root of', x, 'is', answer)

# The algorithmic technique used in this program is  variant of guess and check called exhaustive enumeration.
# We enumerate all possibilities until we get to the right answer or exhaust the space of possibilities.
