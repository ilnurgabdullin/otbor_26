def maximize_duration_and_remain_budget(A, performers):
    # Сначала отделяем докладчиков от музыкантов
    speakers = [performer for performer in performers if performer[2] == 'D']
    musicians = [performer for performer in performers if performer[2] == 'M']
    # Сортируем по возрастанию стоимости выступления за минуту
    speakers.sort(key=lambda x: x[0])
    musicians.sort(key=lambda x: x[0])
    # Приглашаем докладчиков на максимальную длительность, пока есть бюджет
    total_duration = 0
    total_cost = 0
    for speaker in speakers:
        cost_per_minute, max_duration, _ = speaker
        # Проверяем хватит ли на полное выступление
        if max_duration * cost_per_minute <= A:
            total_duration += max_duration
            A -= max_duration * cost_per_minute
        # Если не хватает берем только часть
        else:
            dur = A // cost_per_minute
            total_duration += dur
            A -= dur * cost_per_minute
            return total_duration, A

    # Если есть оставшийся бюджет, приглашаем музыкантов
    for musician in musicians:
        cost_per_minute, max_duration, _ = musician
        if max_duration * cost_per_minute <= A:
            total_duration += max_duration
            A -= max_duration * cost_per_minute
        else:
            dur = A // cost_per_minute
            total_duration += dur
            A -= dur * cost_per_minute
            return total_duration, A

    return total_duration, A


# Пример входных данных
if __name__ == '__main__':
    performers = []
    with open("input2.txt", "r") as file:
        N, A = map(int, file.readline().split())
        for _ in range(N):
            cost_per_minute, max_duration, performer_type = file.readline().split()
            performers.append((int(cost_per_minute), int(max_duration), performer_type))

    # Получаем результат и выводим его
    result = maximize_duration_and_remain_budget(A, performers)
    print(result[0], result[1])
