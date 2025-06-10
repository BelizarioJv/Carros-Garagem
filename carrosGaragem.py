modeloVeiculo_Matriz = []
numeroDias_Matriz = []
totaisDias = 0
veiculoMaisTempo_nome= ''
veiculoMaisTempo = 0
totalVeiculos = 0
totalDiaVeiculo = 0

while True :
  modeloVeiculo = input('Digite o modelo do veiculo')
  TotalDiaVeiculo_str = input('Digite o total de dias que o veiculo vai ficar')

  if TotalDiaVeiculo_str.isdigit():
    totalDiaVeiculo = int(TotalDiaVeiculo_str)
  else:
    print('Digito invalido')
    break
  

  if veiculoMaisTempo < totalDiaVeiculo:
    veiculoMaisTempo_nome = modeloVeiculo
    veiculoMaisTempo = totalDiaVeiculo

    modeloVeiculo_Matriz.insert(0,veiculoMaisTempo_nome)
    numeroDias_Matriz.insert(0,veiculoMaisTempo)
  else:
    modeloVeiculo_Matriz.append([modeloVeiculo])
    numeroDias_Matriz.append([totalDiaVeiculo])
  

  continuar = input('Deseja cadastrar outro veiculo?(S/N)').strip().upper()
  if continuar != 'S':
    break
  mediaDiaVeiculos = sum(numeroDias_Matriz)/ len(numeroDias_Matriz)
print('-                                                             -')
print('Veiculos cadastrados com sucesso!!')
print('************************************')
print(f'A soma total de dias dos veiculos e:{(sum(numeroDias_Matriz))}')
print(f'O modelo que ficara mais tempo na garagem e o:{modeloVeiculo_Matriz[0]} com um toal de {numeroDias_Matriz[0]}')
print(f'O numero de veiculos na garagem e de : {len(modeloVeiculo_Matriz)}')
print(f'A media de dias dos veiculos e de:{mediaDiaVeiculos}')
print('-                                                             -')
   




