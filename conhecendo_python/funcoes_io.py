nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")
print(nome, idade)

nome = "Rogério"
sobrenome = "Tiúma"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n") #trocando o final
print(nome, sobrenome, sep="#") #trocando separador

print("teste", end=" ")
print(nome, idade, end="...\n")