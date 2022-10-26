def is_prime(n):
    prime_num_list = [2,3,5,7,9,11,13,17,19]
    if n in prime_num_list:
        print('%d is a prime nubmer' %n)
    elif n == 1:
        print('%d is not a prime number nor a synthetic number' %n)
    else:
        print('%d is not a synthetic number' %n)
