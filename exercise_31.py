# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


for dictionary in perguntas:
    print(dictionary['Pergunta'])
    for i,opcao in enumerate(dictionary['Opções']):
        print(f'{i}) {opcao}')
    answer = input('Type the correct answer: ')
    if(dictionary['Opções'][int(answer)] == dictionary['Resposta']):
        print('Correct Answer!!')
        print()
    else:
        print('Wrong answer T-T')
    