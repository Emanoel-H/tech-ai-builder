def correct_text (txt):
    return " ".join(txt.upper().split())

nome = input("Digite seu nome: ")
print(correct_text(nome))

print("Em lower case: \n" +nome.lower())
print("Em upper case: \n" +nome.upper())
print("\nSem os espaços: \n" +nome.strip())
print("\nPondo vírgula: \n" + nome.replace("da", ",da").strip())

