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

    # Texto digitado para inserir na lista
    ttf_texto = ft.TextField()

    # Função
    def clk_inserir_final(e):
        # Obter texto digitado pelo usuário
        valor = ttf_texto.value
        # Inserir texto no final da lista
        ltw_lista.controls.append(ft.Text(value=valor))
        # Atualizar a página toda
        page.update()

    # Botão
    btn_inserir_final = ft.ElevatedButton(
        text="Inserir final", on_click=clk_inserir_final
    )

    # Função
    def clk_inserir_inicio(e):
        # Obter texto digitado pelo usuário
        valor = ttf_texto.value
        lista_aux = [ft.Text(value=valor)]
        # Inserir texto no final da lista
        ltw_lista.controls = lista_aux + ltw_lista.controls
        # Atualizar a página toda
        page.update()

    # Botão
    btn_inserir_inicio = ft.ElevatedButton(
        text="Inserir inicio", on_click=clk_inserir_inicio
    )

    page.add(
        txt_titulo,
        ltw_lista,
        ttf_texto,
        btn_inserir_inicio,
        btn_inserir_final,
    )

    # Atualizar/Recarregar a page
    page.update()


ft.app(main)
