class DFA:
    """This is the class to make DFA objects"""
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
        '''customises the print function for our specific needs'''
        output = ""
        output += "\t\t"
        for i in range(self.number_of_symbols):
            output += str(i)+"\t"
        output += "\n"
        for k in self.transition_table.keys():
            if k == self.initial_state:
                output += ">"
            if k in self.final_states:
                output += "*"
            output += "q"+str(k)+"\t\t"
            for v in range(self.number_of_symbols):
                output += "q"+str(self.transition_table[k][v])+"\t"
            output += "\n"
        return output

    def get_initial_final_states(self):
        self.initial_state = int(input('enter initial state:'))
        self.number_of_final_states = int(input('enter number of final states:'))
        for i in range(self.number_of_final_states):
            self.final_states.append(int(input('enter state:')))

    def make_transition_table(self):
        for i in range(self.number_of_states):
            inputDict = {}
            for j in range(self.number_of_symbols):
                checkState = 1000 #to ensure that user inputs only correct states
                while checkState not in self.states:
                    checkState = int(input('d(q' + str(i) + ',' + str(j) + '):'))
                inputDict[j] = checkState
            self.transition_table[i] = inputDict
        print(self.transition_table)

    def print_state_symbol_list(self):
        print('states are:')
        for i in range(self.number_of_states):
            print('q' + str(i))
        print('input symbols are:')
        for i in range(self.number_of_symbols):
            print(i)

    def string_processing(self, string):
        '''String processing is performed by this method'''
        currentState = self.initial_state
        symbols = []
        for i in range(self.number_of_symbols):
            symbols.append(str(i))
        wrongStringFlag = 0
        for char in string:
            if char not in symbols:
                print('error, incorrect input string')
                wrongStringFlag = 1
                break
            else:
                print('transition q' + str(currentState), end=' ')
                currentState = self.transition_table[currentState][int(char)]
                print('to q' + str(currentState), end='\n')

        if wrongStringFlag == 1:
            print('string not processed, incorrect input string')
        elif currentState in self.final_states:
            print('string processed')
        else:
            print('string not processed, finished at q' + str(currentState))