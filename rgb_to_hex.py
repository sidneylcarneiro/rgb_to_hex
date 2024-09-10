import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


def update_color():
    """
    Atualiza a cor de visualização 
    com base nos valores RGB ajustados pelos deslizadores.
    O código hexadecimal da cor resultante 
    é exibido no campo de entrada e na área de visualização.
    Também atualiza os labels com os valores numéricos RGB.
    """
    r = int(red_scale.get())
    g = int(green_scale.get())
    b = int(blue_scale.get())
    # Fstring converte RGB em HEX
    hex_color = f"#{r:02X}{g:02X}{b:02X}"
    color_display.configure(fg_color=hex_color)
    color_entry.delete(0, tk.END)
    color_entry.insert(0, hex_color)
    
    # Atualiza os valores numéricos dos labels
    red_label.configure(text=f"Vermelho: {r}")
    green_label.configure(text=f"Verde: {g}")
    blue_label.configure(text=f"Azul: {b}")


def copy_to_clipboard():
    """
    Copia o código hexadecimal da cor atual 
    para a área de transferência e exibe uma mensagem de sucesso.
    """
    hex_color = color_entry.get()
    root.clipboard_clear()
    root.clipboard_append(hex_color)
    root.update()  # Mantém o código copiado na área de transferência
    # Exibe uma mensagem de sucesso
    messagebox.showinfo(
        "Info",
        "Código hexadecimal copiado para a área de transferência")


# Criando a janela principal
root = ctk.CTk()

# Configurando a janela principal
root.title("Selecionador de Cor RGB")
root.geometry("500x400")

# Frame para o campo de entrada e botão
entry_frame = ctk.CTkFrame(root)
entry_frame.place(relx=0.04, rely=0.03, relwidth=0.92, relheight=0.1)

# Campo de entrada para o código hexadecimal
color_entry = ctk.CTkEntry(
    entry_frame, 
    placeholder_text="Código hexadecimal")
color_entry.place(relx=0, rely=0, relwidth=0.7, relheight=1)

# Botão para copiar o código hexadecimal
copy_button = ctk.CTkButton(
    entry_frame, 
    text="Copiar Código", 
    command=copy_to_clipboard)
copy_button.place(relx=0.72, rely=0, relwidth=0.28, relheight=1)

# Área de visualização da cor
color_display = ctk.CTkLabel(
    root, 
    text="Cor de Visualização", 
    corner_radius=10)
color_display.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.3)

# Deslizadores para ajustar os valores RGB
red_scale = ctk.CTkSlider(
    root, 
    from_=0, to=255, 
    command=lambda x: update_color())
red_scale.set(0)
red_scale.place(relx=0.04, rely=0.5, relwidth=0.92, relheight=0.05)
red_label = ctk.CTkLabel(root, text="Vermelho: 0")
red_label.place(relx=0.04, rely=0.55)

green_scale = ctk.CTkSlider(
    root, 
    from_=0, to=255, 
    command=lambda x: update_color())
green_scale.set(0)
green_scale.place(relx=0.04, rely=0.62, relwidth=0.92, relheight=0.05)
green_label = ctk.CTkLabel(root, text="Verde: 0")
green_label.place(relx=0.04, rely=0.67)

blue_scale = ctk.CTkSlider(
    root, 
    from_=0, to=255, 
    command=lambda x: update_color())
blue_scale.set(0)
blue_scale.place(relx=0.04, rely=0.74, relwidth=0.92, relheight=0.05)
blue_label = ctk.CTkLabel(root, text="Azul: 0")
blue_label.place(relx=0.04, rely=0.79)

# Atualiza a cor inicial
update_color()

# Iniciando o loop principal do Tkinter
root.mainloop()
