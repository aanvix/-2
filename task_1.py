money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
sum_ = money_capital+salary
month = 0
while sum_ >= spend:
        sum_ = sum_ - spend + salary
        spend = spend + spend* increase
        month += 1

print("Количество месяцев, которое можно протянуть без долгов:",month)

