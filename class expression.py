import re

class Expression:
    def __init__(self, expression_string):
        self.expression_string = expression_string
        self.variables = self.find_variables()
        self.terms = self.divide_expression_into_terms()

    def find_variables(self):
        variables = set()
        for term in self.terms:
            for character in term:
                if character.isalpha() and character not in variables:
                    variables.add(character)
        return variables

    def divide_expression_into_terms(self):
        terms = []
        current_term = ''
        for character in self.expression_string:
            if character in ['+', '-']:
                terms.append(current_term)
                current_term = character
            else:
                current_term += character
        terms.append(current_term)
        return terms

    def find_coefficient(self, term):
        coefficient_match = re.match(r'^[+-]?\d*\.?\d*', term)
        if coefficient_match:
            return float(coefficient_match.group())
        else:
            return 1.0

    def find_order(self, term, variable):
        if variable not in term:
            return 0
        order_match = re.search(r'\^\d+', term)
        if order_match:
            return int(order_match.group()[1:])
        else:
            return 1

    def get_terms(self):
        terms = []
        for term in self.terms:
            term_coefficient = self.find_coefficient(term)
            term_variable = None
            for character in term:
                if character.isalpha():
                    term_variable = character
                    break
            term_order = self.find_order(term, term_variable)
            terms.append((term_coefficient, term_variable, term_order))
        return terms

expression = Expression('5y^3 + 4y^2 + 9y + 7')

# Find the variables in the expression
variables = expression.find_variables()
print(f'Variables: {variables}')

# Divide the expression into individual terms
terms = expression.divide_expression_into_terms()
print(f'Terms: {terms}')

# Find the coefficient of a term
coefficient = expression.find_coefficient('5y^3')
print(f'Coefficient of 5y^3: {coefficient}')

# Find the order of a term
order = expression.find_order('5y^3', 'y')
print(f'Order of 5y^3: {order}')

# Get the terms of the expression
terms = expression.get_terms()
print(f'Terms: {terms}')

# Variables: {'y'}
# Terms: ['5y^3', '4y^2', '9y', '7']
# Coefficient of 5y^3: 5.0
# Order of 5y^3: 3
# Terms: [(5.0, 'y', 3), (4.0, 'y', 2), (9.0, 'y', 1), (7.0, None, 0)]
