notaMax = 10
diasLimite = 7
entrega = str(input("Informe o tipo de entrega: "))
diasAtraso = int(input("Digite quantos dias de atraso: "))
entrega = entrega.lower() #garantindo que a resposta sempre será formada por todas as letras minúsculas.
if (entrega == "parcial"):
    for i in range(1, diasAtraso+1):
        if(i == 1):
            notaMax -= 1.5
        elif(i == diasLimite+1):
            notaMax = 0
            break
        else:
            notaMax -= 0.5
if (entrega == "final"):
    for i in range(1, diasAtraso+1):
        notaMax -= 1
        if(i == diasLimite+1):
            notaMax = 0
            break
print("A nota final do aluno foi: %.2f" % notaMax)