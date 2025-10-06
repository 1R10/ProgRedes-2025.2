ip = '200.17.143.129'
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


        if if eh_inteiro < 0 or eh_inteiro > 255: # >>>Todo<<< octeto deve ser um número inteiro que esteja entre 0(00000000) e 255(11111111)
            return False
