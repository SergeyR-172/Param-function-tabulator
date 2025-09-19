import flet as ft
from validators import n_validate, a_validate, k_validate, k1_validate, kd_validate
from calculator import function_compute
import os


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

        self.compute_button = ft.Button(text="Вычислить",on_click=self.on_compute)

        function_image = ft.Image(
            fit=ft.ImageFit.CONTAIN,
            repeat=ft.ImageRepeat.NO_REPEAT,
            gapless_playback=False,
        )
        if os.path.exists("function_image.png"):
            function_image.src = "function_image.png"

        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("N", weight=ft.FontWeight.BOLD, color="#1976d2")),
                ft.DataColumn(ft.Text("X", weight=ft.FontWeight.BOLD, color="#1976d2")),
                ft.DataColumn(ft.Text("Y", weight=ft.FontWeight.BOLD, color="#1976d2")),
            ],
            rows=[],
            heading_row_color="#e3f2fd",
            border=ft.border.all(1, "#000000"),
            border_radius=8,
            horizontal_lines=ft.border.BorderSide(1, "#000000"),
            vertical_lines=ft.border.BorderSide(1, "#000000"),
        )

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
                        self.compute_button,
                    ])
                ]
            )
        )

        self.func_image_container = ft.Container(
            bgcolor=ft.Colors.BLUE_ACCENT,
            expand=True,
            padding=20,
            border_radius=20,

            content=function_image
        )

        self.table_container = ft.Container(
            bgcolor=ft.Colors.RED_ACCENT,
            padding=20,
            border_radius=20,

            content=ft.Column(
                controls=[self.data_table],
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        self.graph_container = ft.Container(
            bgcolor=ft.Colors.CYAN_ACCENT,
            expand=True,
            padding=20,
            border_radius=20,
        )   
        

        self.controls = [
            ft.Row(expand=1,controls=[
                self.params_container,
                self.func_image_container
            ], vertical_alignment=ft.CrossAxisAlignment.STRETCH),
            ft.Row(expand=2,controls=[
                self.table_container,
                self.graph_container
            ], vertical_alignment=ft.CrossAxisAlignment.STRETCH),
        ]

        self.on_compute(None)


    def on_compute(self, e):             
        if True in [
            self.n_input.error_text,
            self.a_input.error_text,
            self.k1_input.error_text,
            self.k_input.error_text,
            self.kd_input.error_text]:
            return
        
        self.x_values, self.y_values = function_compute(
            int(self.n_input.value), 
            float(self.a_input.value), 
            float(self.k1_input.value), 
            float(self.k_input.value), 
            float(self.kd_input.value))

        
        for i in range(len(self.x_values)):
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(f"{i+1}")),
                        ft.DataCell(ft.Text(f"{self.x_values[i]:.2f}")),
                        ft.DataCell(ft.Text(f"{self.y_values[i]:.3f}")),
                    ]
                )
            )

def main(page: ft.Page):
    page.title = "Табулирование параметрической функции"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(GraphApp())
    page.update()

ft.app(main)
