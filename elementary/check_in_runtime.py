from elementary.repeat_ex import repeat


def main():
    name = 'Anne'
    if name == 'Guido':
        print(repeeeet(name, False) + '!!!')
    else:
        print(repeat(name, False))


if __name__ == '__main__':
    main()