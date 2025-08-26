# # Meta: somar dois números digitados pelo usuário.

# # 1) input() lê texto do teclado. Tudo que vem do input é 'str' (string).
# a_texto = input('Digite o primeiro número: ')
# b_texto = input('Digite o segundo número: ')

# # 2) Usuários brasileiros usam a vírgula como separador decimal.
# # Para converter para float, trocamos ',' por '.'
# a_texto = a_texto.replace(',', '.')
# b_texto = b_texto.replace(',', '.')

# # 3) float() converte string para número de ponto flutuante.
# # Se o usuário digitar algo não numérico, dará erro - na v1 vamos tratar isso melhor.
# a = float(a_texto)
# b = float(b_texto)

# # 4) Processamento: Nesse momento do projeto vou apenas somar.
# resultado = a + b

# # 5) Saída: mostrar o resultado ao usuário.
# print('Resultado:', resultado)



# Meta: permitir as operações de adição, subtração, multiplicação, divisão e validar entrada.

def ler_numero(rotulo):
    """
    Função = "bloco reutilizável" de código.
    Por que usar função? Evita repetição, melhora a leitura e facilita testes.
    """
    while True:  # loop até o usuário digitar um número válido
        texto = input(rotulo).strip().replace(',', '.')
        try:
            # Tentamos converter para float.
            # Se der certo, retornamos o número e encerramos a função
            return float(texto)
        except ValueError:
            # Se não for número (ex.: 'dez'), avisamos e pedimos de novo.
            print('Entrada inválida. Digite um número. Ex.: 10, 3.5, -2')


# Ler o primeiro número
a = ler_numero('Digite o primeiro número: ')

# Ler o operador: aqui não convertemos, apenas lemos como texto.
op = input('Operador (+, -, *, /): ').strip()

b = ler_numero('Digite o segundo número: ')

# Decisão com if/elif/else: escolhemos a operação de acordo com 'op'
if op == '+':
    resultado = a + b
elif op == '-':
    resultado = a - b
elif op == '*':
    resultado = a * b
elif op == '/':
    # Divisão por zero é um erro matemático - então aqui vamos previnir.
    if b == 0:
        print('Erro: divisão por zero não é permitida.')
        # Encerramos o programa com código de erro.
        raise SystemExit(1)
    resultado = a / b
else:
    # Se o operador não for reconhecido, informamos.
    print('Operador inválido. Use um destes: +, -, *, /')
    raise SystemExit(1)

# Formatamos a saída para o usuário entender claramente o cálculo feito.
print(f'Resultado: {a} {op} {b} = {resultado}')
