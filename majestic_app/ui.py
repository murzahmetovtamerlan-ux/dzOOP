import flet as ft
from datetime import datetime
from models import Player
from dm import DataManager


class Main(ft.Container):
    def __init__(self):
        super().__init__()
        self.dm = DataManager()
        self.time_in = datetime.now()
        self.username = 'student'

        self.status = ft.Text('Готово')
        self.search = ft.TextField(label='Поиск по нику', width=250)
        self.btn = ft.Button('Найти', on_click=self.find_player, width=100)
        self.sort_dd = ft.Dropdown(
            label='Сортировка',
            width=180,
            options=[
                ft.dropdown.Option('dmg', 'По урону'),
                ft.dropdown.Option('kills', 'По киллам'),
                ft.dropdown.Option('captures', 'По каптам'),
                ft.dropdown.Option('avg', 'По ср. урону')],
            value='dmg',
            on_select=self.change_sort)
        self.table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text('Игрок')),
                ft.DataColumn(ft.Text('Семья')),
                ft.DataColumn(ft.Text('Ср. урон')),
                ft.DataColumn(ft.Text('Общий урон')),
                ft.DataColumn(ft.Text('Убийства')),
                ft.DataColumn(ft.Text('Капты'))],
            rows=[])
        self.content = ft.Column(
            [
                ft.Text('Топ 10 игроков Memphis', size=24, weight=ft.FontWeight.BOLD),
                ft.Row([self.search, self.btn, self.sort_dd],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=15),
                self.status,
                self.table],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO)
        self.load()

    def load(self):
        data = [('Hunter Gucci', 'Gucci', 673, 84093, 239, 125),
            ('Exho Versetti', 'Versetti', 665, 90490, 197, 136),
            ('Finess Size', 'SIZE', 640, 115765, 183, 181),
            ('Stellar Blade', 'Blade', 615, 103391, 218, 168),
            ('Uno Corpses', 'CORPSES', 602, 90290, 243, 150),
            ('Hinnde Zangetsu', 'ZANGETSU CLAN', 582, 82671, 255, 142),
            ('Polaris Corpses', 'CORPSES', 563, 101835, 238, 181),
            ('Andru Blade', 'Blade', 553, 100641, 238, 182),
            ('Desolator Size', 'SIZE', 544, 108336, 276, 199),
            ('Chase Corpses', 'CORPSES', 489, 99222, 291, 203)] #данные если что не придуманы а взяты с сайта со статой mitsuki.hub
        for d in data:
            self.dm.add(Player(*d))
        self.show()

    def show(self):
        players = self.dm.sort(self.sort_dd.value)
        self.table.rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(p.nick)),
                ft.DataCell(ft.Text(p.family)),
                ft.DataCell(ft.Text(str(p.avg))),
                ft.DataCell(ft.Text(str(p.dmg))),
                ft.DataCell(ft.Text(str(p.kills))),
                ft.DataCell(ft.Text(str(p.captures)))
            ]) for p in players]

    def find_player(self, e):
        q = self.search.value.strip()
        if not q:
            self.show()
            self.status.value = 'Готово'
            self.status.color = None
            self.page.update()
            return
        found = self.dm.find(q)
        if found:
            self.table.rows = [
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(p.nick)),
                    ft.DataCell(ft.Text(p.family)),
                    ft.DataCell(ft.Text(str(p.avg))),
                    ft.DataCell(ft.Text(str(p.dmg))),
                    ft.DataCell(ft.Text(str(p.kills))),
                    ft.DataCell(ft.Text(str(p.captures)))
                ]) for p in found]
            if len(found) == 1:
                self.status.value = f'Найден: {found[0].nick}'
            else:
                self.status.value = f'Найдено: {len(found)} игроков'
            self.status.color = ft.Colors.GREEN
        else:
            self.status.value = 'Игрок не найден'
            self.status.color = ft.Colors.ORANGE
        self.page.update()

    def change_sort(self, e):
        self.show()
        self.status.value = f'Сортировка: {e.control.value}'
        self.page.update()

    def save_report(self):
        now = datetime.now()
        path = f'report_{now.strftime("%Y-%m-%d_%H-%M-%S")}.txt'
        with open(path, 'w', encoding='utf-8') as f:
            print('+---------+---------------------+---------------------+', file=f)
            print('| login   | time_in             | time_out            |', file=f)
            print('|---------|---------------------|---------------------|', file=f)
            print(f'| {self.username} | {self.time_in.strftime("%d.%m.%Y %H:%M:%S")} | {now.strftime("%d.%m.%Y %H:%M:%S")} |', file=f)
            print('+---------+---------------------+---------------------+', file=f)