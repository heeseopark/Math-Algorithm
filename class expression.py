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

    def organizeParenthesis(self):
        # Initialize a queue to store the open brackets
        queue = []

        # Iterate over the characters in the expression string
        for character in self.expression_string:
            # If the character is an open bracket, append it to the queue
            if character in ['(', '{', '[']:
                queue.append(character)
            # If the character is a close bracket, check if it matches the last open bracket in the queue
            elif character in [')', '}', ']']:
                # If the queue is empty or the open and close brackets do not match, raise a ValueError
                if not queue or (character == ')' and queue[-1] != '(') or (character == '}' and queue[-1] != '{') or (character == ']' and queue[-1] != '['):
                    raise ValueError('Does not match parenthesis rules')
                # If the open and close brackets match, pop the last open bracket from the queue
                else:
                    queue.pop()

        # If the queue is not empty, raise a ValueError
        if queue:
            raise ValueError('Does not match parenthesis rules')

        # Initialize an empty list to store the organized terms
        organized_terms = []

        # Iterate over the terms of the expression
        for term in self.terms:
            # Check if the term has a parenthesis
            if any(character in term for character in ['(', '{', '[']):
                # Extract the coefficient of the term
                coefficient = self.find_coefficient(term)
                # Extract the variable of the term
                variable = None
                for character in term:
                    if character.isalpha():
                        variable = character
                        break
                # Extract the order of the term
                order = self.find_order(term, variable)
                # Extract the expression inside the parenthesis
                inner_expression_string = term[term.index('(')+1:term.rindex(')')]
                # Create an Expression object for the inner expression
                inner_expression = Expression(inner_expression_string)
                # Organize the inner expression
                inner_expression.organizeParenthesis()
                # Multiply the inner expression by the coefficient
                inner_expression.expression_string = f'{coefficient}*{inner_expression.expression_string}'
                # Append the organized term to the organized terms list
                organized_terms.append(inner_expression.expression_string)
            else:
                # If the term does not have a parenthesis, append it to the organized terms list
                organized_terms.append(term)

        # Reassign the expression_string variable with the organized expression
        self.expression_string = '+'.join(organized_terms)



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

class Equation(Expression):
    def __init__(self, equation_string):
        self.equation_string = equation_string
        self.left_side, self.right_side = self.divide_equation_into_sides()
        super().__init__(self.left_side)
        self.variables.update(Expression(self.right_side).variables)
        self.terms = self.get_terms()

    def divide_equation_into_sides(self):
        # Divide the equation into left and right sides
        left_side = ''
        right_side = ''
        on_right_side = False
        for character in self.equation_string:
            if character == '=':
                on_right_side = True
            elif not on_right_side:
                left_side += character
            else:
                right_side += character
        return left_side, right_side

class Inequality(Expression):
    def __init__(self, inequality_string):
        self.inequality_string = inequality_string
        self.left_side, self.right_side, self.inequality_type = self.divide_inequality_into_sides()
        super().__init__(self.left_side)
        self.variables.update(Expression(self.right_side).variables)
       
# # Create an equation
# equation = Equation('5x + 7 = 2')
# print(f'Left side: {equation.left_side}')
# print(f'Right side: {equation.right_side}')
# print(f'Variables: {equation.variables}')
# print(f'Terms: {equation.terms}')

# # Create an inequality
# inequality = Inequality('5x + 7 < 2')
# print(f'Left side: {inequality.left_side}')
# print(f'Right side: {inequality.right_side}')
# print(f'Inequality type: {inequality.inequality_type}')
# print(f'Variables: {inequality.variables}')
# print(f'Terms: {inequality.terms}')

# Left side: 5x + 7
# Right side: 2
# Variables: {'x'}
# Terms: [(5.0, 'x', 1), (7.0, None, 0)]
# Left side: 5x + 7
# Right side: 2
# Inequality type: <
# Variables: {'x'}
# Terms: [(5.0, 'x', 1), (7.0, None, 0)]

def solve_first_order_equation(equation_string):
    # Create an Equation object
    equation = Equation(equation_string)

    # Check if the equation is first-order
    if max([term[2] for term in equation.terms]) != 1:
        raise ValueError('The equation is not first-order.')

    # Check if the equation has a solution
    if equation.left_side() == equation.right_side():
        raise ValueError('The equation has infinite solutions.')
    elif equation.left_side() == 0:
        raise ValueError('The equation has no solutions.')

    # Return the solution
    return f'{equation.variables.pop()} = {equation.right_side()/equation.left_side():.2f}'

def solve_first_order_inequality(inequality_string):
    # Create an Inequality object
    inequality = Inequality(inequality_string)

    # Check if the inequality is first-order
    if max([term[2] for term in inequality.terms]) != 1:
        raise ValueError('The inequality is not first-order.')

    # Check if the inequality has a solution
    if inequality.left_side() == inequality.right_side():
        raise ValueError('The inequality has no solutions.')
    elif inequality.left_side() == 0:
        if inequality.inequality_type == '>':
            return f'{inequality.variables.pop()} > {inequality.right_side()/inequality.left_side():.2f}'
        elif inequality.inequality_type == '<':
            return f'{inequality.variables.pop()} < {inequality.right_side()/inequality.left_side():.2f}'

    # Return the solution
    if inequality.inequality_type == '>':
        return f'{inequality.variables.pop()} > {inequality.right_side()/inequality.left_side():.2f}'
    elif inequality.inequality_type == '<':
        return f'{inequality.variables.pop()} < {inequality.right_side()/inequality.left_side():.2f}'

def system_of_first_order_equations(system_string, method='addition'):
    # Divide the system string into individual equation strings
    equation_strings = system_string.split(';')

    # Create a list of Equation objects
    equations = [Equation(equation_string) for equation_string in equation_strings]

    # Check if the system is first-order
    if any(max([term[2] for term in equation.terms]) != 1 for equation in equations):
        raise ValueError('The system is not first-order.')

    # Check if the system has a solution
    if all(equation.left_side() == equation.right_side() for equation in equations):
        raise ValueError('The system has infinite solutions.')
    elif any(equation.left_side() == 0 for equation in equations):
        raise ValueError('The system has no solutions.')

    # Solve the system using the addition method
    if method == 'addition':
        # Check if the variables of the equations are the same
        variables = [equation.variables.pop() for equation in equations]
        if any(variable != variables[0] for variable in variables):
            raise ValueError('The variables of the equations are not the same.')

        # Find the sum of the coefficients of the variable in the equations
        variable_coefficients = [equation.left_side().coefficients[variable] for equation in equations]
        variable_coefficient_sum = sum(variable_coefficients)

        # Find the sum of the constants in the equations
        constants = [equation.right_side().constant for equation in equations]
        constant_sum = sum(constants)

        # Check if the system has a solution
        if variable_coefficient_sum == 0:
            if constant_sum == 0:
                raise ValueError('The system has infinite solutions.')
            else:
                raise ValueError('The system has no solutions.')

        # Return the solution
        return f'{variables[0]} = {constant_sum/variable_coefficient_sum:.2f}'

    # Solve the system using the substitution method
    elif method == 'substitution':
        # Check if the variables of the equations are different
        variables = [equation.variables.pop() for equation in equations]
        if not all(variable != variables[0] for variable in variables):
            raise ValueError('The variables of the equations are not different.')

        # Solve the first equation for the first variable
        solution = solve_first_order_equation(equations[0].expression_string)
        variable_value = float(solution.split(' = ')[1])

        # Substitute the value of the first variable into the second equation
        second_equation = equations[1].expression_string.replace(variables[0], str(variable_value))

        # Solve the second equation
        return solve_first_order_equation(second_equation)
    else:
        raise ValueError('Invalid method.')

