def step1():

    print('Выбираем тему тимбилдинга')
    print('Тебе нравится проводить время со своей командой?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2()
    else:
        print('Ты предпочел(ла) остаться дома')


def step2():

    print(
        'Ты любишь страшные квесты?'
         )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step4()
    else:
        return step3()


def step3():

    print(
        'А может все-таки да, вся твоя команда их любит?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step4()
    else:
        print('игра окончена')


def step4():

    print(
        'Поздравляю, вы идете на хоррор перфоманс!'
    )


if __name__ == '__main__':
    step1()
