def policz_bmi(masa, wzrost):
    wzrost_m = wzrost / 100
    try:
        bmi = masa / (wzrost_m**2)
    except Exception as e:
        print(e)
        return -1
    return round(bmi, 2)
