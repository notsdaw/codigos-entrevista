def count_letter_a(string):
    count = string.lower().count('a')
    return count

texto = input("Digite uma string: ")
quantidade = count_letter_a(texto)

if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")