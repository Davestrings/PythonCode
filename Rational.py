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
    def __init__(self, numer, denomer):
        self.numerator = numer
        self.denominator = denomer

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        """ Add two rational numbers """
        the_lcm = lcm(self.denominator, other.denominator)

        numerator_sum = (self.numerator * the_lcm / self.denominator) + \
                        (other.numerator * the_lcm / other.denominator)
        return Rational(int(numerator_sum), the_lcm)

    def __sub__(self, other):
        """Subtract two rational number"""
        the_lcm = lcm(self.denominator, other.denominator)

        numerator_sum = (self.numerator * the_lcm / self.denominator) - \
                        (other.numerator * the_lcm / other.denominator)
        return Rational(int(numerator_sum), the_lcm)


def main():
    one_fifth = Rational(1, 5)
    print(one_fifth)
    two_seventh = Rational(2, 7)
    print(two_seventh)
    print(one_fifth.__add__(two_seventh))
    print(one_fifth.__sub__(two_seventh))


main()

