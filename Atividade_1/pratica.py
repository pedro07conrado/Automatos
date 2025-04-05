from automata.fa.dfa import DFA

afd = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q2'},
        'q1': {'a': 'q0', 'b': 'q5'},
        'q2': {'a': 'q3', 'b': 'q4'},
        'q3': {'a': 'q2', 'b': 'q5'},
        'q4': {'a': 'q5', 'b': 'q0'},
        'q5': {'a': 'q4', 'b': 'q1'},
    },
    initial_state='q0',
    final_states={'q1'}
)

test_strings = ['aabbb', 'bbbaaa', 'aaaaabbbbb', 'bbb']

for s in test_strings:
    print(f"{s}: {afd.accepts_input(s)}")
