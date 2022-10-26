def is_prime(n,print_solution):
    if print_solution == 1:
        if n<=0:
            return print('%d is not a natural number.' %n)

        if n == 1:
            return print('%d is not a prime number nor a synthetic number' %n)


        for i in range(2, n):
            if n%i == 0:
                print('%d can be devided by %d' %(n,i))
                return print('%d is a synthetic number' %n)
        
        else:
            return print('%d is a prime nubmer' %n)

    if print_solution == 0:
        if i<2:
            raise ValueError
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

