from automata.fa.dfa import DFA

afd = DFA(
    states={'A', 'B', 'C'},
    input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
    transitions={
        'A': {'0': 'B', '1': 'C', '2': 'C', '3': 'C', '4': 'B', '5': 'C', '6': 'B', '7': 'C', '8': 'B', '9': 'C'},
        'B': {'0': 'B', '1': 'C', '2': 'C', '3': 'C', '4': 'B', '5': 'C', '6': 'B', '7': 'C', '8': 'B', '9': 'C'},
        'C': {'0': 'B', '1': 'C', '2': 'C', '3': 'C', '4': 'B', '5': 'C', '6': 'B', '7': 'C', '8': 'B', '9': 'C'},
    },
    initial_state='A',
    final_states={'B'}
)

def simular_afd(palavra):
    resultado = afd.accepts_input(palavra)
    print(f"AFD((Q, Sigma, delta, A, F), {palavra}) -> {resultado}")

palavras = ['246', '1357', '1122', '987654', '111', '1234567890']

for palavra in palavras:
    simular_afd(palavra)
