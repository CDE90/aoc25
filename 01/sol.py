inp = open("01/inp.txt").read().strip().split("\n")

val = 50
count = 0

for line in inp:
    left = line.startswith("L")
    number = int(line[1:])
    if left:
        val = (val - number) % 100
    else:
        val = (val + number) % 100

    if val == 0:
        count += 1

print(count)


count2 = 0
val = 50


for line in inp:
    left = line.startswith("L")
    number = int(line[1:])

    for _ in range(number):  # Simulate each click
        if left:
            val = (val - 1) % 100
        else:
            val = (val + 1) % 100

        if val == 0:
            count2 += 1

print(count2)
