
class Oshibka_1(Exception):
    def __init__(self, tip_oshibki, podskazka):
        self.tip_oshibki = tip_oshibki
        self.podskazka = podskazka

class Oshibka_2(Exception):
    def __init__(self, obryv_cepi, nizkie_temp, otsyt_benz):
        self.obryv_cepi = obryv_cepi
        self.nizkie_temp = nizkie_temp
        self.otsyt_benz = otsyt_benz


def zapysk_dvigatela(klych, iskra, temp, benz):
    if klych == 1:
        print('Зажигание включено')
    else:
        try:
            raise Oshibka_1 ("Зажигание не включено", "Поверните ключ")
        except Oshibka_1 as o_1:
            print(f'Ошибка: {o_1.tip_oshibki}')
            print(f'Ваши дальнейшие действия: {o_1.podskazka}')
            raise
    if iskra > 0:
        print('Пуск!')
    else:
        try:
            raise Oshibka_2(obryv_cepi="Проверьте электрическую цепь")
        except Oshibka_2 as o_2:
            print(f'Внимание! {o_2.obryv_cepi}\n')
            raise
    if temp > 0 and temp < 90:
        print('Двигатель завелся!')
    else:
        try:
            raise Oshibka_2(nizkie_temp="Недопустимая температура")
        except Oshibka_2 as o_2:
            print(f'Температура: {o_2.nizkie_temp}\n')
            raise
    if benz > 10:
        print('Поехали!')
    else:
        try:
            raise Oshibka_2(otsyt_benz="Низкий уровень топлива")
        except Oshibka_2 as o_2:
            print(f'Внимание! {o_2.otsyt_benz}\n')
            raise

zapysk_dvigatela(1, 30, 60, 80)
zapysk_dvigatela(1, 20, 35, 5)







