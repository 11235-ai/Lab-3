# import tkinter as tk
# from tkinter import messagebox
# import random
# import string


# hex_input = input()
# dec_value = int(hex_input, 16)
    
# if dec_value == ValueError:
#     tk.messagebox.showwarning('Error', 'Введите корректное HEX-число!')
# import flet as ft  
# import string
# import random

# all_symbols = string.ascii_letters + string.digits

# #генератор ключа
# def generate_key(hex_value):
#     dec_value = str(int(hex_value, 16))
#     first_part = list(dec_value[:3])
#     finish_part = dec_value[-2:]
    
#     key = ''
#     for i in range(3):
#         sequence = random.choices(all_symbols, k=4)
#         sequence.insert(random.randint(0, 4), first_part[i])
#         key += ''.join(sequence)
#         if i == 2:
#             key += f' {finish_part}'
#             break
#         key += '-'
#     return key

# def main(page):
#     #установка размеров окна
#     page.window_width = 1089
#     page.window_height = 613
#     page.resizable = False  #запрет изменения размера окна

#     #убираем стандартные отступы для страницы
#     page.padding = 0
#     page.margin = 0

#     #стек для наложения элементов
#     stack = ft.Stack()

#     #фон
#     background_image = ft.Image(
#         src="/Users/tss/Documents/PYTHON LABS/LAB_3/Lab-3/image.png",
#         fit=ft.ImageFit.COVER,
#         width=1089,
#         height=613,
#     )
#     stack.controls.append(background_image)

#     #музыка
#     audio = ft.Audio(
#         src="/Users/tss/Documents/PYTHON LABS/LAB_3/Lab-3/26. Cloudy Park (Sky Area).mp3",
#         autoplay=True
#     )
#     stack.controls.append(audio)

#     #контейнер для выравнивания элементов
#     column = ft.Column(
#         alignment=ft.MainAxisAlignment.CENTER,  # Выравнивание по вертикали по центру
#         horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Выравнивание по горизонтали по центру
#         spacing=10  # Расстояние между элементами
#     )
#     column.controls.append(ft.Container(height=1)) 

#     #поле для ввода hex числа
#     hex_field = ft.TextField(
#         label="Enter your HEX number:",
#         bgcolor=ft.colors.BLACK, 
#         cursor_color="yellow",
#         hover_color="pink300", #цвет при наведении
#         border_color=ft.colors.YELLOW,
#         width=700,
#         text_align=ft.TextAlign.CENTER, #текст вводится из центра
#         border_radius=ft.border_radius.all(10), #закругления рамочки
#         color="yellow",
#     )

#     #кнопка для генерации результата
#     btn = ft.ElevatedButton(
#         "Generate Key", 
#         on_click=lambda e: btn_click(e), 
#         width=400,
#         bgcolor=ft.colors.YELLOW_300, 
#         color=ft.colors.PINK_300,
#         style=ft.ButtonStyle(
#             overlay_color=ft.colors.YELLOW_500, 
#             padding=ft.Padding(top=15, right=20, bottom=15, left=20), #настройка внутренних отступов
#             shape=ft.RoundedRectangleBorder(radius=10)  #закругление углов
#         )
#     )

#     #кнопка для отображения результата
#     result_button = ft.ElevatedButton(
#         "YOUR KEY WILL APPEAR HERE", 
#         bgcolor=ft.colors.BLUE_100,
#         width=300,
#         color=ft.colors.PINK_400,
#         style=ft.ButtonStyle(
#             padding=ft.Padding(top=15, right=20, bottom=15, left=20), 
#             shape=ft.RoundedRectangleBorder(radius=10)
#         )
#     )

#     #бработчик нажатия кнопки
#     def btn_click(e):
#         if not hex_field.value:
#             hex_field.error_text = "Please enter correct HEX number"
#             page.update()
#         else:
#             hex_value = hex_field.value
#             name = generate_key(hex_value)
#             result_button.text = f"{name}"  # обновить текст на кнопке результата
#             hex_field.error_text = ""  #очистить текст ошибки
#             page.update() 

#     #добавляем элементы в столбец
#     column.controls.append(hex_field)  #текстовое поле
#     column.controls.append(btn)  #кнопка генерации
#     column.controls.append(result_button)  #кнопка вывода результата

#     #добавляем контейнер с кнопками в стек
#     stack.controls.append(column)

#     #добавляем стек на страницу
#     page.controls.append(stack) 
#     page.update() 

# ft.app(target=main)

