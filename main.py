from src.translator import translate

# Importăm tkinter pentru interfața grafică
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import threading

def on_translate(input_text, combobox1, combobox2, output_text, translate_button, status_label):


    # Preluăm textul din zona de input
    text = input_text.get("1.0", tk.END).strip()

    limba_intrare = combobox1.get()
    limba_iesire = combobox2.get()

    # Dacă există text, realizăm traducerea
    if text:
        status_label['text'] = "Se traduce textul..."
        translate_button.configure(state="disabled")
        translated = translate(text, limba_intrare, limba_iesire)

        output_text.configure(state="normal")
        # Ștergem ce era anterior în output
        output_text.delete("1.0", tk.END)

        # Inserăm noua traducere
        output_text.insert(tk.END, translated)


        output_text.configure(state="disabled")
        translate_button.configure(state="normal")
        status_label['text'] = ''

def main():

    # Creăm fereastra principală a aplicației
    root = tk.Tk()
    root.title("Translator App")
    root.resizable(False, False)  # Nu permitem redimensionarea ferestrei

    style = ttk.Style(root)
    style.theme_use("clam")

    # Eticheta pentru textul de intrare
    input_label = tk.Label(root, text="Text intrare:")
    input_label.grid(row=0, column=0, sticky="n", padx=5)

    # Zonă scrollabilă pentru introducerea textului
    input_text = ScrolledText(root, wrap=tk.WORD,)
    input_text.grid(row=1, column=0, sticky="nsew", padx=5)
    input_text.configure(width=40, height=15)
    input_text.focus_set()

    # Frame intermediar pentru limbă și buton
    middle_frame = tk.Frame(root)
    middle_frame.grid(row=0, column=1, rowspan=3, padx=10)

    # Eticheta pentru selecția limbii
    language_label = tk.Label(middle_frame, text="Alege limba:")
    language_label.grid(row=0, column=1, padx=5, pady=5)

    # Lista direcțiilor de traducere disponibile
    directions = ["RO", "EN", "DE", "ES", "FR", "IT"]

    langauge_choice_frame = tk.Frame(middle_frame)
    langauge_choice_frame.grid(row=1, column=1, padx=5, pady=5)

    # Combobox pentru selectarea direcției
    combobox1 = ttk.Combobox(
        langauge_choice_frame,
        values=directions,
        width=7,
        justify="left",
        state="readonly"
    )
    combobox1.set("RO")  # Valoare implicită
    combobox1.grid(row=0, column=0, padx=5, pady=5)

    combobox2 = ttk.Combobox(
        langauge_choice_frame,
        values=directions,
        width=7,
        justify="right",
        state="readonly"
    )
    combobox2.set("EN")
    combobox2.grid(row=0, column=1, padx=5, pady=5)


    # Buton care declanșează traducerea
    translate_button = ttk.Button(
        middle_frame,
        text="Traducere",
        command=lambda: threading.Thread(target=on_translate, args=(input_text, combobox1, combobox2, output_text, translate_button,
                                                                    status_label)).start()
    )

    translate_button.grid(row=2, column=1, padx=5, pady=5)


    status_label = tk.Label(middle_frame)
    status_label.grid(row=3, column=1, sticky="nsew", pady=5)

    # Eticheta pentru textul de ieșire
    output_label = tk.Label(root, text="Text tradus:")
    output_label.grid(row=0, column=2, sticky="n", padx=5)

    # Zonă scrollabilă pentru afișarea traducerii
    output_text = ScrolledText(root, wrap=tk.WORD)
    output_text.grid(row=1, column=2, sticky="nsew", padx=5)
    output_text.configure(width=40, height=15)
    output_text.configure(state="disabled")

    # Pornim bucla principală a aplicației (aplicația rămâne deschisă)
    root.mainloop()

if __name__ == "__main__":
    main()