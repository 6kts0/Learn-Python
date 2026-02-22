# Find the zeros of a polynomial function
from sympy import symbols , factor, roots, Function
from math import gcd
x = symbols('x')
y = symbols('y')

# Example polynomial
f = 12*x**3 - 17*x**2 - 24*x + 20
fac = factor(f)
rt = roots(f)

print('Factorization: ', fac)
print('Roots dictL: ', rt)
print('Roots list: ', list(rt.keys()))

# Perform rational root test viable numbers: ± factors of 20 / factors of 12
viable_num = []
num_factors = [1, 2, 3, 4, 5, 10, 20]
den_factors = [1, 2, 3, 4, 6, 12]
for a in num_factors:
    for b in den_factors:
        viable_num += [a/b, -a/b]
viable_num = sorted(set(viable_num))
print('Root candidates: ', viable_num[:8])