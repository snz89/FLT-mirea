class NFA:
    def __init__(self, states, initial_state, final_states, transitions):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    def process_input(self, input_string):
        current_states = {self.initial_state}

        for char in input_string:
            next_states = set()
            for state in current_states:
                if (state, char) in self.transitions:
                    if isinstance(self.transitions[(state, char)], set):
                        next_states.update(self.transitions[(state, char)]) # Объединяет множества
                    else:
                        next_states.add(self.transitions[(state, char)])

            if not next_states:
                return False

            current_states = next_states

        return any(state in self.final_states for state in current_states)

    def printGraphviz(self):
        print('digraph NFA {')
        print('    rankdir=LR;')
        print('    size="8,5";')

        for state in self.final_states:
            print(f'    node [shape = doublecircle]; {state};')

        print('    node [shape = circle];')

        for key, value in self.transitions.items():
            if isinstance(value, set):
                for v in value:
                   print(f'    {key[0]} -> {v} [ label = "{key[1]}" ];')
            else:
                 print(f'    {key[0]} -> {value} [ label = "{key[1]}" ];')

        print('}')

def main():
    states = {0, 1, 2, 3}
    initial_state = 0
    final_states = {3}
    transitions = {
        (0, 'a'): {0, 1},
        (0, 'b'): 0,
        (1, 'a'): 2,
        (1, 'b'): 2,
        (2, 'a'): 3,
        (2, 'b'): 3,
    }

    nfa = NFA(states, initial_state, final_states, transitions)

    print("Регулярное выражение: (a|b)*a(a|b)(a|b)")
    input_string = input("Введите строку для анализа: ")
    if nfa.process_input(input_string):
        print("Строка принята.")
    else:
        print("Строка не принята.")

    nfa.printGraphviz()

if __name__ == "__main__":
    main()