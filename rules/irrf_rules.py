def calculate_irrf(base_irrf):
    if base_irrf <= 2112.00:
        return 0
    elif base_irrf <= 2826.65:
        return (base_irrf * 0.075) - 169.44
    elif base_irrf <= 3751.05:
        return (base_irrf * 0.15) - 381.44
    elif base_irrf <= 4664.68:
        return (base_irrf * 0.225) - 662.77
    return (base_irrf * 0.275) - 896.00