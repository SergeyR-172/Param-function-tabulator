import flet as ft
from validators import n_validate, a_validate, k_validate, k1_validate, kd_validate
from calculator import function_compute
import os
from dialogs import show_programmer_info, show_error_dialog

import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart


# Унифицированные цвета для UI
PRIMARY_COLOR = "#1976d2"
SECONDARY_COLOR = "#f5f5f5"
ACCENT_COLOR = "#42a5f5"
TEXT_COLOR = "#212121"
BACKGROUND_COLOR = "#fafafa"
CONTAINER_COLOR = "#ffffff"
SUCCESS_COLOR = "#4caf50"
ERROR_COLOR = "#f44336"


class ParamInput(ft.TextField):
    def __init__(self, label, value, width, helper_text, validate_input = None):
        super().__init__()
        self.label = label
        self.value = value
        self.width = width
        self.helper_text = helper_text
        self.bgcolor = CONTAINER_COLOR
        self.border_color = PRIMARY_COLOR
        self.focused_border_color = ACCENT_COLOR
        self.border_radius = 8
        self.text_style = ft.TextStyle(color=TEXT_COLOR)

        if validate_input:
            self.on_change = lambda e: validate_input(self)


class GraphApp(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.scroll = ft.ScrollMode.AUTO


        self.n_input = ParamInput("Количество точек N (минимум 2)", "15", 200, "Введите целое число ≥ 2", n_validate)
        self.a_input = ParamInput("Параметр функции a (a > 0)", "1", 200, "Введите положительное число", a_validate)
        self.k1_input = ParamInput("Коэффициент для начального значения функции k1 (k1 > 0)", "0.1", 200, "Введите положительное число", lambda field: k1_validate(field, self.k_input))
        self.k_input = ParamInput(f"Коэффициент k (k > {self.k1_input.value})", "1", 200, f"Должно быть больше {self.k1_input.value}", lambda field: k_validate(field, self.k1_input))
        self.kd_input = ParamInput("Коэффициент для шага изменения аргумента (kd > 0)", "0.05", 200, "Введите положительное число", kd_validate)

        self.compute_button = ft.FilledButton(
            text="Вычислить",
            on_click=self.on_compute,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                bgcolor=PRIMARY_COLOR,
                color=ft.Colors.WHITE,
            ),
            width=150,
            height=50,
        )

        function_image = ft.Image(
            fit=ft.ImageFit.CONTAIN,
            expand=True,
            repeat=ft.ImageRepeat.NO_REPEAT,
            gapless_playback=False,
        )
        if os.path.exists("function_image.png"):
            function_image.src = "function_image.png"

        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("N", weight=ft.FontWeight.BOLD, color=PRIMARY_COLOR)),
                ft.DataColumn(ft.Text("X", weight=ft.FontWeight.BOLD, color=PRIMARY_COLOR)),
                ft.DataColumn(ft.Text("Y", weight=ft.FontWeight.BOLD, color=PRIMARY_COLOR)),
            ],
            rows=[],
            heading_row_color=ft.Colors.with_opacity(0.1, PRIMARY_COLOR),
            border=ft.border.all(1, "#e0e0e0"),
            border_radius=8,
            horizontal_lines=ft.border.BorderSide(0.5, "#e0e0e0"),
            vertical_lines=ft.border.BorderSide(0.5, "#e0e0e0"),
            data_row_min_height=30,
        )

        self.params_container = ft.Container(
            bgcolor=CONTAINER_COLOR,
            padding=20,
            margin=5,
            border_radius=15,
            height=240,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.Colors.with_opacity(0.2, "black"),
            ),
            content=ft.Column(
                controls=[
                    ft.Text("Параметры функции", size=18, weight=ft.FontWeight.W_500, color=PRIMARY_COLOR),
                    ft.Row(controls=[
                        self.n_input,
                        self.a_input,
                        self.kd_input
                    ]),
                    ft.Row(controls=[
                        self.k1_input,
                        self.k_input,
                        self.compute_button,
                    ],vertical_alignment=ft.CrossAxisAlignment.START)
                ],
                spacing=15,
            )
        )

        self.func_image_container = ft.Container(
            bgcolor=CONTAINER_COLOR,
            padding=20,
            margin=5,
            border_radius=15,
            height=240,
            expand=True,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.Colors.with_opacity(0.2, "black"),
            ),
            content=ft.Column(
                controls=[
                    ft.Text("Формула функции", size=18, weight=ft.FontWeight.W_500, color=PRIMARY_COLOR),
                    function_image
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        self.table_container = ft.Container(
            bgcolor=CONTAINER_COLOR,
            padding=20,
            margin=5,
            border_radius=15,
            height=800,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.Colors.with_opacity(0.2, "black"),
            ),
            content=ft.Column(
                controls=[
                    ft.Text("Таблица значений", size=18, weight=ft.FontWeight.W_500, color=PRIMARY_COLOR),
                    self.data_table
                ],
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        self.graph_container = ft.Container(
            bgcolor=CONTAINER_COLOR,
            padding=20,
            margin=5,
            border_radius=15,
            height=800,  # Set fixed height to 800
            expand=True,  # Allow horizontal expansion
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.Colors.with_opacity(0.2, "black"),
            ),
            content=ft.Column(
                controls=[
                    ft.Text("График функции", size=18, weight=ft.FontWeight.W_500, color=PRIMARY_COLOR),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        

        self.controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text("Табулирование параметрической функции", size=24, weight=ft.FontWeight.BOLD),
                    ft.TextButton(text="Информация о програмисте", icon=ft.Icons.INFO, on_click= lambda e: show_programmer_info(page))
                ]
            ),
            ft.Row(controls=[  # Remove expand=1 to prevent excessive height
                self.params_container,
                self.func_image_container
            ], vertical_alignment=ft.CrossAxisAlignment.START),  # Use START instead of STRETCH
            ft.Row(controls=[  # Remove expand=2 to prevent excessive height
                self.table_container,
                self.graph_container
            ], vertical_alignment=ft.CrossAxisAlignment.START),  # Use START instead of STRETCH
        ]

    def build_graph(self):
        fig, ax = plt.subplots(figsize=(10, 6), dpi=100)  # Adjust figure size to fit within 800px height container
        ax.plot(self.x_values, self.y_values, 'bo-', linewidth=2, markersize=4, color=PRIMARY_COLOR)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('Значение аргумента', fontsize=12, color=TEXT_COLOR)
        ax.set_ylabel('Значение функции', fontsize=12, color=TEXT_COLOR)
        ax.set_title(f'График параметрической функции Y = f(x, {self.a_input.value})', fontsize=14, pad=20, color=TEXT_COLOR)
        
        ax.tick_params(axis='both', which='major', labelsize=10, colors=TEXT_COLOR)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#e0e0e0')
        ax.spines['bottom'].set_color('#e0e0e0')
        
        fig.patch.set_facecolor(CONTAINER_COLOR)
        ax.set_facecolor(CONTAINER_COLOR)

        return fig


    def on_compute(self, e):             
        if True in [
            bool(self.n_input.error_text),
            bool(self.a_input.error_text),
            bool(self.k1_input.error_text),
            bool(self.k_input.error_text),
            bool(self.kd_input.error_text)]:

            show_error_dialog(self.page, "Неправильно заданы параметры функции")

            return
        
        self.x_values, self.y_values = function_compute(
            int(self.n_input.value), 
            float(self.a_input.value), 
            float(self.k1_input.value), 
            float(self.k_input.value), 
            float(self.kd_input.value))

        self.data_table.rows.clear()

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
        self.data_table.update()
        
        
        new_graph = MatplotlibChart(figure=self.build_graph(), expand=True)
        self.graph_container.content.controls = [
            ft.Text("График функции", size=18, weight=ft.FontWeight.W_500, color=PRIMARY_COLOR),
            new_graph
        ]
        self.graph_container.update()

def main(page: ft.Page):
    page.title = "Табулятор параметрических функций"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = BACKGROUND_COLOR
    page.padding = 20
    page.spacing = 0

    app = GraphApp(page)
    page.add(app)
    app.on_compute(None)

ft.app(main)
