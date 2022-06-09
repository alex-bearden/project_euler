from sympy.solvers.diophantine import diophantine
from sympy import symbols
from sympy import simplify

n, m = symbols('n, m', integer=True)
k = symbols('k', integer=True)
s = diophantine(n**2 - 2*n*m - m**2 - n +m, k)

m1, n1 = s.pop()
m2, n2 = s.pop()

if simplify(n1.subs({k: 1})) < 0:
	n,m = [n2, m2]
else:
	n,m = [n1, m1]	

count = 1

while True:
	blues = simplify(n.subs({k: count}))
	reds = simplify(m.subs({k: count}))
	if blues + reds > 10**12:
		print(blues)
		break
	count += 1
