import flet as ft

class ParamInput(ft.TextField):
    def __init__(self, label, value, helper_text):
        super().__init__()
        self.label = label
        self.value = value
        self.helper_text = helper_text

class GraphApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.params_container = ft.Container(
            bgcolor=ft.Colors.AMBER_400,
            expand=1,
            padding=20,
            border_radius=20,
        )

        self.func_image_container = ft.Container(
            bgcolor=ft.Colors.BLUE_ACCENT,
            expand=3,
            padding=20,
            border_radius=20,
        )

        self.table_container = ft.Container(
            bgcolor=ft.Colors.RED_ACCENT,
            expand=1,
            padding=20,
            border_radius=20,
        )

        self.graph_container = ft.Container(
            bgcolor=ft.Colors.CYAN_ACCENT,
            expand=3,
            padding=20,
            border_radius=20,
        )   

        self.controls = [
            ft.Row(expand=1,controls=[
                self.params_container,
                self.func_image_container
            ]),
            ft.Row(expand=2,controls=[
                self.table_container,
                self.graph_container
            ]),
        ]

def main(page: ft.Page):
    page.title = "Табулирование параметрической функции"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(GraphApp())
    page.update()

ft.app(main)
