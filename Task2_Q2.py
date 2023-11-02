def primeFactor(number):
    prime_number = []
    for i in range(2, number+1):
        if number % i == 0:
            prime_number.append(i)
    print("These are the multiple prime number of original number : ", prime_number)
primeFactor(35)
