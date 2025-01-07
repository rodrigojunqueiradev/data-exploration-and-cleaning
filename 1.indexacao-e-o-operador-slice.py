"""
Este código foi utilizado como base de estudos de alguns conceitos básicos da linguagem Python, para fundamentar a exploração final do projeto.
"""

# Listas: Uma lista é uma coleção ordenada mutável que pode conter qualquer tipo de dado
example_list = list(range(1,6))
print(example_list)
print(example_list[0])
print(example_list[1])
print(example_list[-1])
print(example_list[-2])
print(example_list[:3])
print(example_list[:2])
example_list[0] = "some string"
print(example_list)
print(example_list[0])

# Dicionários: Um dicionário é uma coleção não ordenada de pares "chave:valor"
example_dict = {'apples':5, 'oranges':8}
print(example_dict)
print(example_dict['apples'])
example_dict['bananas'] = 13
print(example_dict)
print(example_dict['bananas'])
