def check_paranthesis(expression): #오류 있어서 바꿔야 됨
    paranthesis_list = []
    for i in expression:
        if i == '(' or i == '{' or i == '[':
            paranthesis_list.append(i)
            print(paranthesis_list)
        if i == ')' and paranthesis_list[-1] == '(':
            paranthesis_list.pop()
            print(paranthesis_list)
        if i == '}' and paranthesis_list[-1] == '{':
            paranthesis_list.pop()
            print(paranthesis_list)
        if i == ']' and paranthesis_list[-1] == '[':
            paranthesis_list.pop()
            print(paranthesis_list)
    if paranthesis_list == []:
        return True
    else:
        return print('paranthesis order does not match')


exp_1 = '[adsfa;lkjadf+{ads()fasdf(Asdfadf)asdfa())sf}ad{()}fadf]'

#print(check_paranthesis(exp_1))

exp_2 = '3x+4y+7'

def get_value_of_expression(expression):
    variable_list = []
    for i in expression:
        if i.isnumeric() == False and i not in ['+', '-', '*', '/']:
            variable_list.append(i)
    #print(variable_list)

get_value_of_expression(exp_2)
