from rules.inss_rules import identify_inss_range
from rules.irrf_rules import calculate_irrf

employees = {}


def register_employee(name, role, dependents, gross_salary):
    if name in employees:
        return False

    employees[name] = {
        "role": role,
        "dependents": dependents,
        "gross_salary": gross_salary,
    }

    return True


def list_employees():
    return sorted(employees.keys())


def calculate_paycheck(employee_name):
    employee = employees[employee_name]

    gross_salary = employee["gross_salary"]
    dependents = employee["dependents"]

    inss = identify_inss_range(gross_salary)

    dependent_discount = dependents * 189.59

    base_irrf = gross_salary - inss - dependent_discount

    irrf = calculate_irrf(base_irrf)

    net_salary = gross_salary - inss - irrf

    fgts = gross_salary * 0.08

    return {
        "name": employee_name,
        "role": employee["role"],
        "gross_salary": gross_salary,
        "inss": inss,
        "irrf": irrf,
        "net_salary": net_salary,
        "fgts": fgts,
    }
