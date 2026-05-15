FIRST_RANGE = 1412.00 * 0.075


def calculate_inss_discount(quantity_range, salary):
    ranges = {
        1: range_1,
        2: range_2,
        3: range_3,
        4: range_4,
        5: range_5,
    }

    return ranges[quantity_range](salary)


def range_1(salary):
    return salary * 0.075


def range_2(salary):
    return FIRST_RANGE + (salary - 1412.00) * 0.09


def range_3(salary):
    range_2_value = (2666.68 - 1412.00) * 0.09
    range_3_value = (salary - 2666.68) * 0.12

    return FIRST_RANGE + range_2_value + range_3_value


def range_4(salary):
    range_2_value = (2666.68 - 1412.00) * 0.09
    range_3_value = (4000.03 - 2666.68) * 0.12
    range_4_value = (salary - 4000.03) * 0.14

    return (
        FIRST_RANGE
        + range_2_value
        + range_3_value
        + range_4_value
    )


def range_5(_salary):
    range_2_value = (2666.68 - 1412.00) * 0.09
    range_3_value = (4000.03 - 2666.68) * 0.12
    range_4_value = (7786.02 - 4000.03) * 0.14

    return (
        FIRST_RANGE
        + range_2_value
        + range_3_value
        + range_4_value
    )