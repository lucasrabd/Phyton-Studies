nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
conceito= str

if media >= 9:
 conceito = "A"
elif media >= 8 and media <= 8.9:
 conceito = "B"
elif media >= 7 and media <= 7.9:
 conceito = "C"
elif media >= 6 and media <= 6.9:
 conceito = "D"
else:
 conceito = "E"
    
match conceito:
    case "A":
        print ("Seu conceito é A")
    case "B":
        print ("Seu conceito é B")
    case "C":
        print ("Seu conceito é C")
    case "D":
        print ("Seu conceito é D")
    case "E":
        print ("Seu conceito é E")