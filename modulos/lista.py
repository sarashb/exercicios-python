# Exercicio de frutas pedidas em uma lista
frutas =['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelao']

fruta_pedida = input('Qual a fruta que deseja consultar?')

if (fruta_pedida in frutas):
    print ('Sim, temos a fruta.')
else: 
    print ('Não temos a fruta')

# Retorna o menor valor de uma lista
print (min(frutas))

# Retorna a quantidade de itens na lista
print (len(frutas))