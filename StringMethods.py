nome = input("Digite seu nome: ")
print(nome)

print("Em lower case: \n" +nome.lower())

print(nome)
print("Em upper case: \n" +nome.upper())
print("\nSem os espaços: \n" +nome.strip())
print("\nPondo vírgula: \n" + nome.replace("da", ",da").strip())