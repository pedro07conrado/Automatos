from automata.fa.dfa import DFA

# Definindo o AFD
afd = DFA(
    states={'q0', 'q1'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q1'},
        'q1': {'a': 'q0', 'b': 'q0'},
    },
    initial_state='q0',
    final_states={'q0'}
)

# Função para simular a execução do AFD e imprimir o resultado
def simular_afd(palavra):
    resultado = afd.accepts_input(palavra)
    print(f"AFD((Q, Sigma, delta, q0, F), {palavra}) -> {resultado}")

# Lista de palavras para testar
palavras = ['a', 'aa', 'ab', 'abab', 'aabb', '']

# Executando a simulação para cada palavra
for palavra in palavras:
    simular_afd(palavra)
