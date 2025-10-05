text = input("Enter: ")
golosni = ['a','e','i','o','u']
count = [['a', 0],['e', 0],['i', 0],['o', 0],['u', 0]]
for ch in text:
    if ch.lower() == golosni[0]:
        count[0][1] += 1
    if ch.lower() == golosni[1]:
        count[1][1] += 1
    if ch.lower() == golosni[2]:
        count[2][1] += 1
    if ch.lower() == golosni[3]:
        count[3][1] += 1
    if ch.lower() == golosni[4]:
        count[4][1] += 1

print(f'A:{count[0][1]} E:{count[1][1]} I:{count[2][1]} O:{count[3][1]} U:{count[4][1]}')