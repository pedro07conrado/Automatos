from automata.fa.dfa import DFA

afd = DFA(
    states={'S0', 'S1', 'S2', 'S3', 'S4'},  # Estados
    input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
    transitions={
        'S0': {'0': 'S0', '1': 'S1', '2': 'S2', '3': 'S3', '4': 'S4', '5': 'S0', '6': 'S1', '7': 'S2', '8': 'S3', '9': 'S4'},
        'S1': {'0': 'S1', '1': 'S2', '2': 'S3', '3': 'S4', '4': 'S0', '5': 'S1', '6': 'S1', '7': 'S2', '8': 'S3', '9': 'S4'},
        'S2': {'0': 'S2', '1': 'S3', '2': 'S4', '3': 'S0', '4': 'S1', '5': 'S2', '6': 'S1', '7': 'S2', '8': 'S3', '9': 'S4'},
        'S3': {'0': 'S3', '1': 'S4', '2': 'S0', '3': 'S1', '4': 'S2', '5': 'S3', '6': 'S1', '7': 'S2', '8': 'S3', '9': 'S4'},
        'S4': {'0': 'S4', '1': 'S0', '2': 'S1', '3': 'S2', '4': 'S3', '5': 'S4', '6': 'S1', '7': 'S2', '8': 'S3', '9': 'S4'},
    },
    initial_state='S0',  # Estado inicial
    final_states={'S0'}  # Estado(s) final(is)
)

# Função para testar o AFD
def simular_afd(palavra):
    resultado = afd.accepts_input(palavra)
    print(f"AFD((Q, Sigma, delta, S0, F), {palavra}) -> {resultado}")

palavras = ['0', '5', '10', '15', '20', '25', '30']

for palavra in palavras:
    simular_afd(palavra)
