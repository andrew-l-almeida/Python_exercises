import random
msg = 'MasterCgef é legalll'
p = 151
q = 157



def rsa(msg, p, q):
    cript_msg = []
    decrypto_msg = []
    n = p * q #Modulo de P * Q = 151 * 157 = {23707}

    totient = calculate_totient(p, q) #Totiente = 23400

    e = random_prime(totient) # o 'e' tem que ser menor que o totient e qualquer numero que seja coprimo

    d = calculate_D(e , totient) # De acordo com a formula, D = 3503

    public_key = {'e': e, 'n': n} # e = 167 e n = 23707
    private_key = {'d': d, 'n': n} # d = 303, n = 23707

    cript_msg = encrypt(msg, public_key)
    decrypto_msg = decrypt(cript_msg, private_key)

    print(f'Valor de P: {p}')
    print(f'Valor de Q: {q}')
    print(f'Valor do Totient: {totient}')
    print(f'Valor do E (gerado aleatoriamente): {e}')
    print(f'Valor do D (Formula): {d}')
    print(f'Public key: {public_key}')
    print(f'Private key: {private_key}')
    print(f'Mensagem enviada: {msg}')
    print(f'Mensagem Criptografada: {cript_msg}')
    print(f'Mensagem Descriptografada: {decrypto_msg}')


def calculate_totient(p, q):
    totient = ((p - 1) * (q - 1))
    return totient

def calculate_D(e, totient):
    # Formula 
    # e * d mod totiente(n) = 1
    # 17 * d mod 20 precisa ser 1.
    i = 1
    x = 1
    while(True):
        if(e * x % totient == 1):
            d = x
            break
        x += 1
    return d

def encrypt(msg, public_key):
    cript_msg = []
    cryptStr = ''
    for m in msg:
        c = pow(ord(m), public_key['e']) % public_key['n']
        #print(f'Letra: {m}, Ord: {ord(m)}, Crypto: {c}')
        cript_msg.append(chr(c))
    for l in cript_msg:
        cryptStr = cryptStr + l
    return cryptStr

def decrypt(encryptMsg, private_key):
    decrypto_msg = []
    strDecriptedMsg = ''
    # decrypt = c ^ d mod n
    # X = (C * Y^(-1)) % Z
    for c in encryptMsg:
        d = pow(ord(c), private_key['d']) % private_key['n']
        decrypto_msg.append(chr(d))
    for l in decrypto_msg:
        strDecriptedMsg = strDecriptedMsg + l

    return strDecriptedMsg





def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def random_prime(totient):
    while True:
        candidate = random.randint(2, totient)
        if is_prime(candidate) and totient % candidate != 0:
            return candidate

rsa(msg, p, q)



