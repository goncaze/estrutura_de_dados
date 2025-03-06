import flet as ft


def main(page: ft.Page):
    # Configurar tema de cor da page
    page.theme_mode = ft.ThemeMode.LIGHT
    # Setar largura da page
    page.window.width = 380
    # Setar altura da page
    page.window.height = 680

    txt_titulo = ft.Text(value="Lista Encadeada Simples", size=25)

    page.add(txt_titulo)

    # Atualizar/Recarregar a page
    page.update()


ft.app(main)
