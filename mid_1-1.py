from fractions import *


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

def gcd(a,b):
    list_a = factorization(a)
    list_b = factorization(b)
    
def first_order_equation(a, b):
    if a ==0:
        raise ValueError
    else:
        return Fraction(-b,a)

# 식 정리 하는 알고리즘 만들 필요 있음 (딥러닝 이용)

def find_degree(expression):
    pass

def number_of_terms(expression):
	count = 0
	for i in expression:
		if i == '+':
			count += 1
	return count+1
	
def organize_expression(expression):
	n = 0
	terms = list()
	for i in expression:
		if i == '+':
			n += 1
		terms[n].append(i)
	return terms

def find_variable(expression):
    pass
def sort_like_terms(expression):
    pass
def cal_parentheses(expression):
    pass
def sort_expression(expression, variable):
    expression_list = []
    return expression_list

def find_coefficient(expression, order, variable):
    return sort_expression(expression)[order]

def factorization_dictionary(n):
    factorization_result = dict()
    if n<=1:
        factorization_result[n]=1
        return factorization_result
    
    d=2
    while n != 1:
        if n % d != 0:
            d += 1
        else:
            n //= d
            factorization_result
            
    return 

def paranthesis_check(expression):
	#use stack
	paranthesis_error = bool()
	return paranthesis_error

def is_odd_or_even(n):
    if n<=0:
        return print('%d is not a natural number' %n)
    elif n//2 == 1:
        return print('%d is an odd number' %n)
    elif n//2 == 0:
        return print('%d is an even number' %n)

def is_integer(n):
    return isinstance(n, int)

def is_natural(n):
    return isinstance(n, int) and n>0

def is_positive_or_negative(n):
    if n>0:

    elif n<0:

    elif n==0:

def print_commutative_property(expression):
    count = 0
    for i in expression:
        if i == '+' or i == '-':
            count += 1
        if expression[0] == '-':
            count -= 1
    if count != 2:
        return print("expression cannot use commutative property")

    # + 있는 인덱스 받아서 자리 바꾸기