def max_profit(N, S, cargo):
    # тут мы сортируем данные чтобы сначала шли более тяжелые
    sorted_cargo = sorted(cargo, key=lambda x: x[1], reverse = True)
    # тут мы уже сортируем грузы так чтобы сначала шли грузы с большей удельной
    # стоимостью, если два груза имеют равную удельную стоимость то за счёт строки 3
    # выше приоритет будут иметь более объёмные грузы
    sorted_cargo = sorted(sorted_cargo, key=lambda x: x[0] / x[1], reverse=True)
    max_cost = 0
    max_vol = 0
    total_volume = 0
    total_profit = 0

    for c in sorted_cargo:
        cost, volume = c
        # можно заметить что если объём грузов уже в отсеке + новый груз больше
        # объёма отсека то мы не заканчиваем погрузку а продолжаем смотереть грузы
        # потому что свободное место для менее выгодного ещё могло остаться
        if total_volume + volume <= S:
            total_volume += volume
            total_profit += cost
            # запоминаем объём самого дорого груза
            if max_cost < cost:
                max_cost = cost
                max_vol = volume
            elif max_cost == cost:
                max_vol = max(max_vol, volume)

    return (total_profit, max_vol)


if __name__ == '__main__':
    with open("input.txt", "r") as file:
        N, S = map(int, file.readline().split())
        cargo = [tuple(map(int, line.split())) for line in file]

    result, max_vol = max_profit(N, S, cargo)
    print(int(result * 0.2), max_vol)


