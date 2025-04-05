from automata.fa.dfa import DFA

afd = DFA (
    states={ 'q0', 'q1', 'q2'},
    input_symbols={'a','b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q1'},
        'q1': {'a': 'q2', 'b': 'q2'},
        'q2': {'a': 'q0', 'b': 'q0'},
    },
    initial_state='q0',
    final_states={'q0'}
)

def simular_afd(palavra):
    resultado = afd.accepts_input(palavra)
    print(f'AFD((Q,SIGMA, DELTA, Q0, F), {palavra})')
    print(resultado)

palavras = ['aab', 'bba', 'aaa', '']

for palavra in palavras:
    simular_afd(palavra)