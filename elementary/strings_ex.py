def main():

    value = 2.791514
    print(f'approximate value = {value:.2f}')

    car = {'tires':4, 'doors':2}
    print(f'car = {car}')

    address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
                    {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
                    {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]

    for person in address_book:
        print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')

    time_hour = 1
    mood = 'sleepy'

    if time_hour >= 0 and time_hour <= 24:
        print('Suggesting a drink option...')
    if mood == 'sleepy' and time_hour < 10:
        print('coffee')
    elif mood == 'thirsty' or time_hour < 2:
        print('lemonade')
    else:
        print('water')

if __name__ == '__main__':
    main()