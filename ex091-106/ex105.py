# Faça um programa que tenha uma função notas que pode receber várias notas de alunos e vai retornar um dicionário com as informações: -A quantidade de notas -A maior nota -A menor nota -A média da turma -A situação 

def notas(*nota, sit = False): 
    aluno = {}
    aluno['Total'] = len(nota)
    aluno['Maior'] = max(nota)
    aluno['Menor'] = min(nota)
    aluno['Média'] = sum(nota) / len(nota)
    if sit == True:
        if aluno['Média'] >= 7:
            aluno['situação'] = 'BOA'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


resp = notas(5.5,9.5,5,6.5, sit = True)
print('-'*20)
print(resp)