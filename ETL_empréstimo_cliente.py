"""1 - EXTRATION:
Here we'll import csv library, build a archive extract """
import csv

arquivo = open("score_clientes.csv")
scores = csv.reader(arquivo)

"""2 - TRANSFORM"""
table = list()

for score in scores:
    
    if score[2] == "alto":
        score.append("Empréstimo concedido a 10% /mês")
        table.append(score)
        print(score)

    elif score[2] == "médio":
        score.append("Empréstimo concedido a 20% /mês")
        table.append(score)
        print(score)

    elif score[2] == "baixo":
        score.append("Empréstimo negado, consulte seu gerente.")
        table.append(score)
        print(score)
  