

def calc_price(minutes, cloth_type):
    data = {'F3': 3.13, 'G3': 6.45, 'H3': 12.0, 'I3': 85.58, 'J3': 354.47}

    cloth_type_lower = cloth_type.lower()

    cloth_prices = {
        'футболка': 1000,
        'кепка': 500,
        'худи': 1750,
        'свитшот': 1750,
        'толстова': 2500
    }

    price = (minutes/60)*(data['F3']+data['G3']+data['H3']) + data['I3']+data['J3'] + (minutes/60)*cloth_prices[cloth_type_lower]

    return round(price, 2), round(price * 1.7, 2), round(price * 2.5, 2)
