def is_prime(n):

    if n<=0:
        return print('%d is not a natural number.' %n)

    if n == 1:
        return print('%d is not a prime number nor a synthetic number' %n)


    for i in range(2, n):
        if n%i == 0:
            return print('%d is a synthetic number' %n)
    
    else:
        return print('%d is a prime nubmer' %n)