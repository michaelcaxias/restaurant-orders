import csv


def maria_favorites_plates(orders_list):
    plates = {}

    for name, order, _day in orders_list:
        if name == 'maria':
            if order not in plates:
                plates[order] = 1
            else:
                plates[order] += 1

    # key necessário para
    # https://pythonguides.com/python-find-max-value-in-a-dictionary

    favorite_plate = max(plates, key=plates.get)

    return favorite_plate


def many_times_arnaldo_asked_hamburguer(orders_list):
    hamburgers_count = 0

    for name, order, _day in orders_list:
        if name == 'arnaldo' and order == 'hamburguer':
            hamburgers_count += 1

    return hamburgers_count


def which_plates_joao_never_asked(orders_list):
    foods = set()
    foods_of_john = set()

    for name, order, _day in orders_list:
        foods.add(order)
        if name == 'joao':
            foods_of_john.add(order)

    return foods.difference(foods_of_john)


def which_days_did_joao_never_go_to_the_cafeteria():
    raise NotImplementedError


def analyze_log(path_to_file):
    if not path_to_file.endswith('csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as file:
            file_reader = csv.reader(file, delimiter=",", quotechar='"')
            orders_list = [order for order in file_reader]

            maria_favorites = maria_favorites_plates(orders_list)
            quantity_hamburguers = many_times_arnaldo_asked_hamburguer(orders_list)
            plates_never_asked = which_plates_joao_never_asked(orders_list)

            content = [
                f"{maria_favorites}\n",
                f"{quantity_hamburguers}\n",
                f"{plates_never_asked}\n"
            ]

        with open('data/mkt_campaign.txt', 'w') as file:
            file.writelines(content)
            file.close()

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
