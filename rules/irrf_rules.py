def calculate_irrf(base_irrf):
    if base_irrf <= 2112.00:
        return 0.0

    if base_irrf <= 2826.65:
        return base_irrf * 0.075 - 158.40

    if base_irrf <= 3751.05:
        return base_irrf * 0.15 - 370.40

    if base_irrf <= 4664.68:
        return base_irrf * 0.225 - 651.73

    return base_irrf * 0.275 - 884.96