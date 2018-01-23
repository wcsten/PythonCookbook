"""

Problema

Você deve desempacotar N elementos, mas o iterável pode ter mais de N elementos,
causando uma exceçāo igual a ˜too many values to unpack" (valores demais para desempacotar)

"""


"""

Soluçāo

As "expressões com asterisco" do Python podem ser utilizadas para solucionar esse
problema. Por exemplo, suponha que você dê um curso e que, no final do semestre,
decida que irá descartar as notas da primeira e da última lições da casa e tirará
a média somente das restantes. Se houver apenas quatro lições, você poderá simplesmente
desempacotar todas elas, mas e se houver 24? Uma expressāo com asterisco facilita essa tarefa.


"""

def drop_first_last():
	"""
	Funçāo que retorna os termos centrais da lista ignorando o primeiro e o ultimo termo.
	"""
	grades = [ 8, 7, 10, 5, 9, 3]

	first, *middle, last = grades
	print(middle)


"""

Como outro caso de uso, suponha que você tenha registros de usuários contendo um nome e o
endereço de email, seguidos por uma quantidade arbitrária de números de telefone. Os registros
podem ser desempacotados desta maneira:

"""

def drop_first_second():
	"""
	Funçāo que retorna os termos finais da lista ignorando o primeiro e o segundo termo.
	"""
	record = ['Gabriel', 'gabriel@example.com', '99999-9999', '98888-8888']

	name, email, *phone_numbers = record
	print(phone_numbers)


"""

A variável com asterisco também pode ser a primeira da lista. Por exemplo, digamos
que você tenha uam sequência de valores que representam as vendas de sua empresa
nos últimos oito trimestres. Se quiser ver como o trimestre mais recente se compara em relação à média
dos primeiros sete trimestres, você pode fazer algo como:

"""

def quarter_comparison():
	#TODO
	sales_record = [10, 8, 7, 15, 13, 2, 4, 3]

	*trailling_gtrs, current_qtr = sales_record
	trailling_avg = sum(trailling_gtrs) / len(trailling_gtrs)





if __name__ == '__main__':
	drop_first_last()
	drop_first_second()





