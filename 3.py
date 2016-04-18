import math
a = 600851475143
n = int(math.sqrt(a))
array = [2]
running = True
largest_number = 0
for i in range(3, n + 1, 2):
    for j in array:
        if i % j == 0:
            running = False
            break
    if running == True:
        if i < math.sqrt(n):
            array.append(i)
        if a % i == 0:
            largest_number = i

    running = True

print(largest_number)
