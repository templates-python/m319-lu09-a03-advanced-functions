"""Division exercise: compute quotient and remainder."""


def div(dividend, divisor):
    """
    Performs integer division.
    :param dividend: int
    :param divisor: int
    :return: Tuple (result of division, remainder) or None if divisor is zero
    """
    if divisor == 0:
        print('Division durch Null ist nicht erlaubt')
        return None
    result = dividend // divisor
    rest = dividend % divisor
    return result, rest


def main():
    result, rest = div(34, 6)
    print(...)


if __name__ == '__main__':
    main()
