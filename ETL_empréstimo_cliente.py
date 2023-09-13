"""
1 - EXTRACTION:
Here we'll import csv to read and write the file builded at Excel
The program will be Extract whole information tha file.csv 
"""

import csv

arquivo = open("score_clientes.csv") 
scores = csv.reader(arquivo) #create a new object scores to read the file

"""
2 - TRANSFORM:
First we create a list that 'll be store whole modifies does at the table
The Code, 'll check if score's client is high, medium or low, then 'll make a decision, 
to lend money and especifing the lend's tax.
"""
table = list() #Create a list to store whole information

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
    
    else:
        score.append("decisao")
        table.append(score)

"""
3 - LOAD:
At last, will be create a new file, with the new decisions
"""

arquivo_novo = open('decisao.csv', 'w', newline='') #create a new archieve 'decisao.csv' which was created to write
decisao = csv.writer(arquivo_novo, delimiter=',') #create a new object 'decisao' that write at 'decisao.csv'
decisao.writerows(table) #Write all modifies at the table