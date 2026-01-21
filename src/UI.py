import tkinter as tk
import threading

import ttkbootstrap as tb
from ttkbootstrap.widgets.scrolled import ScrolledText
from ttkbootstrap.constants import *

from src.translator import translate

from src.custom_widgets import ImprovedComboBox

application = tb.Window(themename="darkly")


def on_translate(input_text, combobox1, combobox2, output_text, translate_button, status_label:tb.Label):

    # Preluăm textul din zona de input
    text = input_text.get("1.0", END).strip()

    limba_intrare = combobox1.get()
    limba_iesire = combobox2.get()

    # Dacă există text, realizăm traducerea
    if text:
        status_label['text'] = "Se traduce textul..."
        status_label.pack(pady=5)
        translate_button.configure(state="disabled")
        translated = translate(text, limba_intrare, limba_iesire)

        output_text.text.configure(state="normal")
        # Ștergem ce era anterior în output
        output_text.delete("1.0", END)

        # Inserăm noua traducere
        output_text.insert(tk.END, translated)


        output_text.text.configure(state="disabled")
        translate_button.configure(state="normal")
        status_label['text'] = ''
        status_label.pack(pady=0)

def swap_lang(combobox1, combobox2):
    l1: str = combobox1.get()
    l2: str = combobox2.get()

    combobox1.set(l2)
    combobox2.set(l1)

def run_gui():

    # Creăm fereastra principală a aplicației
    application.title("Traducător")
    application.resizable(False, False)  # Nu permitem redimensionarea ferestrei


    input_text_frame = tb.Labelframe(application, text="Text intrare", style='danger.TLabelframe')
    input_text_frame.grid(column=0, row=0, padx = 5, pady = 5)

    # Zonă scrollabilă pentru introducerea textului
    input_text = ScrolledText(input_text_frame, wrap=tk.WORD, bootstyle='danger')
    input_text.pack(padx=5, pady=5)
    input_text.text.configure(width=40, height=10)
    input_text.focus_set()

    # Frame intermediar pentru limbă și buton
    middle_frame = tb.Labelframe(application, text="Opțiuni", style='info.TLabelframe', labelanchor='n')
    middle_frame.grid(row=0, column=1, padx=10, rowspan=2)


    # Lista direcțiilor de traducere disponibile
    directions = ["Română", "Engleză", "Germană", "Spaniolă", "Franceză", "Italiană", 'Japoneză', 'Greacă', 'Suedeză', 'Norvegiană', 'Japoneză']

    langauge_choice_frame = tb.Frame(middle_frame)
    langauge_choice_frame.pack(padx=5, pady=5)

    # Eticheta pentru selecția limbii
    input_language_label = tb.Label(langauge_choice_frame, text="Limba de intrare", foreground="#3498DB")
    input_language_label.grid(row=0, column=0, padx=5, pady=(5,0))

    output_language_label = tb.Label(langauge_choice_frame, text="Limba de iesire", foreground="#3498DB")
    output_language_label.grid(row=0, column=1, padx=5, pady=(5,0))

    # Combobox pentru selectarea direcției
    combobox1 = ImprovedComboBox(
        langauge_choice_frame,
        values=directions,
        width=10,
        justify="left",
        bootstyle='info',
    )

    combobox1.set("Română")  # Valoare implicită
    combobox1.grid(row=1, column=0, padx=5, pady=5)

    combobox2 = ImprovedComboBox(
        langauge_choice_frame,
        values=directions,
        width=10,
        justify="left",
        bootstyle='info'
    )
    combobox2.set("Engleză")
    combobox2.grid(row=1, column=1, padx=5, pady=5)

    swap_language_button = tb.Button(
        middle_frame,
        text="Interschimbă limbile",
        command=lambda: swap_lang(combobox1, combobox2),
        bootstyle='info-outline',
        width=20
    )

    # Buton care declanșează traducerea
    translate_button = tb.Button(
        middle_frame,
        text="Traducere",
        command=lambda: threading.Thread(target=on_translate, args=(input_text, combobox1, combobox2, output_text, translate_button,
                                                                    status_label)).start(),
        bootstyle='info-outline',
        width=20
    )

    swap_language_button.pack(padx=5, pady=(5, 0))
    translate_button.pack(padx=5, pady=5)

    status_label = tb.Label(middle_frame)
    status_label.pack()

    output_text_frame = tb.Labelframe(application, text="Text iesire", style='success.TLabelframe', labelanchor='ne')
    output_text_frame.grid(column=3, row=0, padx=5, pady=5)

    # Zonă scrollabilă pentru afișarea traducerii
    output_text = ScrolledText(output_text_frame, wrap=WORD, bootstyle='success')
    output_text.grid(row=1, column=2, sticky="nsew", padx=5, pady = 5)
    output_text.text.configure(state="disabled",width=40, height=10)

    application.mainloop()