path = []
file = open('input.txt', 'r')
for line in file:
    entry = line.rstrip('\n').split(' ')
    path.append(entry)

y = 0
z = 0
for movement in path:
    if movement[0] == 'forward':
        y += int(movement[1])
    elif movement[0] == 'down':
        z += int(movement[1])
    else:
        z -= int(movement[1])

answer = z * y
print(answer)
