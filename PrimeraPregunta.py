
def suma(x, y):
    return x + y
def resta(x, y):
    return x - y
def multiplicacion(x, y):
    return x * y
def divide(x, y):
    return x / y

def calculadora(x, y, op):
    if op == '+':
        r = suma(x, y)
    if op == '-':
        r = resta(x, y)
    if op == '*':
        r = multiplicacion(x, y)
    if op == '/':
        r = divide(x, y)
    return r;  
print(calculadora(5, 7, '+'))
print(calculadora(5, 7, '*'))
print(calculadora(5, 7, '/'))
print(calculadora(5, 7, '-'))
