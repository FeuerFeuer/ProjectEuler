num = 0
for i in range(100000,999*999):
    a = str(i)
    if a[0] == a[5] and a[1] == a[4] and a[2] == a[3]:
        n = 100
        while n < 1000:
            if i % n == 0 and i / n < 1000:
                num = i            
            n += 1
print(num)
