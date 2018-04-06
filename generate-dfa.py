from dfa import *


def generate_starting_with_dfa():
    number_of_symbols = int(input('enter number of input symbols:'))
    print('input symbols are:',end=' ')
    for i in range(number_of_symbols):
        if i != number_of_symbols-1:
            print(i,end=', ')
        else:
            print(i)
    check = 1
    while check != 0:
        condition = input('enter starting with string:')
        for char in condition:
            if int(char) not in range(number_of_symbols):
                print('incorrect input string for the alphabet')
                break
            else:
                check = 0
    number_of_states = len(condition)+2
    transition_table = {}
    initial_state = 0
    final_state = [len(condition)]
    fs = len(condition)
    for i in range(number_of_states):
        input_dict = {}
        for j in range(number_of_symbols):
            if i < fs:
                if j == int(condition[i]):
                    input_dict[j] = i+1
                else:
                    input_dict[j] = number_of_states-1
            elif i == fs:
                input_dict[j] = fs
            elif i > fs:
                input_dict[j] = i
        transition_table[i] = input_dict
    dfa = DFA(number_of_states,number_of_symbols,transition_table,initial_state,1,final_state)
    print(dfa)
    string = input('enter a string to process:')
    dfa.string_processing(string)


def generate_dfa_for_at_most():
    number_of_symbols = int(input('enter number of input symbols:'))
    print('input symbols are:', end=' ')
    for i in range(number_of_symbols):
        if i != number_of_symbols - 1:
            print(i, end=', ')
        else:
            print(i)
    check = 1
    while check != 0:
        number_at_most = int(input('enter the number of times the character must at most appear:'))
        condition = input('enter the character that should appear at least ' + str(number_at_most) + ' of times:')
        for char in condition:
            if int(char) not in range(number_of_symbols):
                print('incorrect input character for the alphabet')
                break
            else:
                check = 0
    number_of_states = number_at_most+2
    final_states = range(number_of_states-1)
    fs = number_of_states-2  # the last working state
    transition_table = {}
    for i in range(number_of_states):
        input_dict = {}
        for j in range(number_of_symbols):
            if i < fs:
                if int(condition[0]) == j:
                    input_dict[j] = i+1
                else:
                    input_dict[j] = i
            elif i == fs:
                if int(condition[0]) == j:
                    input_dict[j] = i+1
                else:
                    input_dict[j] = i
            else:
                input_dict[j] = i
        transition_table[i] = input_dict
    dfa = DFA(number_of_states,number_of_symbols,transition_table,0,number_of_states-1,final_states)
    print(dfa)
    string = input('enter a string to process:')
    dfa.string_processing(string)


def generate_dfa_for_at_least():
    number_of_symbols = int(input('enter number of input symbols:'))
    print('input symbols are:', end=' ')
    for i in range(number_of_symbols):
        if i != number_of_symbols - 1:
            print(i, end=', ')
        else:
            print(i)
    check = 1
    while check != 0:
        number_at_least = int(input('enter the number of times the character must at least appear:'))
        condition = input('enter the character that should appear at least '+str(number_at_least)+' of times:')
        for char in condition:
            if int(char) not in range(number_of_symbols):
                print('incorrect input character for the alphabet')
                break
            else:
                check = 0
    number_of_states = number_at_least + 1
    final_state = [number_of_states - 1]
    fs = number_of_states - 1
    transition_table = {}
    for i in range(number_of_states):
        input_dict = {}
        for j in range(number_of_symbols):
            if i != fs:
                if int(condition[0]) == j:
                    input_dict[j] = i + 1
                else:
                    input_dict[j] = i
            else:
                input_dict[j] = i
        transition_table[i] = input_dict
    dfa = DFA(number_of_states, number_of_symbols, transition_table, 0, 1, final_state)
    print(dfa)
    string = input('enter a string to process:')
    dfa.string_processing(string)


choice = 0
while choice != 3:
    choice = int(input("0) generate dfa for starting with\n1) generate dfa for at most\n"
                       "2) generate dfa for at least\n3) exit\nenter choice:\n"))
    if choice == 0:
        generate_starting_with_dfa()
    elif choice == 1:
        generate_dfa_for_at_most()
    elif choice == 2:
        generate_dfa_for_at_least()