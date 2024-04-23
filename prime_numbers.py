#display all the prime numbers between 1 to 250

for num in range(1, 250):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            print(num)
            break


