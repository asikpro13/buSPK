# -*- coding: utf-8 -*-
import sys
from plyer import gps  # Объект геолокации для взаимодействия с телефоном
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
# Технические внутренности


from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.toast import toast  # Всплывающее уведомление
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button
from kivymd.uix.list import OneLineListItem
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapMarker, MapSource, MapLayer
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
# Карта, объекты стилей, разметка

from points import paths

#  Импорт класса с путями маршрутов

try:
    from GPS import location  # Импорт класса для работы с геолокацией
except ModuleNotFoundError:
    print('Если вы запускаете код с пк, то модуля геолокации не будет')
from toasts import toasts

button_from = '''
Screen:
    MDRaisedButton:
        id: From
        text: "ОТ?"
        on_release: app.show_example_grid_bottom_sheet_from()
        pos_hint: {"center_x": 0.1, "center_y": 0.01}
        size_hint: (.5, None)
        size: (150, 100)'''  # Левая кнопка выбора остановки

button_to = '''
Screen:
    MDRaisedButton:
        id: To
        text: "ДО?"
        on_release: app.show_example_grid_bottom_sheet_to()
        pos_hint: {"center_x": 0.89, "center_y": 0.009}
        size_hint: (.5, None)
        size: (150, 100)'''  # Правая кнопка выбора остановки

button_router = '''
Screen:
    MDRaisedButton:
        id: To
        text: "ПОСТРОИТЬ МАРШРУТ"
        on_release: app.router()
        pos_hint: {"center_x": 0.5, "center_y": 0.009}
        size_hint: (.5, None)
        size: (150, 100)'''  # Кнопка для построения маршрута


class MainApp(MDApp):  # Главное окно
    def __init__(self, **kwargs):  # Инициализация класса, тут объявляем все объекты и переменные
        super().__init__(**kwargs)
        self.count = 0
        self.paths = paths()
        self.title = "FastGPS"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.bl = FloatLayout()
        self.bl.height += 100
        self.mapview = MapView(zoom=12, lat=61.254035, lon=73.396221, pos_hint={'top': 1}, size_hint=(None, None),
                               size=(Window.width, Window.height))
        try:
            self.gps = location(self.mapview)
            print('Карта')
        except NameError:
            print('Если вы запускаете код с пк, то модуля геолокации не будет')

    def build(self):  # Основной метод на котором основывается все приложение
        self.toasts = toasts()

        def callback(permission, results):
            if all([res for res in results]):
                print(';sada')
            else:
                print('ВСЕ ПЛОХО')

        try:
            from android.permissions import Permission, request_permissions
            request_permissions([Permission.ACCESS_FINE_LOCATION], callback)
            gps.configure(on_location=self.user_geolocation,
                          on_status=self.on_auth_status)
        except ModuleNotFoundError:
            print('С пк не работает т.к. при сборке используется python-for-android')

        self.allSP()
        self.mapview.map_source.min_zoom = 9
        self.mapviewLayout = BoxLayout()
        self.mapviewLayout.add_widget(self.mapview)
        self.bl.add_widget(self.mapviewLayout)
        btn_zoom_in = MDIconButton(
            icon="zoom_in.png",
            pos_hint={'right': 1, 'top': .7},
            on_press=self.zoom_in)
        btn_zoom_out = MDIconButton(
            icon="zoom_out.png",
            pos_hint={'right': 1, 'top': .4},
            on_press=self.zoom_out)
        self.btn_location = MDIconButton(
            icon="location_on_false.png",
            pos_hint={'right': 1, 'top': .18},
            on_press=self.set_state_geolocation)
        self.screen = Builder.load_string(button_from)
        self.screen2 = Builder.load_string(button_to)
        self.screen3 = Builder.load_string(button_router)

        self.bl.add_widget(btn_zoom_in)
        self.bl.add_widget(btn_zoom_out)
        self.bl.add_widget(self.btn_location)
        self.bl.add_widget(self.screen)
        self.bl.add_widget(self.screen2)
        self.bl.add_widget(self.screen3)
        return self.bl

    def allSP(self):  # Вывод всех структурных подразделений
        for point in self.paths.get_allSP_points():
            self.mapview.add_marker(point)

    def show_example_grid_bottom_sheet_from(self):  # Нажатие на кнопку для открытия меню выбора автобуса
        bottom_sheet_menu = MDGridBottomSheet()
        data = {"1 СП": "bus_icon_126644.png",
                "2 СП": "bus_icon_126644.png",
                "3 СП": "bus_icon_126644.png",
                "4 СП": "bus_icon_126644.png",
                "5 СП": "bus_icon_126644.png"}
        for item in data.items():
            bottom_sheet_menu.add_item(item[0],
                                       lambda x, y=item[0]: self.callback_from(y),
                                       icon_src=item[1])
        bottom_sheet_menu.open()

    def path(self, a, b):  # Прокладываем путь
        self.del_all_point()  # Удаляем все точки
        for point in self.paths.get_list_points(a, b):
            self.mapview.add_marker(point)

    def show_example_grid_bottom_sheet_to(self):  # Нажатие на кнопку для открытия меню выбора автобуса
        bottom_sheet_menu = MDGridBottomSheet()
        data = {"1 СП": "bus_icon_126644.png",
                "2 СП": "bus_icon_126644.png",
                "3 СП": "bus_icon_126644.png",
                "4 СП": "bus_icon_126644.png",
                "5 СП": "bus_icon_126644.png"}
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_to(y),
                icon_src=item[1])
        bottom_sheet_menu.open()

    def zoom_in(self, *args):  # Событие для приближения карты
        self.mapview.zoom = self.mapview.zoom + 1

    def zoom_out(self, *args):  # Событие для отдаления карты
        self.mapview.zoom = self.mapview.zoom - 1

    def callback_from(self, *args):  # События для правой кнопки выбора остановки
        self.screen.ids.From.text = str(args[0])

    def callback_to(self, *args):  # События для левой кнопки остановки
        self.screen2.ids.To.text = str(args[0])

    def router(self):  # Функция для вывода оповещения
        if str(self.screen.ids.From.text) == 'ОТ?' or str(self.screen2.ids.To.text) == 'ДО?':
            self.toasts.bad_path()
        elif str(self.screen.ids.From.text) == str(self.screen2.ids.To.text):
            self.toasts.bad_path()
        else:
            self.path(str(self.screen.ids.From.text), str(self.screen2.ids.To.text))
            self.toasts.good_path(self.screen.ids.From.text, self.screen2.ids.To.text)

    def del_all_point(self):  # Удаление всех точек. Т.к. в модуле работы с картой нет метода для очистки маркеров,
        # приходится собственноручно их сохранять и удалять
        for point in self.paths.get_all_points():
            for i in range(len(point)):
                self.mapview.remove_marker(point[i])

    def user_geolocation(self, **kwargs):  # Обновляем местоположение пользователя
        self.mapview.remove_marker(MapMarker(lat=float(self.gps.get_lat_lon()[0]), lon=float(self.gps.get_lat_lon()[1]),
                                             source="location_on_true.png"))
        self.lat = kwargs['lat']
        self.lon = kwargs['lon']
        self.gps.set_lat_lon(self.lat, self.lon)  # Меняем состояние координат
        self.mapview.add_marker(MapMarker(lat=float(self.gps.get_lat_lon()[0]), lon=float(self.gps.get_lat_lon()[1]),
                                          source="location_on_true.png"))  # Ставим маркер по координатам пользователя

    def set_state_geolocation(self, *args):  # Кнопка отслеживания местоположения(вкл/выкл)
        try:
            print(self.gps.state)
            state = self.gps.set_state_geolocation()
            if not state:
                gps.start(minTime=100, minDistance=0)
                self.btn_location.icon = 'location_on_true.png'
            elif state:
                self.btn_location.icon = 'location_on_false.png'
                gps.stop()
        except NotImplementedError:
            pass

    def on_auth_status(self, general, status):  # Событие критической ошибки
        print(general, status)


if __name__ == '__main__':
    app = MainApp()
    app.run()
