nome = input('Olá, qual seu nome?')
mat = int(input('Qual sua nota em matemática? '))
port = int(input('Qual sua nota em português? '))
cie = int(input('Qual sua nota em ciências? '))
media = (mat+port+cie)/3
print(f'{nome} sua média é {media}. Parabéns' if media >=7 else f'{nome}, sua média foi {media} estude mais')