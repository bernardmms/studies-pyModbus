from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
import random

# Criação do servidor Modbus
server = ModbusServer("localhost", 502, no_block=True)

try:
    print("Iniciando servidor...")
    server.start()
    print("Servidor está online")

    # Configuração inicial dos dados
    server.data_bank.set_holding_registers(0, [0]*10)  # 10 registros de retenção (holding registers)
    server.data_bank.set_coils(0, [0]*10)   # 10 bobinas (coils)

    while True:
        # Simulação de leitura de sensor (registro 0)
        temperatura = random.randint(97, 100)
        server.data_bank.set_holding_registers(0, [temperatura])

        # Simulação de um nível de tanque (registro 1)
        nivel = random.randint(700, 702)
        server.data_bank.set_holding_registers(1, [nivel])

        # Simulação de estado de uma bomba (bobina 0)
        estado_bomba = 1
        server.data_bank.set_coils(0, [estado_bomba])

        print(f"Temperatura: {temperatura}°C, Nível: {nivel}, Bomba: {'Ligada' if estado_bomba else 'Desligada'}")
        sleep(2)

except:
    print("Servidor parado")
    server.stop()