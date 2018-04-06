class NFA:
    """This is the class to make NFA objects"""
    def __init__(self, number_of_states, number_of_symbols, transition_table={}, initial_state=0,
                 number_of_final_states=0, final_states=[]):
        self.number_of_states = number_of_states
        self.number_of_symbols = number_of_symbols
        self.transition_table = transition_table
        self.initial_state = initial_state
        self.number_of_final_states = number_of_final_states
        self.final_states = final_states
        self.states = []
        for i in range(number_of_states):
            self.states.append(i)

    def __str__(self):
        """customises the print function for our specific needs"""
        output = ""
        output += "\t\t"
        for i in range(self.number_of_symbols):
            output += str(i)+"\t\t\t"
        output += "\n"
        for k in self.transition_table.keys():
            if k == self.initial_state:
                output += ">"
            if k in self.final_states:
                output += "*"
            output += "q"+str(k)+"\t\t"
            for v in range(self.number_of_symbols):
                output += "{"
                for state in self.transition_table[k][v]:
                    if state is None:
                        output += str(state)
                    else:
                        output += "q"+str(state)+","
                output += "}\t"
            output += "\n"
        return output

    def set_initial_final_states(self):
        self.initial_state = int(input('enter initial state:'))
        self.number_of_final_states = int(input('enter number of final states:'))
        for i in range(self.number_of_final_states):
            self.final_states.append(int(input('enter state:')))

    def get_initial_state(self):
        return self.initial_state

    def get_number_of_input_symbols(self):
        return self.number_of_symbols

    def make_transition_table(self):
        for i in range(self.number_of_states):
            inputDict = {}
            for j in range(self.number_of_symbols):
                number_of_transitions = int(input('for d(q'+str(i)+','+str(j)+') enter number of transitions:'))
                transitions_states = []
                if number_of_transitions == 0:
                    transitions_states.append(None)
                for k in range(number_of_transitions):
                    checkState = 1000 #to ensure that user inputs only correct states
                    while checkState not in self.states:
                        checkState = int(input('d(q' + str(i) + ',' + str(j) + '):'))
                    transitions_states.append(checkState)
                inputDict[j] = transitions_states.copy()
                transitions_states.clear()
            self.transition_table[i] = inputDict
        print(self.transition_table)

    def print_state_symbol_list(self):
        print('states are:')
        for i in range(self.number_of_states):
            print('q' + str(i))
        print('input symbols are:')
        for i in range(self.number_of_symbols):
            print(i)