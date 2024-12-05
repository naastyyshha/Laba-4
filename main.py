backpack = {'r':[3,25],
             'p':[2,15],
             'a':[2,15],
             'm':[2,20],
             'i':[1,5],
             'k':[1,15],
             'x':[3,20],
             't':[1,25],
             'f':[1,15],
             'd':[1,10],
             's':[2,20],
             'c':[2,20]}

capacity = 9
bag = []
points = 15
weight = 0

def get_the_worth_of_stuff(backpack):
    for item in backpack:
        worth = backpack[item][1] / backpack[item][0]
        backpack[item].append(worth)
    return backpack

def get_selected_items_list(backpack, capacity, weight, points):
    backpack =get_the_worth_of_stuff(backpack)
    sorted_backpack = dict(sorted(backpack.items(), key=lambda x: (x[1][2], x[1][0]), reverse=True))
    print(sorted_backpack)
    for item in sorted_backpack:
        if weight + sorted_backpack[item][0] <= capacity:
            weight += sorted_backpack[item][0]
            for i in range(sorted_backpack[item][0]):
                bag.append(item)
            points += sorted_backpack[item][1]
        else:
            points -= sorted_backpack[item][1]

    for i in range(0, len(bag), 3):
        print(f"[{bag[i]}],[{bag[i + 1]}],[{bag[i + 2]}]")
    return f'Итоговые очки выживания: {points}'

print(get_selected_items_list(backpack, capacity, weight, points))
