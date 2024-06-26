from exercicios import *


carro_1 = Carro('Renault', 'Captur', 5)
carro_2 = Carro('Honda', 'HRV', 5)
carro_3 = Carro('Fiat', 'Fastback', 5)

moto_1 = Moto('Haojue', 'DR160', 'casual')
moto_2 = Moto('Yamaha', 'R15', 'esportiva')
moto_3 = Moto('Honda', '300F', 'casual')

for veiculo in range(3):
    print(eval(f"carro_{veiculo+1}"))
    print(eval(f"moto_{veiculo+1}"))