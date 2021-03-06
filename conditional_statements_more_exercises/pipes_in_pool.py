# Басейн с обем V има две тръби от които се пълни.
# Всяка тръба има определен дебит (литрите вода минаващи през една тръба за един час).
# Работникът пуска тръбите едновременно и излиза за N часа. Напишете програма, която изкарва състоянието на басейна,
# в момента, когато работникът се върне.
# Вход
# От конзолата се четат четири реда:
# •	Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# •	Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# •	Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# •	Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]
# Изход
# Да се отпечата на конзолата едно от двете възможни състояния:
# •	До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
# o	"The pool is {запълненост на басейна в проценти}% full. " \
#      "Pipe 1: {процент вода от първата тръба}%. Pipe 2: {процент вода от втората тръба}%."
# Aко басейнът се е препълнил – с колко литра е прелял за даденото време.
# o	"For {часовете, които тръбите са пълнили вода} hours the pool overflows with {литрите вода в повече} liters."
v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
pool_occupancy_in_percent = (((p2 + p1) * h) / v) * 100
percentage_of_water_p1 = p1 / (p2 + p1) * 100
percentage_of_water_p2 = p2 / (p2 + p1) * 100
liters_of_water_in_excess = abs(((p1 + p2) * h) - v)
if ((p2 + p1) * h) <= v:
       print(f"The pool is {pool_occupancy_in_percent}% full. "
       f"Pipe 1: {percentage_of_water_p1}%. Pipe 2: {percentage_of_water_p2}%.")
else:
       print(f"For {h} hours the pool "
             f"overflows with {liters_of_water_in_excess} liters.")
