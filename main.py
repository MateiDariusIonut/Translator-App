# Importăm clasele necesare din biblioteca transformers pentru traducere
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# Importăm PyTorch pentru rularea modelului
import torch

# Importăm tkinter pentru interfața grafică
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


# Numele modelului de traducere multilingv (Facebook M2M100)
model_name = "facebook/m2m100_418M"

# Încărcăm tokenizer-ul (transformă textul în format numeric pentru model)
tokenizer = M2M100Tokenizer.from_pretrained(model_name)

# Încărcăm modelul propriu-zis de traducere
model = M2M100ForConditionalGeneration.from_pretrained(model_name)


# Funcția care realizează traducerea propriu-zisă
def translate(text, direction):
    """
    text = textul introdus de utilizator
    direction = direcția de traducere aleasă (ex: EN -> DE)
    """

    # Stabilim limbile sursă și țintă în funcție de direcție
    if direction == "EN -> DE":
        src, tgt = "en", "de"
    elif direction == "DE -> EN":
        src, tgt = "de", "en"
    elif direction == "EN -> RO":
        src, tgt = "en", "ro"
    elif direction == "RO -> EN":
        src, tgt = "ro", "en"
    elif direction == "RO -> DE":
        src, tgt = "ro", "de"
    elif direction == "DE -> RO":
        src, tgt = "de", "ro"
    else:
        return text  # fallback dacă apare o situație neprevăzută

    # Setăm limba sursă pentru tokenizer
    tokenizer.src_lang = src

    # Convertim textul în format utilizabil de model
    inputs = tokenizer(text, return_tensors="pt")

    # Dezactivăm calculul gradientului (nu antrenăm, doar folosim modelul)
    with torch.no_grad():
        # Generăm traducerea folosind modelul
        translated_tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.get_lang_id(tgt),  # forțăm limba țintă
            num_beams=5,         # beam search pentru calitate mai bună
            max_length=512      # lungimea maximă a rezultatului
        )

    # Convertim rezultatul numeric înapoi în text
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text


# Creăm fereastra principală a aplicației
root = tk.Tk()
root.title("Translator App")
root.resizable(False, False)  # Nu permitem redimensionarea ferestrei


# ======== ZONA DE INPUT (TEXT DE INTRARE) ========

# Eticheta pentru textul de intrare
input_label = tk.Label(root, text="Text intrare:")
input_label.grid(row=0, column=0, sticky="n", padx=5)

# Zonă scrollabilă pentru introducerea textului
input_text = ScrolledText(root, wrap=tk.WORD)
input_text.grid(row=1, column=0, sticky="nsew", padx=5)
input_text.configure(width=40, height=15)


# ======== ZONA CENTRALĂ (SELECTARE LIMBĂ + BUTON) ========

# Frame intermediar pentru limbă și buton
middle_frame = tk.Frame(root)
middle_frame.grid(row=0, column=1, rowspan=3, padx=10)

# Eticheta pentru selecția limbii
language_label = tk.Label(middle_frame, text="Alege limba:")
language_label.grid(row=0, column=1, padx=5, pady=5)

# Lista direcțiilor de traducere disponibile
directions = ["EN -> DE", "DE -> EN", "EN -> RO", "RO -> EN", "RO -> DE", "DE -> RO"]

# Combobox pentru selectarea direcției
combobox = ttk.Combobox(
    middle_frame,
    values=directions,
    width=15,
    justify="center",
    state="readonly"
)
combobox.set("EN -> DE")  # Valoare implicită
combobox.grid(row=1, column=1, padx=5, pady=5)

# Buton care declanșează traducerea
translate_button = ttk.Button(
    middle_frame,
    text="Traducere",
    command=lambda: on_translate()
)
translate_button.grid(row=2, column=1, padx=5, pady=5)


# ======== ZONA DE OUTPUT (TEXT TRADUS) ========

# Eticheta pentru textul de ieșire
output_label = tk.Label(root, text="Text ieșire:")
output_label.grid(row=0, column=2, sticky="n", padx=5)

# Zonă scrollabilă pentru afișarea traducerii
output_text = ScrolledText(root, wrap=tk.WORD)
output_text.grid(row=1, column=2, sticky="nsew", padx=5)
output_text.configure(width=40, height=15)


# ======== FUNCȚIA APELATA LA APĂSAREA BUTONULUI ========

def on_translate():
    # Preluăm textul din zona de input
    text = input_text.get("1.0", tk.END).strip()

    # Preluăm direcția selectată
    direction = combobox.get()

    # Dacă există text, realizăm traducerea
    if text:
        translated = translate(text, direction)

        # Ștergem ce era anterior în output
        output_text.delete("1.0", tk.END)

        # Inserăm noua traducere
        output_text.insert(tk.END, translated)


# Pornim bucla principală a aplicației (aplicația rămâne deschisă)
root.mainloop()