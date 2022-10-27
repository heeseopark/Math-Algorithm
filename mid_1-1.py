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

def prime_list(n, print_solution):
    if print_solution == 0:
        # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
        sieve = [True] * n

        # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if sieve[i] == True:           # i가 소수인 경우
                for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                    sieve[j] = False

        # 소수 목록 산출
        return [i for i in range(2, n) if sieve[i] == True]

def factorization(n):
    if n<=1:
        return n
    result = []
    d=2
    while n != 1:
        if n % d != 0:
            d += 1
        else:
            n //= d
            result.append(d)
    return result