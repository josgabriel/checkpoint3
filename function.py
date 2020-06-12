import base64
from Crypto.Cipher import AES

chave = 'fiap2020FIAP2020'
aes = AES.new(chave, AES.MODE_ECB)

def writetxt(txt):
    with open('dados.txt', 'w') as arquivo:
        arquivo.write(txt)

def originaltxt():
    with open('dados.txt', 'r') as arquivo:
        mostra = arquivo.read()
        return mostra

def b64txt():
    with open('dados.txt', 'rb') as arquivo:
        texto = arquivo.read()
        textolimpo = base64.b64encode(texto)
        return textolimpo.decode('utf8')

def criptob64():
    var = b64txt()
    textoEncriptado = aes.encrypt(b64A(var)[0])
    lista = [textoEncriptado, b64A(var)[1]]
    return lista

def b64A(var):
    quantA = 0
    while True:
        tamanho = len(var)
        if tamanho % 16 != 0:
            var = var + 'a'
            quantA = quantA + 1
        else:
            break
    lista = [var, quantA]
    return lista

def quantLinhas():
    with open('dados.csv', 'r') as arquivo:
        conteudo = arquivo.read()
        var = conteudo.split('\n')
        return len(var)

def gravarCSV():
    with open('dados.csv', 'a') as arquivo:
        arquivo.write(f'{quantLinhas()};{b64txt()};{criptob64()[0]};{criptob64()[1]}\n')

def mostraItens(opt = 2):
    try:
        with open('dados.csv', 'r') as arquivo:
            conteudo = arquivo.read()
            var = conteudo.split('\n')
            for linha in var:
                item = linha.split(';')
                tam = len(item)
                if 0 < tam-1:
                    print(f'código: {item[0]}')
                    print(f'base64: {item[1]}')
                    print(f'texto criptografado: {item[2]}')
                    if opt == 3:
                        texto = b64A(item[1])[0]
                        textoEncriptado = aes.encrypt(texto)
                        print(f'original: {decodeInsercao(textoEncriptado, item[3])}')
                    print('.'*70)
                    print()
    except:
        print('ainda não foi feita nenhuma inserçao, insira um texto antes de fazer a consulta')

def novaInsercao():
    texto = input('Digite o texto para ser codificado: ')
    print('-'*70)
    writetxt(texto)
    gravarCSV()
    print('texto em base64:')
    print(b64txt())
    print('-'*70)
    print('texto em base64 criptografado:')
    print(criptob64()[0])
    print('='*70)

def decodeInsercao(item, quantA):
    original = aes.decrypt(item)
    original = original.decode('utf-8')
    quant = int(quantA)
    while quant > 0:
        original = original[:-1]
        quant = quant-1
    original = base64.b64decode(original)
    return original.decode('utf-8')
    