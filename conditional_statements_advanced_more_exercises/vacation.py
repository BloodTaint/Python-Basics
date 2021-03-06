# 5.	Ваканция
# Напишете програма, която спрямо даден бюджет и сезон да пресмята цената, локацията и мястото на настаняване за ваканция.
# Сезоните са лято и зима – "Summer" и "Winter". Локациите са – "Alaska" и "Morocco".
# Възможните места за настаняване – "Hotel", "Hut" или "Camp".
#


# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
# •	Втори ред –  Сезон – текст "Summer" или "Winter"
# Изход
# На конзолата трябва да се отпечатат един ред.
# "{локацията} – {мястото за настаняване} – {цената}"
# Цената трябва да е форматирана до вторият знак след десетичната запетая.
budget = float(input())
seasons = input()
location = ''
accommodation = ''
price = 0
# •	При бюджет по-малък или равен от 1000лв.:
# o	Настаняване в "Camp"
# o	Според сезона локацията ще е една от следните и ще струва определен процент от бюджета:
# 	Лято – Аляска – 65% от бюджета
# 	Зима – Мароко – 45% от бюджета
if budget <= 1000:
    accommodation = "Camp"
    if seasons == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif seasons == "Winter":
        location = "Morocco"
        price = budget * 0.45
# •	При бюджет по-голям от 1000лв. и по-малък или равен от 3000лв.:
# o	Настаняване в "Hut"
# o	Според сезона локацията ще е една от следните и ще струва определен процент от бюджета:
# 	Лято – Аляска – 80% от бюджета
# 	Зима – Мароко – 60% от бюджета
elif budget <= 3000:
    accommodation = "Hut"
    if seasons == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif seasons == "Winter":
        location = "Morocco"
        price = budget * 0.60
# •	При бюджет по-голям от 3000лв.:
# o	Настаняване в "Hotel"
# o	Според сезона локацията ще е една от следните и ще струва 90% от бюджета:
# 	Лято – Аляска
# 	Зима – Мароко
elif budget > 3000:
    accommodation = "Hotel"
    if seasons == "Summer":
        location = "Alaska"
        price = budget * 0.90
    elif seasons == "Winter":
        location = "Morocco"
        price = budget * 0.90
print(f'{location} - {accommodation} - {price:.2f}')