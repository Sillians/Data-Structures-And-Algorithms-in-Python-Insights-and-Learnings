# Steps:
# 1. Parse the polynomial: you need to have a predefined pattern. The more "untrusted" or "wild" the input is,
# the better you will have to parse it. You could use regular expressions.
# 2. Have the basic components of the equation (coeff, power_of_x) list.
# 3. Do the math (derivative formula)
# 4. Return an equation the way the input was given.


import re

class FirstDerivativePolynomial:
    def __init__(self, polynomial_equation):
        self._polynomial_equation = polynomial_equation
        self.equation_map = []

    def split_equation(self):
        terms = self._polynomial_equation.split('+')
        equation = [re.split(r'x\^?', t) for t in terms]
        return equation

    def map_equation(self):
        equation = self.split_equation()
        for e in equation:
            try:
                coefficient = int(e[0])
            except ValueError:
                coefficient = 1
            try:
                exponent = int(e[1])
            except ValueError:
                exponent = 1
            except IndexError:
                exponent = 0
            self.equation_map.append((coefficient, exponent))
        return self.equation_map

    def str_exponent(self, p):
        if p == 0:
            return ''
        elif p == 1:
            return 'x'
        else:
            return 'x^%d' % (p,)

    def str_coefficient(self, c):
        return '' if c == 1 else str(c)

    def write(self, equation_):
        str_terms = [(self.str_coefficient(c) + self.str_exponent(p)) for c,p in equation_]
        return "+".join(str_terms)

    def first_derivative(self):
        equation_mapping = self.map_equation()
        derivative_mapping = [(p*c, p-1) for c, p in equation_mapping[:-1]]
        return self.write(derivative_mapping)

    def main(self):
        print(self._polynomial_equation, '->', self.first_derivative())


if __name__ == "__main__":
    eqn = "12x^3 + 8x^2 + 3x + 6"
    first_derivative = FirstDerivativePolynomial(eqn)
    first_derivative.main()
