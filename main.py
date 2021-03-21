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
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP1),
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
            MapMarker(lat=61.272384, lon=73.413556, source="station_marker.png", on_press=toasts.toast_for_SP5)]
        # Маршрут от 1 до 5 сп
        self.From_SP1_to_SP4_points = [
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP1),
            MapMarker(lat=61.258884, lon=73.418540, source="point.png"),
            MapMarker(lat=61.259176, lon=73.418713, source="point.png"),
            MapMarker(lat=61.259471, lon=73.418879, source="point.png"),
            MapMarker(lat=61.260049, lon=73.419239, source="point.png"),
            MapMarker(lat=61.260587, lon=73.419550, source="point.png"),
            MapMarker(lat=61.261146, lon=73.419915, source="point.png"),
            MapMarker(lat=61.261884, lon=73.420344, source="point.png"),
            MapMarker(lat=61.262649, lon=73.420805, source="point.png"),
            MapMarker(lat=61.263264, lon=73.421202, source="point.png"),
            MapMarker(lat=61.258884, lon=73.418540, source="point.png"),
            MapMarker(lat=61.264044, lon=73.421674, source="point.png"),
            MapMarker(lat=61.264374, lon=73.418736, source="point.png"),
            MapMarker(lat=61.264249, lon=73.419907, source="point.png"),
            MapMarker(lat=61.264712, lon=73.415550, source="point.png"),
            MapMarker(lat=61.264940, lon=73.413833, source="point.png"),
            MapMarker(lat=61.264642, lon=73.416533, source="point.png"),
            MapMarker(lat=61.265064, lon=73.412718, source="point.png"),
            MapMarker(lat=61.264611, lon=73.412482, source="point.png"),
            MapMarker(lat=61.264249, lon=73.412278, source="point.png"),
            MapMarker(lat=61.258884, lon=73.418540, source="point.png"),
            MapMarker(lat=61.263820, lon=73.412419, source="station_marker.png", on_press=toasts.toast_for_SP4)]

        self.From_SP1_to_SP3_points = [
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP1),
            MapMarker(lat=61.249211, lon=73.374239, source="point.png"),
            MapMarker(lat=61.248991, lon=73.375709, source="point.png"),
            MapMarker(lat=61.248347, lon=73.381055, source="point.png"),
            MapMarker(lat=61.248583, lon=73.378246, source="point.png"),
            MapMarker(lat=61.248521, lon=73.382605, source="point.png"),
            MapMarker(lat=61.249052, lon=73.386604, source="point.png"),
            MapMarker(lat=61.248759, lon=73.384394, source="point.png"),
            MapMarker(lat=61.248759, lon=73.384394, source="point.png"),
            MapMarker(lat=61.249364, lon=73.388654, source="point.png"),
            MapMarker(lat=61.249602, lon=73.390220, source="point.png"),
            MapMarker(lat=61.249795, lon=73.391395, source="point.png"),
            MapMarker(lat=61.250426, lon=73.392146, source="point.png"),
            MapMarker(lat=61.250870, lon=73.392650, source="point.png"),
            MapMarker(lat=61.251421, lon=73.393262, source="point.png"),
            MapMarker(lat=61.251922, lon=73.393820, source="point.png"),
            MapMarker(lat=61.252369, lon=73.394324, source="point.png"),
            MapMarker(lat=61.252860, lon=73.394893, source="point.png"),
            MapMarker(lat=61.253305, lon=73.395397, source="point.png"),
            MapMarker(lat=61.253527, lon=73.396105, source="point.png"),
            MapMarker(lat=61.253591, lon=73.396915, source="point.png"),
            MapMarker(lat=61.254248, lon=73.397253, source="point.png"),
            MapMarker(lat=61.254728, lon=73.396802, source="point.png"),
            MapMarker(lat=61.255057, lon=73.396877, source="point.png"),
            MapMarker(lat=61.256204, lon=73.397462, source="point.png"),
            MapMarker(lat=61.255596, lon=73.397164, source="point.png"),
            MapMarker(lat=61.253926, lon=73.397340, source="point.png"),
            MapMarker(lat=61.256834, lon=73.397784, source="point.png"),
            MapMarker(lat=61.257594, lon=73.398159, source="point.png"),
            MapMarker(lat=61.258178, lon=73.398460, source="point.png"),
            MapMarker(lat=61.258178, lon=73.398460, source="point.png"),
            MapMarker(lat=61.259453, lon=73.399074, source="point.png"),
            MapMarker(lat=61.259351, lon=73.399975, source="point.png"),
            MapMarker(lat=61.259233, lon=73.400884, source="point.png"),
            MapMarker(lat=61.259124, lon=73.401946, source="point.png"),
            MapMarker(lat=61.258969, lon=73.403255, source="point.png"),
            MapMarker(lat=61.258809, lon=73.404467, source="point.png"),
            MapMarker(lat=61.258690, lon=73.405626, source="point.png"),
            MapMarker(lat=61.258509, lon=73.407300, source="point.png"),
            MapMarker(lat=61.258975, lon=73.398845, source="point.png"),
            MapMarker(lat=61.258375, lon=73.408437, source="point.png"),
            MapMarker(lat=61.258173, lon=73.410003, source="point.png"),
            MapMarker(lat=61.258028, lon=73.411297, source="point.png"),
            MapMarker(lat=61.257909, lon=73.412338, source="point.png"),
            MapMarker(lat=61.257770, lon=73.413475, source="point.png"),
            MapMarker(lat=61.257651, lon=73.414580, source="point.png"),
            MapMarker(lat=61.257547, lon=73.415556, source="point.png"),
            MapMarker(lat=61.257423, lon=73.416490, source="point.png"),
            MapMarker(lat=61.257305, lon=73.417562, source="point.png"),
            MapMarker(lat=61.257977, lon=73.417957, source="point.png"),
            MapMarker(lat=61.258592, lon=73.418354, source="point.png"),
            MapMarker(lat=61.249223, lon=73.374205, source="station_marker.png", on_press=toasts.toast_for_SP3)]

        self.From_SP1_to_SP2_points = [
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP1),
            MapMarker(lat=61.251057, lon=73.414062, source="point.png"),
            MapMarker(lat=61.251417, lon=73.416054, source="point.png"),
            MapMarker(lat=61.251650, lon=73.417315, source="point.png"),
            MapMarker(lat=61.251901, lon=73.418618, source="point.png"),
            MapMarker(lat=61.252660, lon=73.418020, source="point.png"),
            MapMarker(lat=61.253451, lon=73.417398, source="point.png"),
            MapMarker(lat=61.254236, lon=73.416797, source="point.png"),
            MapMarker(lat=61.254841, lon=73.416464, source="point.png"),
            MapMarker(lat=61.255441, lon=73.416502, source="point.png"),
            MapMarker(lat=61.256195, lon=73.416888, source="point.png"),
            MapMarker(lat=61.256882, lon=73.417307, source="point.png"),
            MapMarker(lat=61.257725, lon=73.417832, source="point.png"),
            MapMarker(lat=61.258463, lon=73.418272, source="point.png"),
            MapMarker(lat=61.250593, lon=73.411524, source="station_marker.png", on_press=toasts.toast_for_SP2)]

        self.From_SP2_to_SP5_points = [*self.From_SP1_to_SP2_points[1:], *self.From_SP1_to_SP5_points[1:]]

        self.From_SP2_to_SP4_points = [
            MapMarker(lat=61.250593, lon=73.411524, source="station_marker.png", on_press=toasts.toast_for_SP2),
            MapMarker(lat=61.251057, lon=73.414062, source="point.png"),
            MapMarker(lat=61.251417, lon=73.416054, source="point.png"),
            MapMarker(lat=61.251650, lon=73.417315, source="point.png"),
            MapMarker(lat=61.251901, lon=73.418618, source="point.png"),
            MapMarker(lat=61.252660, lon=73.418020, source="point.png"),
            MapMarker(lat=61.253451, lon=73.417398, source="point.png"),
            MapMarker(lat=61.254236, lon=73.416797, source="point.png"),
            MapMarker(lat=61.254841, lon=73.416464, source="point.png"),
            MapMarker(lat=61.255441, lon=73.416502, source="point.png"),
            MapMarker(lat=61.256195, lon=73.416888, source="point.png"),
            MapMarker(lat=61.256882, lon=73.417307, source="point.png"),
            MapMarker(lat=61.257498, lon=73.417694, source="point.png"),
            MapMarker(lat=61.257694, lon=73.415876, source="point.png"),
            MapMarker(lat=61.257953, lon=73.413966, source="point.png"),
            MapMarker(lat=61.258118, lon=73.412013, source="point.png"),
            MapMarker(lat=61.258376, lon=73.410425, source="point.png"),
            MapMarker(lat=61.258469, lon=73.409417, source="point.png"),
            MapMarker(lat=61.259022, lon=73.409685, source="point.png"),
            MapMarker(lat=61.259703, lon=73.409996, source="point.png"),
            MapMarker(lat=61.260432, lon=73.410361, source="point.png"),
            MapMarker(lat=61.261300, lon=73.410790, source="point.png"),
            MapMarker(lat=61.262225, lon=73.411252, source="point.png"),
            MapMarker(lat=61.263143, lon=73.411751, source="point.png"),
            MapMarker(lat=61.263820, lon=73.412419, source="station_marker.png", on_press=toasts.toast_for_SP4)]

        self.From_SP2_to_SP3_points = [
            MapMarker(lat=61.249223, lon=73.374205, source="station_marker.png", on_press=toasts.toast_for_SP3),
            *self.From_SP1_to_SP3_points[1:11],
            MapMarker(lat=61.249802, lon=73.391474, source="point.png"),
            MapMarker(lat=61.249342, lon=73.392086, source="point.png"),
            MapMarker(lat=61.248980, lon=73.392504, source="point.png"),
            MapMarker(lat=61.248582, lon=73.392965, source="point.png"),
            MapMarker(lat=61.248226, lon=73.393287, source="point.png"),
            MapMarker(lat=61.248257, lon=73.394317, source="point.png"),
            MapMarker(lat=61.249802, lon=73.391474, source="point.png"),
            MapMarker(lat=61.248200, lon=73.396130, source="point.png"),
            MapMarker(lat=61.248179, lon=73.397439, source="point.png"),
            MapMarker(lat=61.248242, lon=73.398321, source="point.png"),
            MapMarker(lat=61.248454, lon=73.399597, source="point.png"),
            MapMarker(lat=61.248718, lon=73.401035, source="point.png"),
            MapMarker(lat=61.248976, lon=73.402505, source="point.png"),
            MapMarker(lat=61.249236, lon=73.404205, source="point.png"),
            MapMarker(lat=61.249520, lon=73.405696, source="point.png"),
            MapMarker(lat=61.249805, lon=73.407263, source="point.png"),
            MapMarker(lat=61.250079, lon=73.408754, source="point.png"),
            MapMarker(lat=61.250234, lon=73.409583, source="point.png"),
            MapMarker(lat=61.250593, lon=73.411524, source="station_marker.png", on_press=toasts.toast_for_SP2),
        ]

        self.From_SP3_to_SP4_points = [
            self.From_SP1_to_SP3_points[-1],
            *self.From_SP1_to_SP3_points[1:41],
            *self.From_SP2_to_SP4_points[:-9:-1]]

        self.From_SP3_to_SP5_points = [
            self.From_SP1_to_SP3_points[-1],
            *self.From_SP1_to_SP3_points[1:41],
            *self.From_SP2_to_SP4_points[-2:-9:-1],
            *self.From_SP1_to_SP5_points[1:9],
            MapMarker(lat=61.267886, lon=73.424159, source="point.png"),
            MapMarker(lat=61.265541, lon=73.422647, source="point.png"),
            MapMarker(lat=61.264026, lon=73.421655, source="point.png"),
            MapMarker(lat=61.264263, lon=73.419595, source="point.png"),
            MapMarker(lat=61.264532, lon=73.417363, source="point.png"),
            MapMarker(lat=61.264713, lon=73.415808, source="point.png"),
            MapMarker(lat=61.264909, lon=73.414102, source="point.png"),
            MapMarker(lat=61.265069, lon=73.412707, source="point.png"),
            MapMarker(lat=61.264496, lon=73.412407, source="point.png"),
            MapMarker(lat=61.263864, lon=73.412099, source="point.png"),
            MapMarker(lat=61.272384, lon=73.413556, source="station_marker.png", on_press=toasts.toast_for_SP5)
        ]

        self.From_SP4_to_SP5_points = [
            self.From_SP1_to_SP5_points[-1],
            *self.From_SP1_to_SP5_points[1:9],
            *self.From_SP1_to_SP4_points[13:20],
            self.From_SP1_to_SP4_points[-1]
        ]


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

    def path(self, a, b):  # Прокладываем путь
        self.del_all_point()  # Удаляем все точки
        if (a == '1 СП' and b == '5 СП') or (a == '5 СП' and b == '1 СП'):
            for point in self.From_SP1_to_SP5_points:
                self.mapview.add_marker(point)
        elif (a == '1 СП' and b == '4 СП') or (a == '4 СП' and b == '1 СП'):
            for point in self.From_SP1_to_SP4_points:
                self.mapview.add_marker(point)
        elif (a == '1 СП' and b == '3 СП') or (a == '3 СП' and b == '1 СП'):
            for point in self.From_SP1_to_SP3_points:
                self.mapview.add_marker(point)
        elif (a == '1 СП' and b == '2 СП') or (a == '2 СП' and b == '1 СП'):
            for point in self.From_SP1_to_SP2_points:
                self.mapview.add_marker(point)
        elif (a == '2 СП' and b == '5 СП') or (a == '5 СП' and b == '2 СП'):
            for point in self.From_SP2_to_SP5_points:
                self.mapview.add_marker(point)
        elif (a == '2 СП' and b == '4 СП') or (a == '4 СП' and b == '2 СП'):
            for point in self.From_SP2_to_SP4_points:
                self.mapview.add_marker(point)
        elif (a == '2 СП' and b == '3 СП') or (a == '3 СП' and b == '2 СП'):
            for point in self.From_SP2_to_SP3_points:
                self.mapview.add_marker(point)
        elif (a == '3 СП' and b == '4 СП') or (a == '4 СП' and b == '3 СП'):
            for point in self.From_SP3_to_SP4_points:
                self.mapview.add_marker(point)
        elif (a == '3 СП' and b == '5 СП') or (a == '5 СП' and b == '3 СП'):
            for point in self.From_SP3_to_SP5_points:
                self.mapview.add_marker(point)
        elif (a == '4 СП' and b == '5 СП') or (a == '5 СП' and b == '4 СП'):
            for point in self.From_SP4_to_SP5_points:
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
            self.toasts.bad_path()
        elif str(self.screen.ids.From.text) == str(self.screen2.ids.To.text):
            self.toasts.bad_path()
        else:
            self.path(str(self.screen.ids.From.text), str(self.screen2.ids.To.text))
            self.toasts.good_path(self.screen.ids.From.text, self.screen2.ids.To.text)
            
    def del_all_point(self):  # Удаление всех точек. Т.к. в модуле работы с картой нет метода для очистки маркеров,
        # приходится собственноручно их сохранять и удалять
        for point in [self.From_SP1_to_SP5_points, self.From_SP1_to_SP4_points, self.From_SP1_to_SP3_points,
                      self.From_SP1_to_SP2_points, self.From_SP2_to_SP5_points, self.From_SP2_to_SP4_points,
                      self.From_SP2_to_SP3_points, self.allSP_points]:
            for i in range(len(point)):
                self.mapview.remove_marker(point[i])

    def user_geolocation(self, **kwargs):  # Обновляем местоположение пользователя
        self.lat = kwargs['lat']
        self.lon = kwargs['lon']
        self.gps.set_lat_lon(self.lat, self.lon)  # Меняем состояние координат
        self.mapview.add_marker(MapMarker(lat=float(self.gps.get_lat_lon()[0]), lon=float(self.gps.get_lat_lon()[1]),
                                          source="location.me"))  # Ставим маркер по координатам пользователя

    def set_state_geolocation(self, *args):
        try:
            state = self.gps.set_state_geolocation()
            if state:
                gps.start(minTime=100, minDistance=0)
                self.btn_location.icon = 'location_on_true.png'
            elif not state:
                self.btn_location.icon = 'location_on_false.png'
                gps.stop()
        except NotImplementedError:
            pass

    def on_auth_status(self, general, status):
        print(general, status)


if __name__ == '__main__':
    app = MainApp()
    app.run()
