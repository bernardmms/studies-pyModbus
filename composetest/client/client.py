from pyModbusTCP.client import ModbusClient
import time

client = ModbusClient(host="localhost", port=502)
time.sleep(5)

try:
    print('Iniciando cliente...')
    client.open()
    print('Cliente iniciado.')
    while True:
        # Leitura da temperatura (registro 0)
        temperatura = client.read_holding_registers(0, 1)
        
        # Leitura do nível (registro 1)
        nivel = client.read_holding_registers(1, 1)
        
        # Leitura do estado da bomba (bobina 0)
        estado_bomba = client.read_coils(0, 1)

        if temperatura and nivel and estado_bomba is not None:
            print(f"Temperatura: {temperatura[0]}°C")
            print(f"Nível do tanque: {nivel[0]}")
            print(f"Estado da bomba: {'Ligada' if estado_bomba[0] else 'Desligada'}")
        else:
            print("Falha na leitura dos dados")

        time.sleep(2)

except KeyboardInterrupt:
    print("Programa interrompido pelo usuário")
finally:
    client.close()