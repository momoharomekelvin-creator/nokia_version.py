import random

numbers = []
for i in range (10):
     number = random.randint(1,50)
     numbers.append(number)
print(numbers)




count = 0
for number in numbers:
    count = count + 1
print(count)





even_sum = 0
for i in range(count): 
    if i % 2 == 0:
         even_sum = even_sum + numbers[i]
print(even_sum)



odd_sum = 0 
for i in range(count):
    if i % 2 != 0:
          odd_sum = odd_sum + numbers[i]
print(odd_sum)





product = 1
for i in range (count):
    if(i+1)% 10 == 0:
        product = product * numbers[i]
print(product)
