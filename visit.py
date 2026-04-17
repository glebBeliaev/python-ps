# подсчитать для каждого дня всего визитов и уникальных
# найти ID тех кто посетил оба дня
# найти ID тех кто посетил только первый день
# найти ID тех кто посетил только второй день
# найти ID тех кто был только раз
visitors_day1 = [101, 102, 103, 101, 104, 102, 105, 101]
visitors_day2 = [101, 108, 100, 101, 105, 107]

unique_visitors_day1 = set(visitors_day1)
unique_visitors_day2 = set(visitors_day2)

print(
    "Всего визитов:",
    len(visitors_day1) + len(visitors_day2),
    "уникальных:",
    len(unique_visitors_day1) + len(unique_visitors_day2),
)

print("Оба дня:", unique_visitors_day1 & unique_visitors_day2)
print("Только первый день:", unique_visitors_day1.difference(unique_visitors_day2))
print("Только второй день:", unique_visitors_day2.difference(unique_visitors_day1))
print(
    "Только один день:", unique_visitors_day1.symmetric_difference(unique_visitors_day2)
)
