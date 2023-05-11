from pprint import pprint

def country_russia(visits):
    country_list = []
    for visit in visits:
        for country in visit.values():
            if 'Россия' in country:
                country_list.append(visit)
    return country_list


def ids_values(ids):
    val_ = list(set(sum(ids.values(), [])))
    return val_


# def max_volume(stats):
#     for k in stats.keys():
#         if stats[k] == max(stats.values()):
#             return k

def max_stats(stats):
    firma_d = {firma: turn for firma, turn in stats.items() if turn == max(stats.values())}
    return firma_d


geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


if __name__ == '__main__':
    pprint(country_russia(geo_logs))
    print(ids_values(ids))
    # print(max_volume(stats))
    print(max_stats(stats))