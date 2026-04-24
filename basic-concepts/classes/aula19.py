"""
# CONSTANTE = 'Variaveis' que não vão mudar
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
"""

velocidade = 61
local_carro = 99


RADAR_1  = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_multado_radar_1 and vel_carro_pass_radar_1:    
    print('Carro multado em radar 1')