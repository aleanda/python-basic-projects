inp = input("Inserisci una frase o il nome di un file:\n")

is_file = False

try:
    fhandle = open(inp)
    is_file = True
    text = fhandle.read()
except FileNotFoundError:
    text = inp

lines = text.splitlines()

array=text.split()
unique_words=[]
for word in array:
    if word not in unique_words:
        unique_words.append(word)

if is_file:
    print("Il numero di righe è:", len(lines))
    print("Il numero di parole è: ", len(array))
    print("Il numero di caratteri è: ", len(text))
    print("Il numero di parole uniche è: ", len(unique_words))
else:
    print("Hai inserito una sola riga")
    print("Il numero di parole è: ", len(array))
    print("Il numero di caratteri è: ", len(text))

longest_word = ""
max_len_word = 0

for word in unique_words:
    if len(word) > max_len_word:
        max_len_word = len(word)
        longest_word = word

words_max_len=[]
for word in unique_words:
    if len(word)== max_len_word:
        words_max_len.append(word)

if len(words_max_len)>1:
    print("Le parole con la lunghezza maggiore sono ", words_max_len)
    print("La lunghezza maggiore è ", max_len_word)
else:
    print("La parola più lunga è", longest_word, "e la sua lunghezza è", max_len_word)
