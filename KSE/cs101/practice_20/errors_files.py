import random

def slot():
    a = [1,2,3,4,5,6,7]
    combination = []
    for x in range(3):
         combination.append(random.choice(a))
    print(combination)
    return combination

def check_if_win(data: list):
    bank = {}.fromkeys([1,2,3,4,5,6,7], 0)
    k = 1
    for x in bank:
        bank[x] += k + 1
        k +=1
    if len(set(data)) == 1:
        return True, bank[data[0]]
    else:
        return False, 0


def amount(if_win, bet, k):
    if if_win == True:
        return bet * k
    else:
        return bet * -1

all_money = 1000
while True:
    bet = int(input('Bet: '))
    data = check_if_win(slot())
    all_money += amount(data[0],bet,data[1])
    print(f'Account: {all_money}')