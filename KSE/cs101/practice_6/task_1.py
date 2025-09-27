text = input("Enter: ")
golosni = ['q','o','e','y','i']
count_q = 0
count_o = 0
count_e = 0
count_y = 0
count_i = 0
for ch in text:
    if ch.lower() == golosni[0]:
        count_q+=1
    if ch.lower() == golosni[1]:
        count_o+=1
    if ch.lower() == golosni[2]:
        count_e+=1
    if ch.lower() == golosni[3]:
        count_y+=1
    if ch.lower() == golosni[4]:
        count_i+=1

print(f'Q:{count_q} O:{count_o} E:{count_e} Y:{count_y} I:{count_i}')