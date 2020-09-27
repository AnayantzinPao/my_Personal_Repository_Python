def read_file():
    counter = 0
    with open('aleph.txt',encoding='utf-8') as f:
        for line in f:
            counter += line.count('Beatriz')

    print('Beatriz se encuentra {} en el texto'.format(counter))

def write_file():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

def run():
    read_file()
    #write_file()


if __name__ == '__main__':
    run()