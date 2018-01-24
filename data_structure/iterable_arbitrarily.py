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
    sales_record = [10, 8, 7, 15, 13, 2, 4, 3]

    *trailling_gtrs, current_qtr = sales_record
    trailling_avg = sum(trailling_gtrs) / len(trailling_gtrs)
    if trailling_avg > current_qtr:
        print(trailling_avg)
    else:
        print(current_qtr)


"""

A sintaxe com asterisco pode ser especialmente útil na iteração por uma sequência de
tuplas com rótulos:

"""

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 4, 5),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


"""

O desempacotamento com asterisco também pode ser útil se combinado com determinados
tipos de operações para processamento de strings, como, por exemplo, uma separação
(splitting). Por exemplo:

"""

def splitting():
    line = 'nobody:*:-2:2:Unprivileged User:/var/empty:/usr/bin/false'

    uname, *fields, homedir, sh = line.split(':')

    print(uname, homedir, sh)



"""

Pode-se imaginar que funções que executem uma separação como essa sejam criadas afim
de executar algum tipo de algoritimo recursivo inteligente. Por exemplo:

"""

def sums():
    items = [1, 10, 7, 4, 5, 9]
    head, *tail = items
    result = head + sum(tail) if tail else head
    print(result)


if __name__ == '__main__':
    drop_first_last()
    drop_first_second()
    quarter_comparison()
    splitting()
    sums()




