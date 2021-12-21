from random import randint

def gerar_cpf():
    while True:
        cpf = [randint(0, 9) for i in range(9)]
        if cpf != cpf[::-1]:
            break

    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    #  Retorna o CPF como string
    result = ''.join(map(str, cpf))
    #print(f'CPF gerado: {result[:3]}.{result[3:6]}.{result[6:9]}-{result[9:]}') # Este tambem dá o resultado final
    return result

if __name__ == '__main__':
    cpf = gerar_cpf()
    print(f'CPF gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
