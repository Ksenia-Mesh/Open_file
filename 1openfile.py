def get_dict():
    cook_book = {}
    with open('recipe book', encoding='utf-8') as f:
        for name in f:
            dish = name.strip()
            count = int(f.readline())
            d = list()
            for h in range(count):
                product = {}
                ing = f.readline().strip()
                product['ingredient_name'], product['quantity'], product['measure'] = ing.split('|')
                d.append(product)
            f.readline()
            cook_book[dish] = d
    return cook_book

print(f'cook_book: \n{get_dict()}')


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_dict()
    order_dish = {}
    for dish in dishes:
        if dish in cook_book:
            for dishe_1 in cook_book[dish]:
                mean_quan = {}
                if dishe_1 ['ingredient_name'] not in order_dish:
                    mean_quan['measure'] = dishe_1['measure']
                    mean_quan['quantity'] = int(dishe_1['quantity']) * person_count
                    order_dish[dishe_1['ingredient_name']] = mean_quan
                else:
                    order_dish[dishe_1['ingredient_name']]['quantity'] = order_dish[dishe_1['ingredient_name']]['quantity'] + int(dishe_1['quantity'])* person_count

        else:
            print('Not dishes')
    return order_dish


print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))

