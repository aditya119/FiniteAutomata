from dfa import *

no_of_states = int(input('enter number of states'))
no_of_symbols = int(input('enter number of symbols'))

dfa = DFA(no_of_states, no_of_symbols)

dfa.print_state_symbol_list()
dfa.make_transition_table()
dfa.get_initial_final_states()
print(dfa)

flag = 0
while flag == 0:
    string = input('enter string to process:')
    dfa.string_processing(string)
    choice = input('process another string:')
    if choice == 'n':
        flag = 1