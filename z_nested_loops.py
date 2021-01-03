#for x in range(2):
#    for y in range(2):
#        print(f'({x},{y})')

numbers = [3,4,6,2]
for x_count in numbers:
    #print('x' * x_count)
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

