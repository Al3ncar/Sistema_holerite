from utils.inss_calculator import calculate_inss_discount


def identify_inss_range(salary):
    if salary <= 1412.00:
        return calculate_inss_discount(1, salary)

    if salary <= 2666.68:
        return calculate_inss_discount(2, salary)

    if salary <= 4000.03:
        return calculate_inss_discount(3, salary)

    if salary <= 7786.02:
        return calculate_inss_discount(4, salary)

    return calculate_inss_discount(5, salary)
