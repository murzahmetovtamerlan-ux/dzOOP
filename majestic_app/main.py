import flet as ft
import atexit
from ui import Main


def main(page: ft.Page):
    page.title = 'Majestic RP'
    page.window.width = 950
    page.window.height = 650
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.padding = 20
    window = Main()
    page.add(window)
    atexit.register(window.save_report)


if __name__ == '__main__':
    ft.run(main)