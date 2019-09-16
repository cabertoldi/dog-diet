from diet import Diet

def get_diet(params):
    factor = params['factor']
    pounds_per_month = params['pounds_per_month']
    minimum_price = params['minimum_price'] if 'minimum_price' in params else Diet.minimum_price
    maximum_price = params['maximum_price'] if 'maximum_price' in params else Diet.maximum_price

    diet = Diet(factor, pounds_per_month, minimum_price, maximum_price)

    return {
        'factor': diet.factor,
        'calories': diet.calories(),
        'unit_price': diet.unit_price(),
        'total_price': diet.total_price(),
    }
