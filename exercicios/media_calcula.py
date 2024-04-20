nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

# Calcula o conceito com base na média
conceito = ""
if media >= 9:
    conceito = "A"
elif 8 <= media < 9:
    conceito = "B"
elif 7 <= media < 8:
    conceito = "C"
elif 6 <= media < 7:
    conceito = "D"
else:
    conceito = "E"

# Utiliza a correspondência de padrões para exibir o conceito
match conceito:
    case "A":
        print("Seu conceito é A")
    case "B":
        print("Seu conceito é B")
    case "C":
        print("Seu conceito é C")
    case "D":
        print("Seu conceito é D")
    case "E":
        print("Seu conceito é E")
