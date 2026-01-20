from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
import torch

# Numele modelului de traducere multilingv (Facebook M2M100)
model_name = "facebook/m2m100_418M"

# Încărcăm tokenizer-ul (transformă textul în format numeric pentru model)
tokenizer = M2M100Tokenizer.from_pretrained(model_name)

# Încărcăm modelul propriu-zis de traducere
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

# Funcția care realizează traducerea propriu-zisă
def translate(text, input, output):

    if input == "RO":
        src = 'ro'
    elif input == "EN":
        src = 'en'
    elif input == "DE":
        src = 'de'
    elif input == "ES":
        src = 'es'
    elif input == "FR":
        src = 'fr'
    elif input == "IT":
        src = 'it'
    else:
        raise ValueError("Invalid input.")

    if output == "RO":
        tgt = 'ro'
    elif output == "EN":
        tgt = 'en'
    elif output == "DE":
        tgt = 'de'
    elif output == "ES":
        tgt = 'es'
    elif output == "FR":
        tgt = 'fr'
    elif output == "IT":
        tgt = 'it'
    else:
        raise ValueError("Invalid output.")

    if tgt == src:
        return text

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
            num_beams=5,  # Beam search pentru calitate mai bună
            max_length=1024  # Lungimea maximă a rezultatului
        )

    # Convertim rezultatul numeric înapoi în text
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text