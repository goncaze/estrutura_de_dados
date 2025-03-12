import flet as ft


def main(page: ft.Page):
    # Configurar tema de cor da page
    page.theme_mode = ft.ThemeMode.LIGHT
    # Setar largura da page
    page.window.width = 400
    # Setar altura da page
    page.window.height = 680

    # Título da aplicação
    txt_titulo = ft.Text(value="Lista Encadeada Simples", size=28)

    # Criar uma lista em FLET
    ltw_lista = ft.ListView(expand=1, auto_scroll=True)

    # Comprimento da lista
    txt_comprimento = ft.Text(value="Comprimento: ", size=23)

    # Texto digitado para inserir na lista
    ttf_texto = ft.TextField()

    # Função para recontar os índices da lista
    def recontar_indices():
        i = 0
        for elemento in ltw_lista.controls:
            elemento.controls[0].value = i
            i += 1

    # Função
    def clk_inserir_final(e):
        # Obter texto digitado pelo usuário
        valor = ttf_texto.value
        # Inserir texto no final da lista
        ltw_lista.controls.append(
            ft.Row(
                controls=[
                    ft.Text(value=len(ltw_lista.controls), size=20),
                    ft.Text(value=valor, size=20),
                ]
            )
        )
        txt_comprimento.value = f"Comprimento: {len(ltw_lista.controls)}"
        recontar_indices()
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
        lista_aux = [ft.Text(value=valor, size=20)]
        # Inserir novo texto no inicio da lista
        ltw_lista.controls = lista_aux + ltw_lista.controls
        txt_comprimento.value = f"Comprimento: {len(ltw_lista.controls)}"
        recontar_indices()
        # Atualizar a página toda
        page.update()

    # Botão
    btn_inserir_inicio = ft.ElevatedButton(
        text="Inserir inicio", on_click=clk_inserir_inicio
    )

    # Função
    def clk_remover_final(e):
        # remover texto no final da lista
        ltw_lista.controls.pop()
        txt_comprimento.value = f"Comprimento: {len(ltw_lista.controls)}"
        recontar_indices()
        txt_comprimento.value = f"Comprimento: {len(ltw_lista.controls)}"
        recontar_indices()
        # Atualizar a página toda
        page.update()

    # Botão
    btn_remover_final = ft.ElevatedButton(
        text="Remover final", on_click=clk_remover_final
    )

    # Criar linha para alinhar botões
    linha = ft.Row(
        wrap=True, controls=[btn_inserir_inicio, btn_inserir_final, btn_remover_final]
    )

    page.add(
        txt_titulo,
        txt_comprimento,
        ltw_lista,
        ttf_texto,
        linha,
    )

    # Atualizar/Recarregar a page
    page.update()


ft.app(main)
