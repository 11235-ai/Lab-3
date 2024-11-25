import tkinter as tk
from tkinter import messagebox
import random
import string
import time 
import pygame


letters_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers_list = '0123456789'
Sound_track = "PvsZ.mp3"


def animate_label():

    colors = ["darkblue", "red", "purple", "orange", "blue", "gray"]
    current_color = label_title.cget("fg")
    current_index = colors.index(current_color)
    next_index = (current_index + 1) % len(colors)
    next_color = colors[next_index]
    label_title.config(fg=next_color)
    window.after(500, animate_label)


    
def generate_key():

    hex_input = entry_hex.get().strip().upper()

    if not all(c in '0123456789abcdefABCDEF' for c in hex_input):
        tk.messagebox.showwarning('Error', 'Введите корректное HEX-число!')
        return

    dec_value = int(hex_input, 16)
    Dec = str(dec_value)

    if len(Dec) < 5:
        tk.messagebox.showwarning('Error', 
        'HEX-число должно содержать как минимум 5 значащих символов!')
    if len(Dec) > 6:
        tk.messagebox.showwarning('Error', 
        'HEX-число должно содержать как максимум 5 значащих символов!')
        return

    # Генерация 
    def generate_block(cod_char, k=3):
    
        block = random.choices(letters_list + numbers_list, k=k)
        block.insert(random.randint(0, len(block)), cod_char)
        return ''.join(block)


    block_1 = generate_block(Dec[0])  
    block_2 = generate_block(Dec[1])  
    block_3 = generate_block(Dec[2]) 
    
    final_key = f"{block_1}-{block_2}-{block_3} {Dec[-2:]}"
    entry_result.delete(0, tk.END)
    entry_result.insert(0, final_key)


window = tk.Tk()
window.geometry("598x450")
bg_img = tk.PhotoImage(file='FondoPZP.png')

#Star
lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

label_title = tk.Label(window, text="Key Generator", font=("Arial", 20, "bold"), 
                       fg="gray", bg="green")
label_title.place(x=200, y=90)

#Bход
label_hex = tk.Label(window, text="Введите HEX-число:", font=("Arial", 14),
                     fg="darkgray", bg="green")
label_hex.place(x=205, y=155)
entry_hex = tk.Entry(window, font=("Arial", 14), width=20,relief="sunken", 
                     borderwidth=3)
entry_hex.place(x=182, y=200)

#Генерации ключа
btn_generate = tk.Button(window, text="Сгенерировать ключ", font=("Arial", 14),
                         fg="darkgray", bg="green", relief="raised", borderwidth=10, 
                         command=generate_key)
btn_generate.place(x=188, y=240)

#Результат
label_result = tk.Label(window, text="Сгенерированный ключ:", 
                        font=("Arial", 14),fg="darkgray", bg="green")
label_result.place(x=186, y=305)
entry_result = tk.Entry(window, font=("Arial", 14), width=35, justify="center", 
                        relief="sunken", borderwidth=3)
entry_result.place(x=110, y=345)


pygame.mixer.init()
pygame.mixer.music.load(Sound_track)
pygame.mixer.music.play(-1)


animate_label()
window.mainloop()
