def make_car(automobile_manufacturer, car_model, **kwargs):
    """Creating a dictionary"""
    kwargs['automobile_manufacturer'] = automobile_manufacturer
    kwargs['car_model'] = car_model

    

    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)