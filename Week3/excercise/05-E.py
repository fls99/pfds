from fractions import Fraction
rstr = input().replace(" ", "")
x = Fraction(rstr)
print(x.numerator)
print(x.denominator)
print(x)