def gcd(bigger, smaller):
    """
    calculate the greatest common divisor of two numbers

1.  If one of the numbers is 0, return the other number and halt.
2. Otherwise, find the integer remainder of the larger number divided by the smaller
number.
3. Reapply the algorithm to the smaller number from the previous iteration and the
just-calculated remainder.
    :param bigger:
    :param smaller:
    :return:
    """
    if not bigger > smaller:
        bigger, smaller = smaller, bigger  # swap smaller for bigger
    while smaller != 0:
        remainder = bigger % smaller
        bigger, smaller = smaller, remainder  # swap smaller to bigger and remainder to smaller
    return bigger


def lcm(num_1, num_2):
    """
    calculate the lowest common multiple of two positive numbers
    :param num_1:
    :param num_2:
    :return:
    """
    return (num_1 * num_2) / gcd(num_1, num_2)


class Rational(object):
    def __init__(self, numer, denomer=1):
        self.numerator = numer
        self.denominator = denomer

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        """ Add two rational numbers. Allows int as a parameter """
        if type(other) == int:
            other = Rational(other)
        if type(other) == Rational:
            # find a common denominator
            the_lcm = lcm(self.denominator, other.denominator)
            #  multiply each by the lcm, then add
            numerator_sum = (self.numerator * the_lcm / self.denominator) + \
                            (other.numerator * the_lcm / other.denominator)
            return Rational(int(numerator_sum), the_lcm)
        else:
            print('wrong type')
            raise TypeError

    def __radd__(self, param):
        """ Add two Rationals (reversed)"""
        # mapping is reversed: if "1 + x", x maps to self, and 1 maps to f
        return self.__add__(param)

    def __sub__(self, other):
        """Subtract two rational number"""
        the_lcm = lcm(self.denominator, other.denominator)

        numerator_sum = (self.numerator * the_lcm / self.denominator) - \
                        (other.numerator * the_lcm / other.denominator)
        return Rational(int(numerator_sum), the_lcm)

    def reduce_rational(self):
        """Return the reduced fractional value as a Rational """
        the_gcd = gcd(self.numerator, self.denominator)
        return Rational(self.numerator // the_gcd, self.denominator // the_gcd)

    def __eq__(self, param_Rational):
        reduce_self = self.reduce_rational()
        reduced_param = param_Rational.reduce_rational()
        return (reduce_self.numerator == reduced_param.numerator) and \
               (reduce_self.denominator == reduced_param.denominator)


def main():
    one_fifth = Rational(1, 5)
    print(one_fifth)
    two_seventh = Rational(2, 7)
    print(two_seventh)
    print(one_fifth.__add__(two_seventh))
    print(one_fifth.__sub__(two_seventh))
    print(one_fifth.__eq__(two_seventh))
    print('\n')
    print(one_fifth + two_seventh)
    print(one_fifth + 5)
    print(5 + one_fifth)


main()
