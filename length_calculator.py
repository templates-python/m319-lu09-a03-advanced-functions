"""Converts lengths between meters, miles, nautical miles, yards and inches."""


def convert(length, from_unit, to_unit):
    """
    Converts lengths. The following lengths can be converted: meters, miles, nautical miles, yards, inches
    :param length: length to convert
    :param from_unit: 1=Meter, 2=Meilen, 3=Seemeilen, 4=Yard, 5=Inches
    :param to_unit: 1=Meter, 2=Meilen, 3=Seemeilen, 4=Yard, 5=Inches
    :return: converted length
    """
    if from_unit == 1:
        result = length
    elif from_unit == 2:
        result = length * 1609.34
    elif from_unit == 3:
        result = length * 1852.0
    elif from_unit == 4:
        result = length * 0.9144
    elif from_unit == 5:
        result = length * 0.0254

    if to_unit == 1:
        return result
    if to_unit == 2:
        result = result / 1609.34
        return result
    if to_unit == 3:
        result = result / 1852.0
        return result
    if to_unit == 4:
        result = result / 0.9144
        return result
    if to_unit == 5:
        result = result / 0.0254
        return result


def main():
    print('1=Meter, 2=Meilen, 3=Seemeilen, 4=Yard, 5=Inches')
    print(convert(1, 1, 4))


if __name__ == '__main__':
    main()
