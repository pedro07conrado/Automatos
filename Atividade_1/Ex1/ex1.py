from automata.fa.dfa import DFA

afd = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q_rejeicao'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'b': 'q1', 'a': 'q_rejeicao'},
        'q1': {'a': 'q2', 'b': 'q_rejeicao'},
        'q2': {'a': 'q_rejeicao', 'b': 'q3'},
        'q3': {'a': 'q4', 'b': 'q_rejeicao'},
        'q4': {'a': 'q_rejeicao', 'b': 'q_rejeicao'},
        'q_rejeicao': {'a': 'q_rejeicao', 'b': 'q_rejeicao'},
    },
    initial_state='q0',
    final_states={'q4'},
)

def simular_afd(palavra):
    resultado = afd.accepts_input(palavra)
    print(f"AFD((Q, Σ, δ, q0, F), '{palavra}') = {resultado}")


palavras = ['baba', 'baabaabaa', 'baaaabaaa']

for palavra in palavras:
    simular_afd(palavra)
