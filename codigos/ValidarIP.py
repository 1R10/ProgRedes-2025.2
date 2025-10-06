
def validar_ip(ip: str): # Feito!
    '''
    Aqui vou formatar e validar o IP. 
    '''

    if type(ip) != str:
        return False
    
    l_octeto = ip.split('.') # >>>Todo<<< octeto deve ser um número inteiro que esteja entre 0 e 255
    if len(l_octeto) != 4:
        return False
    
    for num in l_octeto: 
        try:
            eh_inteiro = int(num)
        except ValueError as a: # Se tiver letra é inválido
            return False
    


        if eh_inteiro < 0 or eh_inteiro > 255: # >>>Todo<<< octeto deve ser um número inteiro que esteja entre 0(00000000) e 255(11111111)
            return False
    

def decimal_binario(ip: str):
    '''
    Aqui vou converter de decimal para binário
    '''
    l_octetos = ip.split('.')
    ipBin = ''

    for octeto in l_octetos:
        octeto = int(octeto)
        for num in range(7,-1,-1):
            bit_teste = octeto >> num
            bit_final = bit_teste & 1
            ipBin += str(bit_final)
    print(ipBin)
    

while True:
    try:
        print('''
[ 0 ] Desligar
[ 1 ] Inserir IP
[ 2 ] Inserir Máscara
[ 3 ] Converter IP para binário

             

''')
        escolha = int(input('Insira uma opção: '))

        if escolha > 3 or escolha < 0:
            print('Opção inválida!')

        if escolha == 0:
            print('Encerrando...')
            break
        elif escolha == 1:
            ip = input('Insira um ip(ex 192.158.1.38): ')
            if validar_ip == False:
                print(f'o IP {ip} não é inválido.')

        elif escolha == 2:
            mask = int(input('Insira uma máscara: '))

        elif escolha == 3:
            try:
                print(decimal_binario(ip))
            except:
                print('Não há um IP válido.')
            

    except:
        input('Houve um erro.')
