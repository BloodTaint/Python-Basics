# Задача 1. Change бюро
# Преди време Петър си е купил биткойн. Сега ще ходи на екскурзия из Европа и ще му трябва евро.
# Освен биткойн има и китайски юанa. Той иска да обмени парите си в евро за екскурзията.
# Напишете програма, която да пресмята колко евро може да купи спрямо следните валутни курсове:
# •	1 биткойн = 1168 лева.
# •	1 китайски юан = 0.15 долара.
# •	1 долар = 1.76 лева.
# •	1 евро = 1.95 лева.
# Обменното бюро има комисионна от 0 до 5 процента от крайната сума в евро.
# Вход
# От конзолата се четат 3 числа:
# •	На първия ред – броят биткойни. Цяло число в интервала [0…20]
# •	На втория ред – броят китайски юана. Реално число в интервала [0.00… 50 000.00]
# •	На третия ред – комисионната. Реално число в интервала [0.00 ... 5.00]
# Изход
# На конзолата да се отпечата 1 число - резултатът от обмяната на валутите.
# Резултатът да се форматира до втората цифра след десетичната запетая.
number_of_bitcoin = int(input())
number_of_ioan = float(input())
fee = float(input())
bitcoin_lv = 1168
dollar_lv = 1.76
euro_lv = 1.95
ioan_lv = dollar_lv * 0.15

total = (number_of_bitcoin * bitcoin_lv) + (number_of_ioan * ioan_lv)
total /= euro_lv
total_fee = total * (fee/100)
total = total - total_fee
print(f'{total:.2f}')
