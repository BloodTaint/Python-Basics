# 6.	Шофьор на ТИР
# Напишете програма която пресмята колко пари ще изкара шофьор на ТИР за един сезон.
# На входа програмата получава през кой сезон ще работи шофьора, както и колко километра на месец ще кара.
# Един сезон е 4 месеца. Според зависи сезона и броя километри на месец ще му се заплаща различна сума на километър:
#
# 	    							Пролет/Есен			Лято			Зима
# км на месец <= 5000				0.75 лв./км		0.90 лв./км		1.05 лв./км
# 5000 < км на месец <= 10000		0.95 лв./км		1.10 лв./км		1.25 лв./км
# 10000 < км на месец <= 20000	1.45 лв./км – за който и да е сезон
#
# След като са извадени 10% за данъци се отпечатват останалите пари.

# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – Сезон – текст "Spring", "Summer", "Autumn" или "Winter"
# •	Втори ред –  Километри на месец – реално число в интервала [10.00...20000.00]
# Изход
# На конзолата трябва да се отпечатат едно число:
seasons = input()
km_in_month = float(input())
salary = 0
if km_in_month <= 5000:
    if seasons == "Spring" or seasons == "Autumn":
        salary = km_in_month * 0.75
    elif seasons == "Summer":
        salary = km_in_month * 0.90
    elif seasons == "Winter":
        salary = km_in_month * 1.05
elif km_in_month <= 10000:
    if seasons == "Spring" or seasons == "Autumn":
        salary = km_in_month * 0.95
    elif seasons == "Summer":
        salary = km_in_month * 1.10
    elif seasons == "Winter":
        salary = km_in_month * 1.25
else:
    salary = km_in_month * 1.45
print(f'{((salary * 4)* 0.90):.2f}')


