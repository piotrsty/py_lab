numbers = [5,3,6,8,0]
numbers2 = numbers.copy()
#numbers.append(13)
#numbers.insert(1,99)
#numbers.remove(3)
#numbers.clear()
#numbers.pop() #remove last in the list 
numbers.sort()
numbers.reverse()
#print(numbers.index(3))
#print(numbers)
#print(9 in numbers)
#print(numbers.count(5))

# removes the duplicats or shows uniq
num = [1,2,1,3,2,6]
#new_num = []
for i in num:
    ile = (num.count(i))
    if ile > 1:
        num.remove(i)
#        new_num.append(i)
#print(new_num)
print(num)

# other method 
num2 = [4,5,4,3,5,6]
uniques = []
for number in num2:
    if number not in uniques:
        uniques.append(number)
print(uniques)


