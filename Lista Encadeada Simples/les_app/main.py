import flet as ft


def main(page: ft.Page):
    # Configurar tema de cor da page
    page.theme_mode = ft.ThemeMode.LIGHT
    # Setar largura da page
    page.window.width = 350
    # Setar altura da page
    page.window.height = 630

    # Atualizar/Recarregar a page
    page.update()


ft.app(main)
