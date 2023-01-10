def get_prime_list(n, print_solution):
    
    #최댓값을 주고 소수 출력
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
    # Create a list with n+1 elements, where the value of each element is the index
    factors = [i for i in range(n+1)]

    # Initialize the list of factorization results with null values
    result = [None] * (n+1)

    # Iterate over the list of factors from 2 to n
    for i in range(2, n+1):
        # If the value of the element at index i is equal to i, it means that i is a prime number
        if factors[i] == i:
            # Set the value at index i in the result list to 0
            result[i] = 0

            # Iterate over the multiples of i and set their value in the factors list to i
            for j in range(i*i, n+1, i):
                factors[j] = i

        # If the value of the element at index i is not equal to i, it means that i is not a prime number
        # and it can be expressed as the product of other factors
        else:
            # Set the value at index i in the result list to the number of times i can be divided by its least prime factor
            result[i] = result[factors[i]] + 1

    # Initialize an empty list to store the factorization results
    factorization = []
    # Iterate over the result list
    for i, count in enumerate(result):
        # If the count is not None, it means that the index i is a prime factor and the value is its order
        if count is not None:
            factorization.append((i, count))
    return factorization

def get_gcd(a, b):
    # Get the factorizations of a and b
    a_factors = factorization(a)
    b_factors = factorization(b)
    # Initialize a list to store the GCD factors
    gcd_factors = []
    # Find the minimum length of the factorizations
    min_length = min(len(a_factors), len(b_factors))
    # Iterate over the indices of the factorizations
    for i in range(2, min_length):
        # If the orders of the i-th factors are equal, append the i-th prime and order to the GCD factors list
        if a_factors[i] == b_factors[i]:
            gcd_factors.append([i, a_factors[i]])
        # If the orders of the i-th factors are different, append the i-th prime and the minimum order to the GCD factors list
        else:
            gcd_factors.append([i, min(a_factors[i], b_factors[i])])
    # Return the GCD factors list
    return gcd_factors

def get_lcm(a, b):
    # Get the factorizations of a and b
    a_factors = factorization(a)
    b_factors = factorization(b)
    # Initialize a list to store the LCM factors
    lcm_factors = []
    # Find the maximum length of the factorizations
    max_length = max(len(a_factors), len(b_factors))
    # Iterate over the indices of the factorizations
    for i in range(2, max_length):
        # If the i-th index is not present in one of the factorizations, use the order from the other factorization
        if i >= len(a_factors):
            lcm_factors.append([i, b_factors[i]])
        elif i >= len(b_factors):
            lcm_factors.append([i, a_factors[i]])
        # If the orders of the i-th factors are different, append the i-th prime and the maximum order to the LCM factors list
        else:
            lcm_factors.append([i, max(a_factors[i], b_factors[i])])
    # Return the LCM factors list
    return lcm_factors

