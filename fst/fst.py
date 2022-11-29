import networkx as nx
from fst.classes import State
from fst.utils import findMaxWordSize, findMinimizedState


def create_minimal_transducer(dictionary):
    # Initial

    fst = nx.MultiDiGraph()
    minimal_states = []
    max_word_size = findMaxWordSize(dictionary)
    # print(max_word_size)
    temp_states = []
    for i in range(0, max_word_size + 1):
        temp_state = State(i)
        temp_states.append(temp_state)

    # Algorithm

    prev_word = ""
    current_word = ""

    index = 1

    for word in dictionary:
        current_word = word
        # print(current_word)
        # Longest Prefix
        prefix_len = 0
        while (prefix_len < len(current_word) and prefix_len < len(prev_word) and prev_word[prefix_len] == current_word[prefix_len]):
            prefix_len = prefix_len + 1
        # Minimize States from Suffix of the Previous Word
        for i in range(len(prev_word), prefix_len, -1):
            cur_output = temp_states[i-1].output(temp_states[i].name)
            # print(cur_output)
            temp_states[i-1].remove_edge(temp_states[i].name, prev_word[i-1])
            temp_states[i-1].add_edge(findMinimizedState(temp_states[i],
                                      minimal_states, max_word_size).name, prev_word[i-1], cur_output)
            temp_states[i].clear()
        # Initializes Tail States for the Current Word
        for i in range(prefix_len, len(current_word)):
            temp_states[i].add_edge(temp_states[i+1].name, current_word[i])
        if current_word != prev_word:
            temp_states[len(current_word)].set_final(True)
        # Fixing Outputs
        missing_output = index
        for i in range(0, prefix_len+1):
            # print(missing_output)
            if i == prefix_len:
                temp_states[i].set_output(
                    temp_states[i+1].name, missing_output)
                break
            cur_output = temp_states[i].output(temp_states[i+1].name)
            # print(cur_output)
            new_output = min(missing_output, cur_output)
            # print(new_output)
            temp_states[i].set_output(temp_states[i+1].name, new_output)

            dif_output = cur_output - new_output

            temp_states[i+1].correct_edges(dif_output)

            missing_output = missing_output - new_output

        prev_word = current_word
        index = index + 1

    # Minimizing States for Last Word
    for i in range(len(current_word), 0, -1):
        cur_output = temp_states[i-1].output(temp_states[i].name)
        temp_states[i-1].remove_edge(temp_states[i].name, current_word[i-1])
        temp_states[i-1].add_edge(findMinimizedState(temp_states[i],
                                  minimal_states, max_word_size).name, current_word[i-1], cur_output)
        temp_states[i].clear()

    # Adding starting state
    new_state = temp_states[0].copy()
    new_state.rename(0)
    minimal_states.append(new_state)

    # Creating FST based on list

    # for stat in minimal_states:
    #     print("Estado: {}, Final:{}, Edges:{}".format(stat.name, stat.final, len(stat.edges)))
    #     for edge in stat.edges:
    #         print("Origem:{}, Destino:{}, Transicao:{}, Output:{}".format(edge.origin, edge.destiny, edge.transition, edge.output))

    for state in minimal_states:
        state.add_state_to_fst(fst)
    for state in minimal_states:
        state.add_edges_to_fst(fst)

    return fst

# Read Input


def read_input_fst(input, fst):
    state = 0
    output = 0
    for letter in input:
        current_state_edges = dict(fst[state])
        prev_state = state
        for next_state, edge_properties in current_state_edges.items():
            for index, edge in edge_properties.items():
                if edge['transition'] == letter:
                    state = next_state
                    output += edge['output']
                    break
        if (state == prev_state):
            print("Nao chegou ao fim")
            break
    return output


def auto_complete_fst(input, fst):
    state = 0

    for letter in input:
        current_state_edges = dict(fst[state])
        prev_state = state
        for next_state, edge_properties in current_state_edges.items():
            for index, edge in edge_properties.items():
                if edge['transition'] == letter:
                    state = next_state
                    break
        if (state == prev_state):
            return "Não existe"

    # print(state)
    queue = [(state, input)]
    autocomplete_list = []

    while len(queue) > 0 and len(autocomplete_list) < 5:
        current_pair = queue.pop(0)
        current_state = current_pair[0]
        # print("Atual:{}".format(current_state))
        # Adding final words to autocomplete_list
        if fst.nodes[current_state]["final"]:
            autocomplete_list.append(current_pair[1])
        # Adding New States to BFS
        current_state_edges = dict(fst[current_state])
        for next_state, edge_properties in current_state_edges.items():
            for index, edge in edge_properties.items():
                # print("Proximo:{}".format(next_state))
                queue.append((next_state, current_pair[1]+edge['transition']))

    return autocomplete_list


def read_fst():
    fst = nx.read_gpickle("generated_fst")
    return fst
