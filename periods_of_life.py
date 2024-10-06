def periods_of_life(age=1):
    try:
        if age < 2:
             period = 'baby'
        elif age >= 2 and age < 4:
            period = 'kid'
        elif age >= 4 and age < 13:
            period = 'child'
        elif age >= 13 and age < 20:
            period = 'teenager'
        elif age >= 20 and age < 65:
            period = 'adult'
        elif age >= 65:
            period = 'old man'
    except TypeError:
        period = 'unknown information'

    print(f"{age} - {period}")

ages = [1, 2, 3, 4, 12, 13, 19, 20, 64, 65, 70, 'hello']
for age in ages:
    periods_of_life(age)