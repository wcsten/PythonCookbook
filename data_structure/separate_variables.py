"""
Problema

Você tem uma tupla ou sequência de N elementos que gostaria de desempacotar em
uma coleçāo de N variáveis.

"""


"""
Soluçāo

Qualquer sequência (ou iterável) pode ser desempacotada em variáveis por meio de
uma operaçāo simples de atribuiçāo. O único requisito é que a quantidade de variáveis
e a estrutura correspondam à sequência. Por exemplo:

"""

def separate_variables():
	data = ['ACME', 50, 91, (2012, 12, 21)]
	name, shares, prices, date = data

	print(name, shares, prices, date)


if __name__ == '__main__':
	separate_variables()
