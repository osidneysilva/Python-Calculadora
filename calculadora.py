# calculadora_v0.py
# Meta: somar dois números digitados pelo usuário.

# 1) input() lê texto do teclado. Tudo que vem do input é 'str' (string).
a_texto = input('Digite o primeiro número: ')
b_texto = input('Digite o segundo número: ')

# 2) Usuários brasileiros usam a vírgula como separador decimal.
# Para converter para float, trocamos ',' por '.'
a_texto = a_texto.replace(',', '.')
b_texto = b_texto.replace(',', '.')

# 3) float() converte string para número de ponto flutuante.
# Se o usuário digitar algo não numérico, dará erro - na v1 vamos tratar isso melhor.
a = float(a_texto)
b = float(b_texto)

# 4) Processamento: Nesse momento do projeto vou apenas somar.
resultado = a + b

# 5) Saída: mostrar o resultado ao usuário.
print('Resultado:', resultado)
