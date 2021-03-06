# Задача 2. Семейна почивка
# Вашата задача е да напишете програма, която да
# изчислява дали предвидения от тях бюджет ще им стигне, като знаете колко нощувки са планирали, каква е
# цената за нощувка и колко процента от бюджета са предвидили за допълнителни разходи. Трябва да се има
# предвид, че ако броят на нощувките е по-голям от 7, цената за нощувка се намаля с 5%.

# От конзолата се четат 4 реда:
#  Бюджетът, с който разполагат – реално число в интервала [1.00 … 10000.00]
#  Брой нощувки – цяло число в интервала [0 … 1000]
#  Цена за нощувка – реално число в интервала [1.00 … 500.00]
#  Процент за допълнителни разходи – цяло число в интервала [0 … 100]

# Отпечатването на конзолата зависи от резултата:
#  Ако сумата е достатъчна:
# o "Ivanovi will be left with {останали пари след почивката} leva after vacation."
#  Ако НЕ е достигната сумата:
# o "{парите нужни до достигане на целта} leva needed."
# Сума трябва да се форматира до втората цифра след десетичния знак.

budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
additional_costs = int(input())

if number_of_nights > 7:
    price_per_night *= 0.95
need_money = ((number_of_nights * price_per_night) + (budget * (additional_costs/100)))
total = abs(need_money - budget)
if need_money <= budget:
    print(f"Ivanovi will be left with {total:.2f} leva after vacation.")
elif need_money > budget:
    print(f"{total:.2f} leva needed.")
