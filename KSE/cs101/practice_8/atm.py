import random
money = [20,50,100,200,500,1000]
atm = []
length = random.randint(1,10)
n = 1
while n <= length:
    atm.append(money[random.randint(0, 5)])
    n+=1
print(atm)
withdraw = int(input('How much many you wanna withdraw?>>>'))
to_give = []
func_sum = 0
for ch in sorted(atm, reverse=True):
    if func_sum + ch <= withdraw:
        to_give.append(ch)
        func_sum+=ch
    if func_sum == withdraw:
        print('You can withdraw money')
        print(f'You will get {to_give}')
        for bill in to_give:
            if bill in atm:
                atm.remove(bill)
        print(f'Left {atm}')
        exit()
print("You can't withdraw")