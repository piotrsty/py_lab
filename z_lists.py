names = ['piotr', 'malwa', 'ala', 'tusia', 'pela']
print(names)
print(names[-1])
print(names[-2])
print(names[2:-1])
print(names[:])
names[0] = 'czayu'
print(names)

numbers = [1,2,33,6,9]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#print(max(numbers))