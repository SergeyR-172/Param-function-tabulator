import flet as ft

def show_programmer_info(page: ft.Page) -> None:
    info_dlg = ft.AlertDialog(
        title=ft.Text("Информация о программисте", size=22, weight=ft.FontWeight.BOLD, color="#1976d2"),
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Имя: SergeyR", size=16, color="#1976d2"),
                    ft.Text("Группа: ", size=16, color="#1976d2"),
                    ft.Text("Спецификации разработки:", size=18, weight=ft.FontWeight.BOLD, color="#1976d2"),
                    ft.Text("• Python 3.13", size=14, color="#1976d2"),
                    ft.Text("• Flet Framework", size=14, color="#1976d2"),
                    ft.Text("• Matplotlib для построения графиков", size=14, color="#1976d2"),
                    ft.Text("• NumPy для вычислений", size=14, color="#1976d2"),
                ],
                spacing=15,
                tight=True
            ),
            padding=ft.Padding(20, 20, 20, 20),
            width=450,
            border_radius=8,
            bgcolor="#f8f9fa"
        ),
        actions=[
            ft.TextButton(
                "Закрыть",
                on_click=lambda e: page.close(info_dlg),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    padding=ft.Padding(15, 10, 15, 10)
                )
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        shape=ft.RoundedRectangleBorder(radius=8),
        bgcolor="#ffffff"
    )
    page.open(info_dlg)
    page.update() 


def show_error_dialog(page: ft.Page, message: str) -> None:
    dlg = ft.AlertDialog(
        title=ft.Text("Ошибка", size=22, weight=ft.FontWeight.BOLD, color="#d32f2f"),
        content=ft.Container(
            content=ft.Text(message, size=16, color="#d32f2f"),
            padding=ft.Padding(20, 20, 20, 20),
            border_radius=8,
            bgcolor="#ffebee"
        ),
        actions=[
            ft.TextButton(
                "Закрыть",
                on_click=lambda e: page.close(dlg),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    padding=ft.Padding(15, 10, 15, 10)
                )
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        shape=ft.RoundedRectangleBorder(radius=8),
        bgcolor="#ffffff"
    )
    page.open(dlg)
    page.update()