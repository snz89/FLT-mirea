class FSM:
    def __init__(self, states: set, initial_state, final_states: set, transitions: dict):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.current_state = initial_state

    def classify_char(self, character: str) -> str:
        if character.isdigit():
            return 'digit'
        elif character in ['+', '-']:
            return 'sign'
        return character

    def process_input(self, input_string):
        self.current_state = self.initial_state

        for char in input_string:
            char_type = self.classify_char(char)
            if char_type is None:
                return False
            if (self.current_state, char_type) in self.transitions:
                self.current_state = self.transitions.get((self.current_state, char_type))
            else:
                return False
        return self.current_state in self.final_states

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
    states = {0, 1, 2}
    initial_state = 0
    final_states = {2}
    transitions = {
        (0, 'sign'): 1,
        (1, 'digit'): 2,
        (2, 'digit'): 2
    }

    fsm = FSM(states, initial_state, final_states, transitions)
    user_input = input("Введите строку для анализа: ")
    if fsm.process_input(user_input):
        print("Строка принята")
    else:
        print("Строка не принята")


if __name__ == "__main__":
    main()
