import flet as ft

def n_validate(input_field: ft.TextField):
    try:
        value = int(input_field.value)
        if value < 2:
            input_field.error_text = "Количество точек должно быть ≥ 2"
        else:
            input_field.error_text = None
    except ValueError:
        input_field.error_text = "Введите целое число"
    input_field.update()


def a_validate(input_field: ft.TextField):
    try:
        value = float(input_field.value)
        if value <= 0:
            input_field.error_text = "a должно быть > 0"
        else:
            input_field.error_text = None
    except ValueError:
        input_field.error_text = "Введите целое число"
    input_field.update()



def k1_validate(k1_field: ft.TextField, k_field: ft.TextField):
    try:
        value = float(k1_field.value)
        if value <= 0:
            k1_field.error_text = "k1 должно быть > 0"
        else:
            k1_field.error_text = None
    except ValueError:
        k1_field.error_text = "Введите число"

    k1_field.update()
    k_validate(k_field, k1_field)


def k_validate(k_field: ft.TextField, k1_field: ft.TextField):
    try:
        k = float(k_field.value)
        k1 = float(k1_field.value)

        if k <= k1:
            k_field.error_text = f"k должно быть > k1 ({k1})"
        else:
            k_field.error_text = None
    except ValueError:
        k_field.error_text = "Введите число"

    k_field.update()


def kd_validate(input_field: ft.TextField):
    try:
        value = float(input_field.value)
        if value <= 0:
            input_field.error_text = "kd должно быть > 0"
        else:
            input_field.error_text = None
    except ValueError:
        input_field.error_text = "Введите целое число"
    input_field.update()