from automata.fa.Mealy import Mealy

# Definindo a máquina de Mealy
mealy = Mealy(
    states=['q0', 'q1', 'q2', 'q3'],
    input_alphabet=['a', 'b'],
    output_alphabet=['0', '1'],
    transitions={
        'q0': {'a': ('q1', '1'), 'b': ('q3', '1')},
        'q1': {'a': ('q3', '0'), 'b': ('q1', '0')},
        'q2': {'a': ('q0', '0'), 'b': ('q3', '0')},
        'q3': {'a': ('q3', '1'), 'b': ('q2', '1')}
    },
    initial_state='q0'
)
print('Definição da Maquina de Mealy:')
print(mealy)
print('\n')
# Função para processar uma entrada
def processar_entrada(maquina, entrada):
    estado_atual = maquina.initial_state
    saida = ''
    
    for simbolo in entrada:
        proximo_estado, simbolo_saida = maquina.transitions[estado_atual][simbolo]
        saida += simbolo_saida
        estado_atual = proximo_estado
        
    return saida

# Processando uma entrada
entrada = 'abbba'
saida = processar_entrada(mealy, entrada)
print(f"Entrada: {entrada}")
print(f"Saída: {saida}")