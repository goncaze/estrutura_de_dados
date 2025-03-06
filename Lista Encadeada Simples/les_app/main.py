import flet as ft


def main(page: ft.Page):
    # Configurar tema de cor da page
    page.theme_mode = ft.ThemeMode.LIGHT
    # Setar largura da page
    page.window.width = 380
    # Setar altura da page
    page.window.height = 680

    # Título da aplicação
    txt_titulo = ft.Text(value="Lista Encadeada Simples", size=25)

    # Criar uma lista em FLET
    ltw_lista = ft.ListView(expand=1, auto_scroll=True)

    ttf_texto = ft.TextField()

    def clk_inserir_final(e):
        valor = ttf_texto.value
        ltw_lista.controls.append(ft.Text(value=valor))
        page.update()

    btn_inserir_final = ft.ElevatedButton(
        text="Inserir final", on_click=clk_inserir_final
    )

    page.add(txt_titulo, ltw_lista, ttf_texto, btn_inserir_final)

    # Atualizar/Recarregar a page
    page.update()


ft.app(main)
