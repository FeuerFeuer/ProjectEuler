number = 210

while True:
    divisible = True
    for i in range(3, 21):
        if number % i != 0:
            divisible = False
            break

    if divisible:
        print(number)
        break

    number += 210
