velocidade_media = int(input('Digite a velocidade média do carro em Km/h: '))
distancia = int(input('Digite a distância do local em Km: '))

tempo_horas = distancia / velocidade_media

horas = int(tempo_horas)

print(f'Tempo estimado: {horas} horas.')