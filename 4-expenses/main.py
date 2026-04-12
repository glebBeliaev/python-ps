weak_expenses = [400, 500, 350, 660, 1240, 235, 555]

sum_expenses = sum(weak_expenses)
average_expenses = sum_expenses / len(weak_expenses)
max_expenses = max(weak_expenses)
min_expenses = min(weak_expenses)

data_expenses = (min_expenses, max_expenses, sum_expenses)

print(data_expenses)
