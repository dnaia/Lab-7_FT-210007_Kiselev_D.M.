k1 = 0  # Счетчик для проверки ввода цифр
l1 = 0  # Счетчик для проверки ввода цифр
m1 = 0  # Счетчик для проверки ввода цифр
n1 = 0  # Счетчик для проверки ввода цифр
f1 = 0  # Счетчик для проверки ввода цифр
s = 0  # Счетчик для проверки
s1 = 0  # Счетчик для проверки
s2 = 0  # Счетчик для проверки
differences = ''


# Всевозможные ходы слона
def elephant(ke, le, me, ne):
    spisokdanger_upleftd_vert = []
    spisokdanger_upleftd_goriz = []
    elephant_spisok = []
    opponent_spisok = []
    mestock = me
    nestock = ne
    kehelp = ke
    lehelp = le
    kehelp2 = ke
    lehelp2 = le
    kehelp3 = ke
    lehelp3 = le
    while ke <= 8 and le >= 1:  # Влево вверх диаг  # Влево вверх и Вправо вниз диаг | Формируется список опасноснтей для фигуры оппонента
        ke = ke + 1
        le = le - 1
        if ke == 9 or le == 0:
            break
        spisokdanger_upleftd_vert.append(ke)  # Список вертикальных опасностей
        spisokdanger_upleftd_goriz.append(le)  # Список горизонталей опасностей
        elephant_spisok.append(ke)
        elephant_spisok.append(le)

    while kehelp >= 1 and lehelp <= 8:  # Вправо вниз диаг
        kehelp = kehelp - 1
        lehelp = lehelp + 1
        if kehelp == 0 or lehelp == 9:
            break
        spisokdanger_upleftd_vert.append(kehelp)  # Список вертикальных опасностей
        spisokdanger_upleftd_goriz.append(lehelp)  # Список горизонталей опасностей
        elephant_spisok.append(kehelp)
        elephant_spisok.append(lehelp)

    spisokdanger_uprightd_vert = []
    spisokdanger_uprightd_goriz = []

    while kehelp2 <= 8 and lehelp2 <= 8:  # Вправо вверх диаг
        kehelp2 = kehelp2 + 1
        lehelp2 = lehelp2 + 1
        if kehelp2 == 9 or lehelp2 == 9:
            break
        spisokdanger_uprightd_vert.append(kehelp2)  # Список вертикальных угроз
        spisokdanger_uprightd_goriz.append(lehelp2)  # Список горизонтальных угроз
        elephant_spisok.append(kehelp2)
        elephant_spisok.append(lehelp2)

    while kehelp3 >= 1 and lehelp3 >= 1:  # Влево вниз диаг
        kehelp3 = kehelp3 - 1
        lehelp3 = lehelp3 - 1
        if kehelp3 == 0 or lehelp3 == 0:
            break
        spisokdanger_uprightd_vert.append(kehelp3)  # Список вертикальных угроз
        spisokdanger_uprightd_goriz.append(lehelp3)  # Список горизонтальных угроз
        elephant_spisok.append(kehelp3)
        elephant_spisok.append(lehelp3)

    # print(spisokdanger_upleftd_vert)
    # print(spisokdanger_upleftd_goriz)
    # print(spisokdanger_uprightd_vert)
    # print(spisokdanger_uprightd_goriz)
    # print(elephant_spisok)  # Список всех возможных ходов слона

    s1 = 0  # Вспомогательные счетчики
    s2 = 0  # Вспомогательные счетчики
    for i in spisokdanger_upleftd_vert:  # Проверка, возможно ли срубить за один ход!
        if me == i:
            index = spisokdanger_upleftd_vert.index(i)
            if spisokdanger_upleftd_goriz[index] == ne:
                s1 += 1
                # print('s1', s1)

    for i in spisokdanger_uprightd_vert:  # Проверка, возможно ли срубить за один ход!
        if i == m:
            index = spisokdanger_uprightd_vert.index(i)
            if spisokdanger_uprightd_goriz[index] == n:
                s2 += 1
                # print('s2', s2)

    if (s1 != 0) or (s2 != 0):
        print('Противник под угрозой!\nЕго можно срубить за один ход.')
    else:
        print('Противника не срубить за один ход!')
        if differences == 'Разные':  # Тк слон ходит по диагоналям, а у оппонента фигура стоит на квадрате противоположного цвета, то сбуить его будет невозможно
            print('За два хода не удастся срубить оппонента!')
        else:
            print('Получиться срубить оппонента за два хода!\n')
            spisokw_upleftd_vert = []  # Проработка диагоналей оппонента
            spisokw_upleftd_goriz = []
            mehelp = me
            nehelp = ne
            mehelp2 = me
            nehelp2 = ne
            mehelp3 = me
            nehelp3 = ne
            while me <= 8 and ne >= 1:  # Влево вверх диаг  # Влево вверх и Вправо вниз диаг | Формируется список опасноснтей для фигуры оппонента
                me = me + 1
                ne = ne - 1
                if me == 9 or ne == 0:
                    break
                spisokw_upleftd_vert.append(me)  # Список вертикальных опасностей
                spisokw_upleftd_goriz.append(ne)  # Список горизонталей опасностей
                opponent_spisok.append(me)
                opponent_spisok.append(ne)

            while mehelp >= 1 and nehelp <= 8:  # Вправо вниз диаг
                mehelp = mehelp - 1
                nehelp = nehelp + 1
                if mehelp == 0 or nehelp == 9:
                    break
                spisokw_upleftd_vert.append(mehelp)  # Список вертикальных опасностей
                spisokw_upleftd_goriz.append(nehelp)  # Список горизонталей опасностей
                opponent_spisok.append(mehelp)
                opponent_spisok.append(nehelp)

            spisokw_uprightd_vert = []
            spisokw_uprightd_goriz = []

            while mehelp2 <= 8 and nehelp2 <= 8:  # Вправо вверх диаг
                mehelp2 = mehelp2 + 1
                nehelp2 = nehelp2 + 1
                if mehelp2 == 9 or nehelp2 == 9:
                    break
                spisokw_uprightd_vert.append(mehelp2)  # Список вертикальных угроз
                spisokw_uprightd_goriz.append(nehelp2)  # Список горизонтальных угроз
                opponent_spisok.append(mehelp2)
                opponent_spisok.append(nehelp2)

            while mehelp3 >= 1 and nehelp3 >= 1:  # Влево вниз диаг
                mehelp3 = mehelp3 - 1
                nehelp3 = nehelp3 - 1
                if mehelp3 == 0 or nehelp3 == 0:
                    break
                spisokw_uprightd_vert.append(mehelp3)  # Список вертикальных угроз
                spisokw_uprightd_goriz.append(nehelp3)  # Список горизонтальных угроз
                opponent_spisok.append(mehelp3)
                opponent_spisok.append(nehelp3)

            # print(spisokw_upleftd_vert)
            # print(spisokw_upleftd_goriz)
            # print(spisokw_uprightd_vert)
            # print(spisokw_uprightd_goriz)
            # print(opponent_spisok)
            o1 = 0  # Вспомогательные счетчики
            o2 = 0  # Вспомогательные счетчики
            dlinael = len(elephant_spisok)
            maxel = dlinael - 1
            dlinaop = len(opponent_spisok)
            maxop = dlinaop - 1
            # i = 0
            # i1 = 0
            # j = 1
            # j1 = 1
            print('Вам будут предложены всевозможные ходы!')
            if o1 != 1:  # Поиск пересекающихся диагоналей для победы вторым ходом
                for j in range(1, dlinaop, 2):
                    i = j - 1
                    elop = opponent_spisok[i]
                    elop2 = opponent_spisok[j]
                    for j1 in range(1, dlinael, 2):
                        i1 = j1 - 1
                        elel = elephant_spisok[i1]
                        elel2 = elephant_spisok[j1]
                        if j1 == dlinael:
                            i += 1
                            j += 1
                        # print(elop, elel, '\n', elop2, elel2)
                        if elop == elel and elop2 == elel2:
                            o1 = 1
                            print(
                                'Для того чтобы срубить фигуру соперника вторым ходом, нужно первым ходом сходить по вертикали на',
                                elop, 'и по горизонатале на', elop2,
                                '\nТаким образом, вторым ходом вы окажетесь по вертикале на', mestock,
                                'и по горизонатале на', nestock,'\n')


def turris(ke, le, me, ne):  # Ход ладьи(туры) | вводим координаты и ход туры
    spisokdanger_updown_vertical = []
    spisokdanger_updown_gorizont = []
    turrisspisok = []
    kehelp = ke
    lehelp = le
    kestock = ke
    lestock = le

    while ke <= 8:  # Ходы по вертикале вверх
        ke = ke + 1
        if ke == 9:
            break
        spisokdanger_updown_vertical.append(ke)
        spisokdanger_updown_gorizont.append(le)
        turrisspisok.append(ke)
        turrisspisok.append(le)

    while kehelp >= 1:  # Ходы по вертикале вниз
        kehelp = kehelp - 1
        if kehelp == 0:
            break
        spisokdanger_updown_vertical.append(kehelp)
        spisokdanger_updown_gorizont.append(le)
        turrisspisok.append(kehelp)
        turrisspisok.append(le)

    spisokdanger_leftright_vertical = []
    spisokdanger_leftright_gorizont = []
    while le <= 8:  # Ходы по горизонтале вправо
        le = le + 1
        if le == 9:
            break
        spisokdanger_leftright_vertical.append(kestock)
        spisokdanger_leftright_gorizont.append(le)
        turrisspisok.append(kestock)
        turrisspisok.append(le)

    while lehelp >= 1:  # Ходы по горизонтале влево
        lehelp = lehelp - 1
        if lehelp == 0:
            break
        spisokdanger_leftright_vertical.append(kestock)
        spisokdanger_leftright_gorizont.append(lehelp)
        turrisspisok.append(kestock)
        turrisspisok.append(lehelp)

    # print(spisokdanger_updown_vertical)
    # print(spisokdanger_updown_gorizont)
    #print(spisokdanger_leftright_vertical)
    #print(spisokdanger_leftright_gorizont)
    s1 = 0  # Вспомогательные счетчики
    s2 = 0  # Вспомогательные счетчики
    for i in spisokdanger_updown_vertical:  # Проверка, возможно ли срубить за один ход!
        if i == m:
            index = spisokdanger_updown_vertical.index(i)
            if spisokdanger_updown_gorizont[index] == n:
                s1 += 1

    for i in spisokdanger_leftright_gorizont:  # Проверка, возможно ли срубить за один ход!
        if i == n:
            index = spisokdanger_leftright_gorizont.index(i)
            if spisokdanger_leftright_vertical[index] == m:
                s2 += 1

    #print('s1', s1)
    #print('s2', s2)
    if (s1 != 0) or (s2 != 0):
        print('Противник под угрозой!\nЕго можно срубить за один ход.')
    else:
        print('Противника не срубить за один ход!')
        print('Получиться срубить оппонента за два хода!\n')
        spisokop_updown_vert = []
        spisokop_updown_gorizont = []
        opponent_spisok = []
        mehelp = me
        nehelp = ne
        mestock = me
        nestock = ne  # Расчет, как срубить оппонента за два хода!
        # Проработка первого хода, для пересечения с соперником
        while me <= 8:  # Ходы по вертикале вверх
            me = me + 1
            if me == 9:
                break
            spisokop_updown_vert.append(me)
            spisokop_updown_gorizont.append(ne)
            opponent_spisok.append(me)
            opponent_spisok.append(ne)

        while mehelp >= 1:
            mehelp = mehelp - 1
            if mehelp == 0:
                break
            spisokop_updown_vert.append(mehelp)
            spisokop_updown_gorizont.append(ne)
            opponent_spisok.append(mehelp)
            opponent_spisok.append(ne)

        spisokop_leftright_vert = []
        spisokop_leftright_gorizont = []
        while ne <= 8:  # Ходы по горизонтале
            ne = ne + 1
            if ne == 9:
                break
            spisokop_leftright_vert.append(mestock)
            spisokop_leftright_gorizont.append(ne)
            opponent_spisok.append(mestock)
            opponent_spisok.append(ne)

        while nehelp >= 1:
            nehelp = nehelp - 1
            if nehelp == 0:
                break
            spisokop_leftright_vert.append(mestock)
            spisokop_leftright_gorizont.append(nehelp)
            opponent_spisok.append(mestock)
            opponent_spisok.append(nehelp)

        o1 = 0  # Вспомогательные счетчики
        dlinatur = len(turrisspisok)
        maxtur = dlinatur - 1
        dlinaop = len(opponent_spisok)
        maxop = dlinaop - 1
        print('Вам будут предложены всевозможные ходы!')
        if o1 != 1:  # Поиск пересекающихся диагоналей для победы вторым ходом
            for j in range(1, dlinaop, 2):
                i = j - 1
                elop = opponent_spisok[i]
                elop2 = opponent_spisok[j]
                for j1 in range(1, dlinatur, 2):
                    i1 = j1 - 1
                    eltur = turrisspisok[i1]
                    eltur2 = turrisspisok[j1]
                    if j1 == dlinatur:
                        i += 1
                        j += 1
                    # print(elop, eltur, '\n', elop2, eltur2)
                    if elop == eltur and elop2 == eltur2:
                        o1 = 1
                        print(
                            'Для того чтобы срубить фигуру соперника вторым ходом, нужно первым ходом сходить по вертикали на',
                            elop, 'и по горизонатале на', elop2,
                            '\nТаким образом, вторым ходом вы окажетесь по вертикале на', mestock,
                            'и по горизонатале на', nestock,'\n')

def qeen(ke,le,me,ne): #Ферзь(королева) ходит как ладья + слон, поэтому скопирую две предыдущих функции и немного отредачу
    spisokdanger_upleftd_vert = []
    spisokdanger_upleftd_goriz = []
    elephant_spisok = []
    opponent_spisok = []
    mestock = me
    nestock = ne
    kehelp = ke
    lehelp = le
    kehelp2 = ke
    lehelp2 = le
    kehelp3 = ke
    lehelp3 = le
    spisokdanger_updown_vertical = []
    spisokdanger_updown_gorizont = []
    turrisspisok = []
    qeenspisok = []
    lehelpl = le
    lehelpl2 = le
    kestock = ke
    kehelpl = kestock
    kehelpl2 = kestock
    lestock = le
    spisokw_upleftd_vert = []  # Проработка диагоналей оппонента
    spisokw_upleftd_goriz = []
    mehelp = me
    nehelp = ne
    mehelp2 = me
    nehelp2 = ne
    mehelp3 = me
    nehelp3 = ne
    opponent_spisok = []
    mehelpl1 = me
    nehelpl1 = ne
    mehelpl2 = me
    nehelpl2 = ne
    nehelpl3 = ne
    nehelpl4 = ne
    mestock = me
    nestock = ne
    spisokop_updown_vert = []
    spisokop_updown_gorizont = []
    opponent_spisok = []
    mehelp = me
    nehelp = ne
    mestock = me
    nestock = ne
    while ke <= 8 and le >= 1:  # Влево вверх диаг  # Влево вверх и Вправо вниз диаг | Формируется список опасноснтей для фигуры оппонента
        ke = ke + 1
        le = le - 1
        if ke == 9 or le == 0:
            break
        spisokdanger_upleftd_vert.append(ke)  # Список вертикальных опасностей
        spisokdanger_upleftd_goriz.append(le)  # Список горизонталей опасностей
        qeenspisok.append(ke)
        qeenspisok.append(le)

    while kehelp >= 1 and lehelp <= 8:  # Вправо вниз диаг
        kehelp = kehelp - 1
        lehelp = lehelp + 1
        if kehelp == 0 or lehelp == 9:
            break
        spisokdanger_upleftd_vert.append(kehelp)  # Список вертикальных опасностей
        spisokdanger_upleftd_goriz.append(lehelp)  # Список горизонталей опасностей
        qeenspisok.append(kehelp)
        qeenspisok.append(lehelp)

    spisokdanger_uprightd_vert = []
    spisokdanger_uprightd_goriz = []

    while kehelp2 <= 8 and lehelp2 <= 8:  # Вправо вверх диаг
        kehelp2 = kehelp2 + 1
        lehelp2 = lehelp2 + 1
        if kehelp2 == 9 or lehelp2 == 9:
            break
        spisokdanger_uprightd_vert.append(kehelp2)  # Список вертикальных угроз
        spisokdanger_uprightd_goriz.append(lehelp2)  # Список горизонтальных угроз
        qeenspisok.append(kehelp2)
        qeenspisok.append(lehelp2)

    while kehelp3 >= 1 and lehelp3 >= 1:  # Влево вниз диаг
        kehelp3 = kehelp3 - 1
        lehelp3 = lehelp3 - 1
        if kehelp3 == 0 or lehelp3 == 0:
            break
        spisokdanger_uprightd_vert.append(kehelp3)  # Список вертикальных угроз
        spisokdanger_uprightd_goriz.append(lehelp3)  # Список горизонтальных угроз
        qeenspisok.append(kehelp3)
        qeenspisok.append(lehelp3)
    # Ходы ладьи
    while kehelpl2 <= 8:  # Ходы по вертикале вверх
        kehelpl2 = kehelpl2 + 1
        if kehelpl2 == 9:
            break
        spisokdanger_updown_vertical.append(kehelpl2)
        spisokdanger_updown_gorizont.append(lestock)
        qeenspisok.append(kehelpl2)
        qeenspisok.append(lestock)

    while kehelpl >= 1:
        kehelpl = kehelpl - 1
        if kehelpl == 0:
            break
        spisokdanger_updown_vertical.append(kehelpl)
        spisokdanger_updown_gorizont.append(lestock)
        qeenspisok.append(kehelpl)
        qeenspisok.append(lestock)

    spisokdanger_leftright_vertical = []
    spisokdanger_leftright_gorizont = []
    while lehelpl <= 8:  # Ходы по горизонтале
        lehelpl = lehelpl + 1
        if lehelpl == 9:
            break
        spisokdanger_leftright_vertical.append(kestock)
        spisokdanger_leftright_gorizont.append(lehelpl)
        qeenspisok.append(kestock)
        qeenspisok.append(lehelpl)

    while lehelpl2 >= 1:
        lehelpl2 = lehelpl2 - 1
        if lehelpl2 == 0:
            break
        spisokdanger_leftright_vertical.append(kestock)
        spisokdanger_leftright_gorizont.append(lehelpl2)
        qeenspisok.append(kestock)
        qeenspisok.append(lehelpl2)
    # print(spisokdanger_upleftd_vert)
    # print(spisokdanger_upleftd_goriz)
    # print(spisokdanger_uprightd_vert)
    # print(spisokdanger_uprightd_goriz)
    # print(elephant_spisok)  # Список всех возможных ходов слона

    s1 = 0  # Вспомогательные счетчики
    s2 = 0  # Вспомогательные счетчики
    s3 = 0  # Вспомогательные счетчики
    s4 = 0  # Вспомогательные счетчики
    for i in spisokdanger_upleftd_vert:  # Проверка, возможно ли срубить за один ход!
        if m == i:
            index = spisokdanger_upleftd_vert.index(i)
            if spisokdanger_upleftd_goriz[index] == n:
                s1 += 1
                # print('s1', s1)

    for i in spisokdanger_uprightd_vert:  # Проверка, возможно ли срубить за один ход!
        if i == m:
            index = spisokdanger_uprightd_vert.index(i)
            if spisokdanger_uprightd_goriz[index] == n:
                s2 += 1
                # print('s2', s2)


    while me <= 8 and ne >= 1:  # Влево вверх диаг  # Влево вверх и Вправо вниз диаг | Формируется список опасноснтей для фигуры оппонента
        me = me + 1
        ne = ne - 1
        if me == 9 or ne == 0:
            break
        spisokw_upleftd_vert.append(me)  # Список вертикальных опасностей
        spisokw_upleftd_goriz.append(ne)  # Список горизонталей опасностей
        opponent_spisok.append(me)
        opponent_spisok.append(ne)

    while mehelp >= 1 and nehelp <= 8:  # Вправо вниз диаг
        mehelp = mehelp - 1
        nehelp = nehelp + 1
        if mehelp == 0 or nehelp == 9:
            break
        spisokw_upleftd_vert.append(mehelp)  # Список вертикальных опасностей
        spisokw_upleftd_goriz.append(nehelp)  # Список горизонталей опасностей
        opponent_spisok.append(mehelp)
        opponent_spisok.append(nehelp)

    spisokw_uprightd_vert = []
    spisokw_uprightd_goriz = []

    while mehelp2 <= 8 and nehelp2 <= 8:  # Вправо вверх диаг
        mehelp2 = mehelp2 + 1
        nehelp2 = nehelp2 + 1
        if mehelp2 == 9 or nehelp2 == 9:
            break
        spisokw_uprightd_vert.append(mehelp2)  # Список вертикальных угроз
        spisokw_uprightd_goriz.append(nehelp2)  # Список горизонтальных угроз
        opponent_spisok.append(mehelp2)
        opponent_spisok.append(nehelp2)

    while mehelp3 >= 1 and nehelp3 >= 1:  # Влево вниз диаг
        mehelp3 = mehelp3 - 1
        nehelp3 = nehelp3 - 1
        if mehelp3 == 0 or nehelp3 == 0:
            break
        spisokw_uprightd_vert.append(mehelp3)  # Список вертикальных угроз
        spisokw_uprightd_goriz.append(nehelp3)  # Список горизонтальных угроз
        opponent_spisok.append(mehelp3)
        opponent_spisok.append(nehelp3)

        spisokop_updown_vert = []
        spisokop_updown_gorizont = []
        opponent_spisok = []
        mehelp = me
        nehelp = ne
        mestock = me
        nestock = ne  # Расчет, как срубить оппонента за два хода!
    # Проработка первого хода, для пересечения с соперником
    while mehelpl1 <= 8:  # Ходы по вертикале вверх
        mehelpl1 = mehelpl1 + 1
        if mehelpl1 == 9:
            break
        spisokop_updown_vert.append(mehelpl1)
        spisokop_updown_gorizont.append(nehelpl1)
        opponent_spisok.append(mehelpl1)
        opponent_spisok.append(nehelpl1)

    while mehelpl2 >= 1:
        mehelpl2 = mehelpl2 - 1
        if mehelpl2 == 0:
            break
        spisokop_updown_vert.append(mehelpl2)
        spisokop_updown_gorizont.append(nehelpl2)
        opponent_spisok.append(mehelpl2)
        opponent_spisok.append(nehelpl2)

    spisokop_leftright_vert = []
    spisokop_leftright_gorizont = []
    while nehelpl3 <= 8:  # Ходы по горизонтале
        nehelpl3 = nehelpl3 + 1
        if nehelpl3 == 9:
            break
        spisokop_leftright_vert.append(mestock)
        spisokop_leftright_gorizont.append(nehelpl3)
        opponent_spisok.append(mestock)
        opponent_spisok.append(nehelpl3)

    while nehelpl4 >= 1:
        nehelpl4 = nehelpl4 - 1
        if nehelpl4 == 0:
            break
        spisokop_leftright_vert.append(mestock)
        spisokop_leftright_gorizont.append(nehelpl4)
        opponent_spisok.append(mestock)
        opponent_spisok.append(nehelpl4)

      # Расчет, как срубить оппонента за два хода!
    # Проработка первого хода, для пересечения с соперником
    while mehelpl1 <= 8:  # Ходы по вертикале вверх
        mehelpl1 = mehelpl1 + 1
        if mehelpl1 == 9:
            break
        spisokop_updown_vert.append(mehelpl1)
        spisokop_updown_gorizont.append(nehelpl1)
        opponent_spisok.append(mehelpl1)
        opponent_spisok.append(nehelpl1)

    while mehelpl2 >= 1:
        mehelpl2 = mehelpl2 - 1
        if mehelpl2 == 0:
            break
        spisokop_updown_vert.append(mehelpl2)
        spisokop_updown_gorizont.append(nehelpl2)
        opponent_spisok.append(mehelpl2)
        opponent_spisok.append(nehelpl2)

    spisokop_leftright_vert = []
    spisokop_leftright_gorizont = []
    while nehelpl3 <= 8:  # Ходы по горизонтале
        nehelpl3 = nehelpl3 + 1
        if nehelpl3 == 9:
            break
        spisokop_leftright_vert.append(mestock)
        spisokop_leftright_gorizont.append(nehelpl3)
        opponent_spisok.append(mestock)
        opponent_spisok.append(nehelpl3)

    while nehelpl4 >= 1:
        nehelpl4 = nehelpl4 - 1
        if nehelpl4 == 0:
            break
        spisokop_leftright_vert.append(mestock)
        spisokop_leftright_gorizont.append(nehelpl4)
        opponent_spisok.append(mestock)
        opponent_spisok.append(nehelpl4)

    for i in spisokdanger_updown_vertical:  # Проверка, возможно ли срубить за один ход!
        if m == i:
            index = spisokdanger_updown_vertical.index(i)
            if spisokdanger_updown_gorizont[index] == n:
                s3 += 1

    for i in spisokdanger_leftright_gorizont:  # Проверка, возможно ли срубить за один ход!
        if n == i:
            index = spisokdanger_leftright_gorizont.index(i)
            if spisokdanger_leftright_vertical[index] == m:
                s4 += 1

    if (s1 != 0) or (s2 != 0) or (s3 != 0) or (s4 != 0):
        print('Противник под угрозой!\nЕго можно срубить за один ход.')
    else:
        print('Противника не срубить за один ход!')
        # Ферзем всегда возможно срубить за два хода

    if s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0:
        print('Получиться срубить оппонента за два хода!\n')
        # print(spisokw_upleftd_vert)
        # print(spisokw_upleftd_goriz)
        # print(spisokw_uprightd_vert)
        # print(spisokw_uprightd_goriz)
        # print(opponent_spisok)
        o1 = 0  # Вспомогательные счетчики
        dlinael = len(qeenspisok)
        maxel = dlinael - 1
        dlinaop = len(opponent_spisok)
        maxop = dlinaop - 1
        o2 = 0  # Вспомогательные счетчики
        dlinatur = len(qeenspisok)
        maxtur = dlinatur - 1
        dlinaopt = len(opponent_spisok)
        maxopt = dlinaop - 1
        print('Вам будут предложены всевозможные ходы!')
        if o1 != 1:  # Поиск пересекающихся диагоналей для победы вторым ходом
            for j in range(1, dlinaop, 2):
                i = j - 1
                elop = opponent_spisok[i]
                elop2 = opponent_spisok[j]
                for j1 in range(1, dlinael, 2):
                    i1 = j1 - 1
                    elel = qeenspisok[i1]
                    elel2 = qeenspisok[j1]
                    if j1 == dlinael:
                        i += 1
                        j += 1
                    # print(elop, elel, '\n', elop2, elel2)
                    if elop == elel and elop2 == elel2:
                        o1 = 1
                        print(
                            'Для того чтобы срубить фигуру соперника вторым ходом, нужно первым ходом сходить по вертикали на',
                            elop, 'и по горизонатале на', elop2,
                            '\nТаким образом, вторым ходом вы окажетесь по вертикале на', m,
                            'и по горизонатале на', n, '\n')


        if o2 != 1:  # Поиск пересекающихся диагоналей для победы вторым ходом
            for j in range(1, dlinaopt, 2):
                i = j - 1
                elopt = opponent_spisok[i]
                elopt2 = opponent_spisok[j]
                for j1 in range(1, dlinatur, 2):
                    i1 = j1 - 1
                    eltur = qeenspisok[i1]
                    eltur2 = qeenspisok[j1]
                    if j1 == dlinatur:
                        i += 1
                        j += 1
                    # print(elop, eltur, '\n', elop2, eltur2)
                    if elopt == eltur and elopt2 == eltur2:
                        o2 = 1
                        print(
                            'Для того чтобы срубить фигуру соперника вторым ходом, нужно первым ходом сходить по вертикали на',
                            elopt, 'и по горизонатале на', elopt2,
                            '\nТаким образом, вторым ходом вы окажетесь по вертикале на', m,
                            'и по горизонатале на', n, '\n')

def horse(ke, le, me, ne):
    spisokdanger_left_vert = []
    spisokdanger_left_goriz = []
    spisokdanger_right_vert = []
    spisokdanger_right_goriz = []
    horse_spisok = []
    opponent_spisok = []
    spisokop_left_vert = []
    spisokop_left_goriz = []
    spisokop_right_vert = []
    spisokop_right_goriz = []
    kestock = ke
    lestock = le
    mestock = me
    nestock = ne
    kehelp = ke
    kehelp1 = ke
    kehelp2 = ke
    ker = ke
    ker1 = ke
    ker2 = ke
    ker3 = ke
    lehelp = le
    lehelp1 = le
    lehelp2 = le
    ler = le
    ler1 = le
    ler2 = le
    ler3 = le
    mehelp = me
    mehelp1 = me
    mehelp2 = me
    nehelp = ne
    nehelp1 = ne
    nehelp2 = ne
    mer = me
    mer1 = me
    mer2 = me
    mer3 = me
    ner = ne
    ner1 = ne
    ner2 = ne
    ner3 = ne
    # Первые ходы, это 4 буквы Г влево, две вверх, две вниз
    if ke <= 6 and le >= 3:  # Влево вверх
        ke = ke + 2
        le = le - 1
        spisokdanger_left_vert.append(ke)
        spisokdanger_left_goriz.append(le)
        horse_spisok.append(ke)
        horse_spisok.append(le)

    if kehelp <= 6 and lehelp >= 2:  # Влево вбок
        kehelp = kehelp + 1
        lehelp = lehelp - 2
        spisokdanger_left_vert.append(kehelp)
        spisokdanger_left_goriz.append(lehelp)
        horse_spisok.append(kehelp)
        horse_spisok.append(lehelp)

    if kehelp1 >= 3 and lehelp1 >= 2:  # Влево вниз
        kehelp1 = kehelp1 - 2
        lehelp1 = lehelp1 - 1
        spisokdanger_left_vert.append(kehelp1)
        spisokdanger_left_goriz.append(lehelp1)
        horse_spisok.append(kehelp1)
        horse_spisok.append(lehelp1)

    if kehelp2 >= 2 and lehelp2 >= 3:  # Влево вбок низ
        kehelp2 = kehelp2 - 1
        lehelp2 = lehelp2 - 2
        spisokdanger_left_vert.append(kehelp2)
        spisokdanger_left_goriz.append(lehelp2)
        horse_spisok.append(kehelp2)
        horse_spisok.append(lehelp2)

    if ker <= 6 and ler <= 7:  # Вправо вверх
        ker = ker + 2
        ler = ler + 1
        spisokdanger_right_vert.append(ker)
        spisokdanger_right_goriz.append(ler)
        horse_spisok.append(ker)
        horse_spisok.append(ler)

    if ker1 <= 7 and ler1 <= 6:  # Вправо вбок
        ker1 = ker1 + 1
        ler1 = ler1 + 2
        spisokdanger_right_vert.append(ker1)
        spisokdanger_right_goriz.append(ler1)
        horse_spisok.append(ker1)
        horse_spisok.append(ler1)

    if ker2 >= 3 and ler2 <= 7:  # Вправо вниз
        ker2 = ker2 - 2
        ler2 = ler2 + 1
        spisokdanger_right_vert.append(ker2)
        spisokdanger_right_goriz.append(ler2)
        horse_spisok.append(ker2)
        horse_spisok.append(ler2)

    if ker3 >= 2 and ler3 <= 6:  # Вправо вбок низ
        ker3 = ker3 - 1
        ler3 = ler3 + 2
        spisokdanger_right_vert.append(ker3)
        spisokdanger_right_goriz.append(ler3)
        horse_spisok.append(ker3)
        horse_spisok.append(ler3)

    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    for i in spisokdanger_left_vert:
        if i == mestock:
            index = spisokdanger_left_vert.index(i)
            if spisokdanger_left_goriz[index] == nestock:
                s1 += 1

    for i in spisokdanger_right_vert:
        if i == mestock:
            index = spisokdanger_right_vert.index(i)
            if spisokdanger_right_goriz[index] == nestock:
                s2 += 1

    for i in spisokdanger_left_goriz:
        if i == nestock:
            index = spisokdanger_left_goriz.index(i)
            if spisokdanger_left_vert[index] == mestock:
                s3 += 1

    for i in spisokdanger_right_goriz:
        if i == nestock:
            index = spisokdanger_right_goriz.index(i)
            if spisokdanger_right_vert[index] == mestock:
                s4 += 1

    if (s1 != 0) or (s2 != 0) or (s3 != 0) or (s4 != 0):
        print('Противник под угрозой!\nЕго можно срубить за один ход.')
    else:
        print('Противника не срубить за один ход!')
        if me <= 6 and ne >= 3:  # Влево вверх
            me = me + 2
            ne = ne - 1
            spisokop_left_vert.append(me)
            spisokop_left_goriz.append(ne)
            opponent_spisok.append(me)
            opponent_spisok.append(ne)

        if mehelp <= 6 and nehelp >= 2:  # Влево вбок
            mehelp = mehelp + 1
            nehelp = nehelp - 2
            spisokop_left_vert.append(mehelp)
            spisokop_left_goriz.append(nehelp)
            opponent_spisok.append(mehelp)
            opponent_spisok.append(nehelp)

        if mehelp1 >= 3 and nehelp1 >= 2:  # Влево вниз
            mehelp1 = mehelp1 - 2
            nehelp1 = nehelp1 - 1
            spisokdanger_left_vert.append(mehelp1)
            spisokdanger_left_goriz.append(nehelp1)
            opponent_spisok.append(mehelp1)
            opponent_spisok.append(nehelp1)

        if mehelp2 >= 2 and nehelp2 >= 3:  # Влево вбок низ
            mehelp2 = mehelp2 - 1
            nehelp2 = nehelp2 - 2
            spisokop_left_vert.append(mehelp2)
            spisokop_left_goriz.append(nehelp2)
            opponent_spisok.append(mehelp2)
            opponent_spisok.append(nehelp2)

        if mer <= 6 and ner <= 7:  # Вправо вверх
            mer = mer + 2
            ner = ner + 1
            spisokop_right_vert.append(mer)
            spisokop_right_goriz.append(ner)
            opponent_spisok.append(mer)
            opponent_spisok.append(ner)

        if mer1 <= 7 and ner1 <= 6:  # Вправо вбок
            mer1 = mer1 + 1
            ner1 = ner1 + 2
            spisokop_right_vert.append(mer1)
            spisokop_right_goriz.append(ner1)
            opponent_spisok.append(mer1)
            opponent_spisok.append(ner1)

        if mer2 >= 3 and ner2 <= 7:  # Вправо вниз
            mer2 = mer2 - 2
            ner2 = ner2 + 1
            spisokop_right_vert.append(mer2)
            spisokop_right_goriz.append(ner2)
            opponent_spisok.append(mer2)
            opponent_spisok.append(ner2)

        if mer3 >= 2 and ner3 <= 6:  # Вправо вбок низ
            mer3 = mer3 - 1
            ner3 = ner3 + 2
            spisokop_right_vert.append(mer3)
            spisokop_right_goriz.append(ner3)
            opponent_spisok.append(mer3)
            opponent_spisok.append(ner3)

        s1 = 0
        s2 = 0
        s3 = 0
        s4 = 0

        for i in spisokop_right_vert:
            if i in spisokdanger_left_vert:
                indexop = spisokop_right_vert.index(i)
                myindex = spisokdanger_left_vert.index(i)
                if spisokop_right_goriz[indexop] == spisokdanger_left_goriz[myindex]:
                    s1 += 1

        for i in spisokop_left_vert:
            if i in spisokdanger_right_vert:
                indexop = spisokop_left_vert.index(i)
                myindex = spisokdanger_right_vert.index(i)
                if spisokop_left_goriz[indexop] == spisokdanger_right_goriz[myindex]:
                    s2 += 1

        for i in spisokop_right_goriz:
            if i in spisokdanger_left_goriz:
                indexop = spisokop_right_goriz.index(i)
                myindex = spisokdanger_left_goriz.index(i)
                if spisokop_right_vert[indexop] == spisokdanger_left_vert[myindex]:
                    s3 += 1

        for i in spisokop_left_goriz:
            if i in spisokdanger_right_goriz:
                indexop = spisokop_left_goriz.index(i)
                myindex = spisokdanger_right_goriz.index(i)
                if spisokop_left_vert[indexop] == spisokdanger_right_vert[myindex]:
                    s4 += 1
        if (s1 != 0) or (s2 != 0) or (s3 != 0) or (s4 != 0):
            print('Получиться срубить оппонента за два хода!\n')
            print('Вам будут предложены всевозможные ходы!')
            o1 = 0  # Вспомогательные счетчики
            dlinael = len(horse_spisok)
            maxel = dlinael - 1
            dlinaop = len(opponent_spisok)
            maxop = dlinaop - 1
            if o1 != 1:  # Поиск пересекающихся диагоналей для победы вторым ходом
                for j in range(1, dlinaop, 2):
                    i = j - 1
                    elop = opponent_spisok[i]
                    elop2 = opponent_spisok[j]
                    for j1 in range(1, dlinael, 2):
                        i1 = j1 - 1
                        elel = horse_spisok[i1]
                        elel2 = horse_spisok[j1]
                        if j1 == dlinael:
                            i += 1
                            j += 1
                        # print(elop, elel, '\n', elop2, elel2)
                        if elop == elel and elop2 == elel2:
                            o1 = 1
                            print(
                                'Для того чтобы срубить фигуру соперника вторым ходом, нужно первым ходом сходить по вертикали на',
                                elop, 'и по горизонатале на', elop2,
                                '\nТаким образом, вторым ходом вы окажетесь по вертикале на', mestock,
                                'и по горизонатале на', nestock,'\n')
        else:
            print('За два хода не срубить!')

while k1 != 1:  # Проверка, чтобы ввели число | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        k = int(input("Введите текущую координату фигуры(вертикаль): "))  # y1 = первая фигура верт
        while k > 8:  # Проверка, чтобы ввели число не больше 8.
            # | Диалоговый режим с пользователем и обработкой ошибок ввода
            print('\nКоордината должна не превышать 8')
            k = int(input("Введите текущую координату фигуры повторно(вертикаль): "))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        k1 += 1

while l1 != 1:  # Проверка, чтобы ввели число | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        l = int(input("Введите текущую координату фигуры(горизонталь): "))  # x1 = первая фигура гориз
        while l > 8:  # Проверка, чтобы ввели число не больше 8.
            # | Диалоговый режим с пользователем и обработкой ошибок ввода
            print('\nКоордината должна не превышать 8')
            l = int(input("Введите текущую координату фигуры повторно(горизонталь): "))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        l1 += 1

while m1 != 1:  # Проверка, чтобы ввели число | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        m = int(input("Введите координату для хода(вертикаль): "))  # y2 = вторая фигура верт
        while m > 8:  # Проверка, чтобы ввели число не больше 8.
            # | Диалоговый режим с пользователем и обработкой ошибок ввода
            print('\nКоордината должна не превышать 8')
            m = int(input("Введите координату для хода повторно(вертикаль): "))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        m1 += 1

while n1 != 1:  # Проверка, чтобы ввели число | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        n = int(input("Введите координату для хода(горизонталь): "))  # x2 = вторая фигура гориз
        while n > 8:  # Проверка, чтобы ввели число не больше 8.
            # | Диалоговый режим с пользователем и обработкой ошибок ввода
            print('\nКоордината должна не превышать 8')
            n = int(input("Введите координату для хода повторно(горизонталь): "))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        n1 += 1

if ((k + l) % 2) == ((m + n) % 2):  # Выясняем являются ли поля (k,l) и (m,n), полями одного цвета
    print('Одинаковые')
    differences = 'Одинаковые'
else:
    print('Разные')
    differences = 'Разные'

f = 0
while f1 != 1:  # Проверка, чтобы ввели число от 1-4 | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        print('Выберите, какая фигура будет стоять на k =', k, '| l =', l)
        figura = int(
            input('\nФерзь - 1\nЛадья - 2\nСлон -  3\nКонь -  4\nВведите число!\n'))  # Ввод выбранной фигурына k,l
        while figura > 4 or figura < 1:
            print('Вы выбрали неверное число!')
            print('Выберите, какая фигура будет стоять на k =', k, '| l =', l)
            figura = int(
                input(
                    '\nФерзь - 1\nЛадья - 2\nСлон -  3\nКонь -  4\nВведите число!\n'))  # Ввод выбранной фигурына k,l
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        f1 += 1

print('Наша фигура: k = ', k, '| l = ', l, '\nПротивник: m = ', m, '| n = ', n)

vertical = k
gorizontal = l
# print('Наша фигура!')
# yourfigura = coloursquare(vertical, gorizontal)  # Цвет квадрата моей фигуры
vertical = m
gorizontal = n
# print('Фигура оппонента!')
# figuraopponent = coloursquare(vertical, gorizontal)  # Цвет квадрата фигуры оппонента

if figura == 1:
    print('Вы выбрали ферзя!\n')
    ke = k
    le = l
    me = m
    ne = n
    qeen(ke, le, me, ne)
elif figura == 2:
    print('Вы выбрали ладью!\n')
    ke = k
    le = l
    me = m
    ne = n
    turris(ke, le, me, ne)
elif figura == 3:
    print('Вы выбрали слона!\n')
    ke = k
    le = l
    me = m
    ne = n
    elephant(ke, le, me, ne)
elif figura == 4:
    print('Вы выбрали коня!\n')
    ke = k
    le = l
    me = m
    ne = n
    horse(ke, le, me, ne)