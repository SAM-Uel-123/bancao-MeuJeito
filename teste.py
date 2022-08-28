import csv
dados = []
with open('contas.csv', 'r') as arq:
	re = csv.reader(arq)
	for a in re:
		if a:
			dados.append(a)
if dados:
	print(dados)
