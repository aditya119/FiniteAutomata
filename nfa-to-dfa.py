from nfa import *
from dfa import *


def make_dfa(nfa):
    initial_state = nfa.get_initial_state()
    number_of_input_symbols = nfa.get_number_of_input_symbols()
    states = [[initial_state]]
    state_id = 0
    state_table = {str([initial_state]): state_id}
    state_id += 1
    transition_table = {}
    final_states = []

    print('checking initial state', initial_state)
    input_dict = {}
    state_checker = [[initial_state]]

    while states:
        for state in states:
            input_dict = {}
            print('checking state ' + str(state) + ' id ' + str(state_table[str(state)]))
            for i in range(number_of_input_symbols):
                new_state = []
                for s in state:
                    new_state += nfa.transition_table[s][i]
                    if None in new_state:
                        new_state.remove(None)
                new_state = list(set(new_state))
                print('new state', new_state)
                print('state list', state_checker)
                if new_state not in state_checker:
                    print('new state doesnt already exist')
                    states.append(new_state)
                    state_checker.append(new_state)
                    state_table[str(new_state)] = state_id
                    print('new state list', state_checker)
                    for s in new_state:
                        if s in nfa.final_states:
                            final_states.append(state_id)
                            break
                    state_id += 1
                input_dict[i] = state_table[str(new_state)]
                print('d(q' + str(state_table[str(state)]) + ',' + str(i) + ') = q' + str(state_table[str(new_state)]))
                print()
            transition_table[state_table[str(state)]] = input_dict
            states.remove(state)
            print('\n\n')
    return DFA(len(state_table), number_of_input_symbols, transition_table, initial_state, len(final_states),
               final_states)


if __name__ == '__main__':
    no_of_states = int(input('enter number of states'))
    no_of_symbols = int(input('enter number of symbols'))

    nfa = NFA(no_of_states, no_of_symbols)

    nfa.print_state_symbol_list()
    nfa.make_transition_table()
    nfa.set_initial_final_states()
    print(nfa)
    dfa = make_dfa(nfa)
    print(dfa)