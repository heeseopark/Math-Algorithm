import re

class term_class():
    def __init__(self,coefficient,order):
        self.coefficient = coefficient
        self.order = order
    def get_coefficient():
        co = self[0]
        return co
    def get_order():
    


terms = expression.split(' ')
print(terms)

# ['3x', '+', '4y', '-', '2z']



for term in terms:
    match = re.search(r'([+-]?\d*)(\w+)', term)
    coefficient = int(match.group(1)) if match.group(1) else 1
    variable = match.group(2)
    print(f'{coefficient} {variable}')

# 3 x
# 4 y
#-2 z
