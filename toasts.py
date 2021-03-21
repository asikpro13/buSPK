from kivymd.toast import toast
import datetime
import time

schedule = {  # Расписание автобусов (какое Структурное Подразделение: Во сколько приедет)
            'SP1_OST': ['7:45', '8:35', '9:45', '11:05', '12:05', '13:40', '14:55', '15:05', '15:40', '16:20', '17:20',
                        '18:05'],  # Остановка СП1
            'SP1_CENTER': ['7:35', '11:00', '12:00', '15:00', '16:15', '17:15', '18:00'],  # Центральный вход СП1
            'SP2': ['7:55', '13:30', '14:45'],
            'SP3': ['8:10'],
            'SP4': ['8:25', '15:30'],
            'SP5': ['7:45', '8:10', '10:30', '11:30', '12:30', '13:10', '14:10', '15:20', '15:30', '16:45', '17:30',
                    '18:30']}


def date_sort(date1):  # Сортируем ближайший автобус исходя из количтесва секунд до его прихода
    d = datetime.timedelta(hours=int(date1.split(':')[0]), minutes=int(date1.split(':')[1])) - \
        datetime.timedelta(hours=int(datetime.datetime.now().hour), minutes=int(datetime.datetime.now().minute))
    # Разница во времени между автобусами и настоящим временем
    if d.total_seconds() > 0:
        return d.total_seconds()
    else:  # Т.к. сортировка происходит от меньшего к большему то возвращаем не отрицательные секунды, а просто
        # огромное число
        return 99999999


class toasts:
    def toast_for_SP1(self, *args):  # Обработчик маркера автобуса
        date = sorted(schedule['SP1_CENTER'] + schedule['SP1_OST'], key=date_sort)
        toast('Ближайший автобус в ' + str(date[0]), 0.4)

    def toast_for_SP2(self, *args):
        date = sorted(schedule['SP2'], key=date_sort)
        toast('Ближайший автобус в ' + str(date[0]), 0.4)

    def toast_for_SP3(self, *args):
        date = sorted(schedule['SP3'], key=date_sort)
        toast('Ближайший автобус в ' + str(date[0]), 0.4)

    def toast_for_SP4(self, *args):
        date = sorted(schedule['SP4'], key=date_sort)
        toast('Ближайший автобус в ' + str(date[0]), 0.4)

    def toast_for_SP5(self, *args):
        date = sorted(schedule['SP5'], key=date_sort)
        toast('Ближайший автобус в ' + str(date[0]), 0.4)

    def good_path(self, a, b):
        toast('Маршрут от ' + str(a) + ' до ' + str(b), 0.4)

    def bad_path(self):
        toast("Некоректные данные для маршрута", 0.4)