# 9.	Лява и дясна сума
# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя,
# и проверява дали сумата на първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума).

# При равенство печата " Yes, sum = " + сумата; иначе печата " No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).
# Примерен вход и изход
# вход	    изход	         коментар
# 2
# 10
# 90
# 60
# 40	 Yes, sum = 100	      10+90 = 60+40 = 100

# 2
# 90
# 9
# 50
# 50	No, diff = 1	       90+9 ≠ 50+50
#                              Difference = |99-100| = 1
numbers = int(input())
one = 0
two = 0
for i in range(numbers):
    sum = int(input())
    one += sum

for i in range(numbers):
    sum = int(input())
    two += sum
total = abs(one - two)
if one == two:

    print(f'Yes, sum = {one}')
else:
    print(f'No, diff = {total}')
