import flet as ft
from validators import n_validate, a_validate, k_validate, k1_validate, kd_validate


class ParamInput(ft.TextField):
    def __init__(self, label, value, width, helper_text, validate_input = None):
        super().__init__()
        self.label = label
        self.value = value
        self.width = width
        self.helper_text = helper_text

        if validate_input:
            self.on_change = lambda e: validate_input(self)


class GraphApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.n_input = ParamInput("Количество точек N (минимум 2)", "15", 200, "Введите целое число ≥ 2", n_validate)
        self.a_input = ParamInput("Параметр функции a (a > 0)", "1", 200, "Введите положительное число", a_validate)
        self.k1_input = ParamInput("Коэффициент для начального значения функции k1 (k1 > 0)", "0.1", 200, "Введите положительное число", lambda field: k1_validate(field, self.k_input))
        self.k_input = ParamInput(f"Коэффициент k (k > {self.k1_input.value})", "1", 200, f"Должно быть больше {self.k1_input.value}", lambda field: k_validate(field, self.k1_input))
        self.kd_input = ParamInput("Коэффициент для шага изменения аргумента (kd > 0)", "0.05", 200, "Введите положительное число", kd_validate)

        self.params_container = ft.Container(
            bgcolor=ft.Colors.AMBER_400,
            padding=20,
            border_radius=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[
                        self.n_input,
                        self.a_input,
                        self.kd_input
                    ]),
                    ft.Row(controls=[
                        self.k1_input,
                        self.k_input,
                    ])
                ]
            )
        )

        self.func_image_container = ft.Container(
            bgcolor=ft.Colors.BLUE_ACCENT,
            expand=True,
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
