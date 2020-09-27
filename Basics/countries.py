countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

def run():
    while True:
        country = str(input('Write name of a country: ')).lower()

        try:
            print('The population of {} is: {} millions'.format(country, countries[country]))
        except KeyError:
            print('We does not have the population of {}'.format(country))
            seguir = str(input('Do you want to add it ? [y]es [n]o'))

            if seguir == 'y':
                new_country(country)
            else:
                break


def new_country(country):
    new_country = str(input('Write population of: {} :'.format(country))).lower()
    countries[country] = new_country
    print('Country was added correctly: ')
    print(countries)

if __name__ == '__main__':
    run()