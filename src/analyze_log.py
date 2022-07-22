import csv


def maria_favorites_plates(orders_list):
    all_marias_plates = {}

    return all_marias_plates


def many_times_arnaldo_asked():
    raise NotImplementedError


def which_plates_joao_never_asked():
    raise NotImplementedError


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
            return maria_favorites

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
