'''
in function iterativePower with base and exponent variable
    every exp value 
        let result equal result time base
    return result
print iterativePower function
'''
def iterativePower(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

print(iterativePower(2,3))
'''
 function recursivePower with base and exp
    if exp equal to one
        return the base
    else
        return the base time the recursive function
print recursivePower function
'''
base = 0
exp = 0
def recursivePower(base, exp):
    if exp == 1:
        return base
    else:
        return base * (recursivePower(base, exp - 1))

print(recursivePower(2,3))
