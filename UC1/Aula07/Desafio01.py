resultados = []
for i in range(5):
    try:
        n1 = float(input("Nota N1: "))
        n2 = float(input("Nota N2: "))
        optativa = float(input("Nota Optativa (-1 se não fez): "))

        nota_final_1 = n1
        nota_final_2 = n2

        # PONTO DE DECISÃO 1: Substituição (IF ANINHADO)
        if optativa != -1:
            # Se N1 é a menor nota (ou igual), substitui N1
            if nota_final_1 <= nota_final_2:
                nota_final_1 = optativa
            else: # Se N2 é menor
                nota_final_2 = optativa
                
        media = (nota_final_1 + nota_final_2) / 2.0

        # PONTO DE DECISÃO 2: Situação Final (IF/ELIF/ELSE)
        if media >= 6.0:
            situacao = "APROVADO"
        elif media < 3.0:
            situacao = "REPROVADO"
        else:
            situacao = "EM EXAME (Recuperação)"

        print(f"Resultado:\n  Média Final: {media:.1f}")
        print(f" Aluno {i + 1}: {situacao}\n")
        
        resultados.append(f" Aluno {i + 1}: {situacao}\n")

    except ValueError:
        print("ERRO: Digite apenas números válidos.")

for estudantes in resultados:
    print(estudantes)