# Фирма получава заявка за изработването на проект, за който са необходими определен брой часове.
# Фирмата разполага с определен брой дни. През 10% от дните служителите са на обучение и не могат да работят по проекта.
# Един нормален работен ден във фирмата е 8 часа.
# Всеки служител може да работи по проекта в извънработно време по 2 часа на ден.
# Часовете трябва да са закръглени към по-ниско цяло число (Например –> 6.98 часа се закръглят на 6 часа).
# Напишете програма, която изчислява дали фирмата може да завърши проекта навреме и колко часа не достигат или остават.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# •	На първия ред са необходимите часовете – цяло число в интервала [0 ... 200 000]
# •	На втория ред са дните, с които фирмата разполага – цяло число в интервала [0 ... 20 000]
# •	На третия ред е броят на служителите, работещи извънредно – цяло число в интервала [0 ... 200]
import math

hours = int(input())
days = int(input())
numbers_of_workers = int(input())
extra_hours = (numbers_of_workers * 2) * days
hours_sum = (8 * 0.90) * days
total_hours = abs(hours -(extra_hours + hours_sum) )
# print(hours_sum)
# print(extra_hours)
# print(total_hours)

if hours <= (extra_hours + hours_sum) :
    print(f'Yes!{math.ceil(total_hours)} hours left.')
else:
# •	Ако  времето НЕ Е достатъчно:
    print(f'Not enough time!{math.ceil(total_hours)} hours needed.')
