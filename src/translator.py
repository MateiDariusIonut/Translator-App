from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
import torch

# Numele modelului de traducere multilingv (Facebook M2M100)
model_name = "facebook/m2m100_418M"

# Încărcăm tokenizer-ul (transformă textul în format numeric pentru model)
tokenizer = M2M100Tokenizer.from_pretrained(model_name)

# Încărcăm modelul propriu-zis de traducere
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

# Funcția care realizează traducerea propriu-zisă
def translate(text:str, input:str, output:str):

    langs_map = {'Română': 'ro',
                 'Engleză': 'en',
                 'Germană': 'de',
                 'Spaniolă': 'es',
                 'Franceză': 'fr',
                 'Italiană': 'it',
                 'Japoneză': 'ja',
                 'Greacă': 'el',
                 'Norvegiană': 'no',
                 'Suedeză': 'se',
                 'Olandeză': 'ol'}
    try:
        input, output = langs_map[input], langs_map[output]
    except KeyError:
        raise ValueError("Limba de intrare sau ieșire nu se află în lista limbilor valide.")

    src, tgt = input.lower(), output.lower()

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
            num_beams=10,  # Beam search pentru calitate mai bună
            max_length=1024  # Lungimea maximă a rezultatului
        )

    # Convertim rezultatul numeric înapoi în text
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text