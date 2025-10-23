magaz = {
    'bread': 15,
    'cola': 25,
    'milk': 48,
    'sausage': 220,
    'mivina': 17
}

bought = {}
total = 0

while True:
    ask = input('What do you want to buy?: ')
    if ask == 'Paka':
        print(f'Your total sum: {total}')
        print(f'You bought: {bought}')
        break
    if ask not in magaz:
        print('No such item, try again.')
        continue
    bought[ask] = magaz[ask]
    total += magaz[ask]
    print('You bought:', bought)
    print('Total price:', total)
