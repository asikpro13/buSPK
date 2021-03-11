# -*- coding: utf-8 -*-
import sys
from plyer import gps
from kivy.app import App
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.toast import toast

from kivymd_extensions.akivymd import *
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
try:
    from GPS import location
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


def path(From, to):
    if From == '':
        pass


class MainApp(MDApp):
    def __init__(self, **kwargs):  # Инициализация класса, тут объявляем все объекты и переменные
        self.From_SP1_to_SP5_points = [
            MapMarker(lat=61.272586, lon=73.411232, source="station_marker.png", on_press=toasts.toast_for_SP1),
            MapMarker(lat=61.271631, lon=73.413228, source="point.png"),
            MapMarker(lat=61.271032, lon=73.417133, source="point.png"),
            MapMarker(lat=61.270598, lon=73.420051, source="point.png"),
            MapMarker(lat=61.270143, lon=73.423013, source="point.png"),
            MapMarker(lat=61.269709, lon=73.425545, source="point.png"),
            MapMarker(lat=61.268697, lon=73.424858, source="point.png"),
            MapMarker(lat=61.266837, lon=73.423356, source="point.png"),
            MapMarker(lat=61.264542, lon=73.422041, source="point.png"),
            MapMarker(lat=61.262124, lon=73.420582, source="point.png"),
            MapMarker(lat=61.260264, lon=73.419423, source="point.png"),
            MapMarker(lat=61.258884, lon=73.418540, source="point.png"),
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP5)]
        # Маршрут от 1 до 5 сп
        self.From_Sp1_to_SP4_points = []

        self.allSP_points = [
            # Маркер для СП1:
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP1),
            # Маркер для СП2:
            MapMarker(lat=61.250593, lon=73.411524, source="station_marker.png", on_press=toasts.toast_for_SP2),
            # Маркер для СП3:
            MapMarker(lat=61.249223, lon=73.374205, source="station_marker.png", on_press=toasts.toast_for_SP3),
            # Маркер для СП4:
            MapMarker(lat=61.263820, lon=73.412419, source="station_marker.png", on_press=toasts.toast_for_SP4),
            # Маркер для СП5:
            MapMarker(lat=61.272384, lon=73.413556, source="station_marker.png", on_press=toasts.toast_for_SP5)]

        super().__init__(**kwargs)
        self.count = 0
        self.title = "FastGPS"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.bl = FloatLayout()
        self.bl.height += 100
        try:
            self.gps = location(self.mapview)
        except NameError:
            print('Если вы запускаете код с пк, то модуля геолокации не будет')
        self.verify_geolocation = True

    def build(self):  # Основной метод на котором основывается все приложение
        self.mapview = MapView(zoom=12, lat=61.254035, lon=73.396221, pos_hint={'top': 1}, size_hint=(None, None),
                               size=(Window.width, Window.height))
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
            on_press=self.user_geolocation)
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
        for point in self.allSP_points:
            self.mapview.add_marker(point)

    def show_example_grid_bottom_sheet_from(self):
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

    def path(self):  # Прокладываем путь
        self.del_all_point()  # Удаляем все точки
        for point in self.From_SP1_to_SP5_points:
            self.mapview.add_marker(point)

    def show_example_grid_bottom_sheet_to(self):
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

    def router(self):  # Функция для обработки маршрута и вывод оповещения
        if str(self.screen.ids.From.text) == 'ОТ?' or str(self.screen2.ids.To.text) == 'ДО?':
            toast("Некоректные данные для маршрута", 0.4)
        else:
            self.path()
            toast('Маршрут от ' + str(self.screen.ids.From.text) + ' до ' + str(self.screen2.ids.To.text), 0.4)

    def del_all_point(self):  # Удаление всех точек. Т.к. в модуле работы с картой нет метода для очистки маркеров,
        # приходится собственноручно их сохранять и удалять
        for point in [self.From_SP1_to_SP5_points, self.allSP_points]:
            for i in range(len(point)):
                self.mapview.remove_marker(point[i])

    def user_geolocation(self, *args):  # Обновляем местоположение пользователя
        if self.gps.get_state() == 0:
            self.gps.start()
            self.btn_location.icon = 'location_on_true.png'
        else:
            self.gps.stop()
            self.btn_location.icon = 'location_on_false.png'

if __name__ == '__main__':
    app = MainApp()
    app.run()
