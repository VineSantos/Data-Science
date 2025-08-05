import tkinter as tk
import random

def move_button(event):
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    button_width = no_btn.winfo_width()
    button_height = no_btn.winfo_height()
    
    x = random.randint(0, window_width - button_width)
    y = random.randint(0, window_height - button_height)
    
    no_btn.place(x=x, y=y)

def confirm():
    response_label.config(text="Você me fez a pessoa mais feliz do mundo!")
    yes_btn.config(state="disabled")
    no_btn.config(state="disabled")

root = tk.Tk()
root.title("Quer namorar comigo?")

# Centralizar a janela
root.geometry("400x200")
root.eval('tk::PlaceWindow . center')

# Criando o layout
question_label = tk.Label(root, text="Quer namorar comigo?", font=("Helvetica", 16))
question_label.pack(pady=20)

yes_btn = tk.Button(root, text="Sim", font=("Helvetica", 12), command=confirm)
yes_btn.pack(side="left", padx=20, pady=20)

no_btn = tk.Button(root, text="Não", font=("Helvetica", 12))
no_btn.pack(side="right", padx=20, pady=20)

no_btn.bind("<Enter>", move_button)

response_label = tk.Label(root, text="", font=("Helvetica", 14))
response_label.pack(pady=20)

root.mainloop()
