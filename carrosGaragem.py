while True :
  totaisDias = 0
  veiculoMaisTempo_nome= ''
  veiculoMaisTempo = 0
  totalVeiculos = 0
  modeloVeiculo = input('Digite o modelo do veiculo: ')
  TotalDiaVeiculo_str = input('Digite o total de dias que o veiculo vai ficar: ')

  if TotalDiaVeiculo_str.isdigit():
   totalDiaVeiculo = int(TotalDiaVeiculo_str)
  else:
    print('Digito invalido')
    break

  totaisDias += totalDiaVeiculo
  totalVeiculos += 1 

  if veiculoMaisTempo < totalDiaVeiculo:
    veiculoMaisTempo_nome = modeloVeiculo
    veiculoMaisTempo = totalDiaVeiculo

  continuar = input('Deseja cadastrar outro veiculo?(S/N)').strip().upper()
  if continuar != 'S':
    break

mediaDiaVeiculos = totalDiaVeiculo / totalVeiculos
print('-                                                             -')
print('Veiculos cadastrados com sucesso!!')
print('************************************')
print(f'O modelo que ficara mais tempo na garagem é o: {veiculoMaisTempo_nome} que vai ficar {veiculoMaisTempo}')
print(f'O numero de veiculos na garagem é de : {totalVeiculos}')
print(f'A media de dias dos veiculos é de: {mediaDiaVeiculos:.0f}')
print('-                                                             -')
