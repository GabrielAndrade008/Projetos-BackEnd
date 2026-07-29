print('='*40)
print('Conversor de medidas')
print('='*40)

m=float(input('Digite um valor em Metros: '))

km = m/1000
hm = m/100 
dam = m/10 
dm = m*10
cm = m*100 
mm = m*1000


print(f'O valor de {m} m corresponde a {km} km, {hm} hm, {dam} dam, {dm} dm, {cm} cm, e {mm} mm')