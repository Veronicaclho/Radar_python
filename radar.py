v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é 80km/h')
multa = (v-80) * 7   
print('Você terá que pagar uma multa de R$ {:.2f}'.format(multa)) 
print('Tenha um excelente dia! Dirija com cuidado!')
