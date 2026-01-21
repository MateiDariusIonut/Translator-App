# Aplicație de traducere

---

Această aplicație oferă posibilitatea utilizatorului de a traduce un text dintr-o selecție 
extensivă de limbi. Aceasta se folosește de modelul de inteligență artificială M2M100_418M, 
dezvoltat de compania META (Facebook). 

## Utilizare

---
Aplicația poate fii utilizată prin intermediul executabilului localizat în folder-ul 'dist'.

## Rulare

---

Utilizatorii avansați pot alege rularea codului sursă, mai precis al fișierului 'main.py'. 
Această acțiune se poate realiza fie prin intermediul unui emulator de terminal (cmd, Powershell, Bash, etc.), 
fie prin intermediul unui mediu de dezvoltare integrat, ce prezintă suport pentru
limbajul de programare python. Linia de comandă cu ajutorul căreia se poate rula codul sursă este:

    python main.py

Pentru rulare este nevoie de o versiune a limbajului de programare python, mai nouă decât versiunea 3.9. 
Totodată este necesară instalarea a mai multor module python prin intermediul uneltei 'pip'. Acestea sunt
listate în fișierul 'reuqirements.txt'.
Instalarea modulelor în mediul local de dezvoltare se poate realiza într-o manieră facilă prin intermediul liniei de 
comandă:

    pip install -r requirements.txt

Compilarea codului sursă se poate realiza prin intermediul uneltei 'pyinstaller', care se poate descărca cu ajutorul
uneltei pip. Linia de comandă folosită pentru compilarea codului sursă este:

    pyinstaller --onefile -w 'main.py'

## Cerințe de sistem minime 

---
- Procesor: Intel i5 generația 4 
- RAM: minim 4 GB
- Stocare: 1 GB liber
- Conexiune la internet: da

## Licență

---
MIT License
