import flet as ft
import os

print(f"Diretório de trabalho atual: {os.getcwd()}")


def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()

    img = ft.Image(
        src=r"icon.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    page.add(img)

    page.update()


ft.app(target=main)
