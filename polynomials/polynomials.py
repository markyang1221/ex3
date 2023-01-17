from numbers import Number
from numbers import Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        if isinstance(self.coefficients, Number):
            return 0
        else:
            return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        if isinstance(other, Polynomial):
            list1 = [-n for n in list(other.coefficients)]
            temp = Polynomial(tuple(list1))
            return self+temp

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,) + self.coefficients[1:])

        else:
            return NotImplemented
    
    def __mul__(self, other):

        if isinstance(other, Number):
            list1 = [a * other for a in list(self.coefficients)]
            return Polynomial(tuple(list1))

        elif isinstance(other, Polynomial) and isinstance(self, Polynomial):
            deg_1 = len(self.coefficients) - 1
            deg_2 = len(other.coefficients) - 1
            ans = [0] * (deg_1 + deg_2 + 1)
            for i in range(deg_1 + 1):
                for j in range(deg_2 + 1):
                    ans[i+j] += self.coefficients[i] * other.coefficients[j]
            return Polynomial(tuple((ans)))

        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        return -1 * (self-other)
    
    def __pow__(self, other):
        a = self
        if isinstance(other, Integral):
            if other == 0:
                return Polynomial((1,))
            else:
                for i in range(other-1):
                    a = a*self
                return a
        else:
            return NotImplemented
    
    def __call__(self, other):
        a = 0
        for i in range(Polynomial.degree(self) + 1):
            if self.coefficients[i]>0:
                a += self.coefficients[i] * other ** i
            if self.coefficients[i]<0:
                a -= self.coefficients[i] * other ** i
        return a

    def dx(self):
        a = list(self.coefficients)
        x = Polynomial((0,1))
        ans = Polynomial((0,))

        for i in range(Polynomial.degree(self)):
            ans = ans + a[i+1] * (i+1) * x ** i
        return ans 

def derivative(p):
    return p.dx()

