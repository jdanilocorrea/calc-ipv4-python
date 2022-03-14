# No cálculo ipv4 temos 4 octetos de 8 bits
# em que cada bit representa um valor na posição sequencial
# os respectivos valores são: 128 64 32 16 8 4 2 1
# Em observação o valor posterior é a metade do antecesso

# Aqui temos os intervalos de classes representativa
# O valor do primeiro octeto representa a classe

# "Classe A de 10.0.0.0 - 10.255.255.255"
# "Classe B 172.16.0.0 - 172.31.255.255"
# "Classe C 192.168.0.0 - 192.168.255.255"


ipv4 = input(r'digite um ip valido "com pontos": ')
mask = input(r'digite uma mascara valida "com pontos": ')
# my_mask = input(r'digite uma maskara *"com pontos"*')

octet_ipv4 = ipv4.split('.')
octets_mask = mask.split('.')
tipo_classe = ''

#     =>  8    7   6   5  4  3  2  1
octet_dec = [128, 64, 32, 16, 8, 4, 2, 1]

octet1 = int(octet_ipv4[0])
octet2 = int(octet_ipv4[1])
octet3 = int(octet_ipv4[2])
octet4 = int(octet_ipv4[3])

# ---------------------------------------------------------------------------------------
if octet1 > 0 and octet1 < 128:
    if octet1 == 127:
        print('IP  Reservado para testes internos dispositivo loopback - "localhost"')

    else:
        tipo_classe = 'A'
        print('Classe A / 10.0.0.0 - 10.255.255.255')
# ---------------------------------------------------------------------------------------
if octet1 > 127 and octet1 < 192:
    tipo_classe = 'B'
    print('Classe B / 172.16.0.0 - 172.31.255.255')
# ---------------------------------------------------------------------------------------
if octet1 > 191 and octet1 < 224:
    tipo_classe = 'C'
    print('Classe C / 192.168.0.0 - 192.168.255.255')
# ---------------------------------------------------------------------------------------
if octet1 > 223 and octet1 < 240:
    tipo_classe = 'D'
    print('Classe D')
# ---------------------------------------------------------------------------------------
if octet1 > 239 and octet1 < 256:
    tipo_classe = 'E'
    print('Classe E')


octets = [octet1, octet2, octet3, octet4]
soma_bit = 0
list_octs = []
for oct in octets:
    list_bits = []
    for index in range(8):
        if octet_dec[index] <= oct:
            res = oct % octet_dec[index]
            list_bits.append(1)
            soma_bit += octet_dec[index]
            if res == octet_dec[index]:
                break
            oct = res
        else:
            list_bits.append(0)

    list_octs.append(list_bits)

print('----------------------------------------------------------------------------------------------------------')
octets_decs = [octet_dec, octet_dec, octet_dec, octet_dec]
print(f'octets:\n{octets_decs}')
print('----------------------------------------------------------------------------------------------------------')
print(f'bits:\n{list_octs}')
# print('----------------------------------------------------------------------------------------------------------')
print(f'ip:{octet1: ^22}||{octet2: ^24}||{octet3: ^24}||{octet4: ^24}')
print('----------------------------------------------------------------------------------------------------------')

for v in range(4):
    for index in range(8):
        if index == 7:
            print(f'/{octet_dec[index]}', end='  ||  ')

        else:
            print(f'/{octet_dec[index]}', end='')

print('')


for oct_ in list_octs:
    for bit in range(8):
        if bit == 7:
            print(f'/{oct_[bit]}', end='   ||  ')
        elif octet_dec[bit] < 16:
            print(f'/{oct_[bit]}', end='')
        else:
            print(f'/ {oct_[bit]}', end='')

print('')

print('----------------------------------------------------------------------------------------------------------')

bits_rede = 0
bits_maq = 0
list_octs_bits_mask = []

for oct_mk in octets_mask:
    bits_mask = []
    bit_dec = 256 - int(oct_mk)
    for index in range(len(octet_dec)):
        if int(oct_mk) == 255:
            bits_rede += 1
            bits_mask.append(1)
        elif bit_dec <= octet_dec[index]:
            bits_rede += 1
            bits_mask.append(1)
        else:
            bits_maq += 1
            bits_mask.append(0)
    list_octs_bits_mask.append(bits_mask)

print(f'mascara: {octets_mask}')
print(f'bits de rede: {bits_rede}')
print(f'bits de máquina: {bits_maq}')
print(
    f'mask:{octets_mask[0]: ^20}||{octets_mask[1]: ^24}||{octets_mask[2]: ^24}||{octets_mask[3]: ^24}')
print(f'octetos de bits: {list_octs_bits_mask}')

# --------------------------------------------------
# append, insert, pop, del, clear, extend, +
