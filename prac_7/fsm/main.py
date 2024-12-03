class FSM:
    def __init__(self,
                 states: set,
                 initial_state,
                 final_states: set,
                 transitions: dict):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    def process_input(self, input_string):
        current_state = self.initial_state

        for char in input_string:
            if (current_state, char) in self.transitions:
                current_state = self.transitions.get((current_state, char))
            else:
                return False
        return current_state in self.final_states
    
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
    states = {1, 2, 3, 4}
    initial_state = 1
    final_states = {4}
    transitions = {
        (1, 'a'): 2,
        (1, 'b'): 1,
        (2, 'a'): 3,
        (2, 'b'): 3,
        (3, 'a'): 4,
        (3, 'b'): 4,
    }


    fsm = FSM(states, initial_state, final_states, transitions)
    fsm.printGraphviz()
    # print("Регулярное выражение: (a|b)*a(a|b)(a|b)")
    # input_string = input("Введите строку для анализа: ")

    # if fsm.process_input(input_string):
    #     print("Строка принята.")
    # else:
    #     print("Строка не принята.")


if __name__ == "__main__":
    main()