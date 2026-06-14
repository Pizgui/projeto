n = c = 0
while True:
    n = int(input('Quer saber a tabuada de qual número? '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1,11):
        print(f'{n} * {c} = {n*c}')
    print('-' * 30)