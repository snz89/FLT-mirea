class FSM:
    def __init__(self, initial_state, final_states: set, transitions: dict):
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
    def printGraphviz(self):
        print('digraph FSM {')
        print('    rankdir=LR;')
        print('    size="8,5";')

        for state in self.final_states:
            print(f'    node [shape = doublecircle]; {state};')

        print('    node [shape = circle];')

        for key, value in self.transitions.items():
            print(f'    {key[0]} -> {value} [ label = "{key[1]}" ];')

        print('}')


def main():
    initial_state = 'q0'
    final_states = {'q2'}
    transitions = {
        ('q0', 0): 'q1',
        ('q1', 0): 'q6',
        ('q2', 0): 'q0',
        ('q3', 0): 'q2',
        ('q4', 0): 'q7',
        ('q5', 0): 'q2',
        ('q6', 0): 'q6',
        ('q7', 0): 'q6',
        ('q0', 1): 'q5',
        ('q1', 1): 'q2',
        ('q2', 1): 'q2',
        ('q3', 1): 'q6',
        ('q4', 1): 'q5',
        ('q5', 1): 'q6',
        ('q6', 1): 'q4',
        ('q7', 1): 'q2'
    }
    
    min_transitions = {
        ('q0q4', 0): 'q1q7',
        ('q1q7', 0): 'q6',
        ('q2', 0): 'q0q4',
        ('q3q5', 0): 'q2',
        ('q6', 0): 'q6',
        ('q0q4', 1): 'q3q5',
        ('q1q7', 1): 'q2',
        ('q2', 1): 'q2',
        ('q3q5', 1): 'q6',
        ('q6', 1): 'q0q4',
    }

    dka = FSM(initial_state, final_states, transitions)
    mdka = FSM(initial_state, final_states, min_transitions)
    dka.printGraphviz()


if __name__ == "__main__":
    main()
