def inverter_string(texto):
    invertida = ''
    
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

texto_usuario = input("Digite uma string para inverter: ")

resultado = inverter_string(texto_usuario)
print("String invertida:", resultado)