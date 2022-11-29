import networkx as nx
from trie.classes import State


def create_trie(dictionary):
    # Initial

    trie = nx.DiGraph()
    states = []
    i = 0

    # Creating TRIE based on dictionary
    state0 = State(i)
    i += 1
    state0.add_state_to_trie(trie)

    value = 1

    for key in dictionary:
        state = 0
        for idx, letter in enumerate(key):
            current_state_edges = dict(trie[state])
            prev_state = state
            for next_state, edge_properties in current_state_edges.items():
                if edge_properties['transition'] == letter:
                    state = next_state
                    break
            if (state == prev_state):
                aux_state = State(i)

                if idx == len(key)-1:
                    aux_state.set_final(1)
                    aux_state.set_output(value)

                aux_state.add_state_to_trie(trie)
                trie.add_edge(state, i, transition=letter)
                # print(
                #     f"adicionei a transição {state} para {i} com a letra {letter}")
                state = i
                i += 1
        value = value + 1

    return trie


def read_input_trie(input, trie):
    state = 0
    output = None
    for idx, letter in enumerate(input):
        current_state_edges = dict(trie[state])
        # print(trie[state])
        prev_state = state
        for next_state, edge_properties in current_state_edges.items():
            if edge_properties['transition'] == letter:
                state = next_state
                if idx == len(input)-1:
                    if (trie.nodes[state]["final"]):
                        output = trie.nodes[state]["output"]
                break
        if (state == prev_state):
            break

    return output


def auto_complete_trie(input, trie):
    state = 0

    for idx, letter in enumerate(input):
        current_state_edges = dict(trie[state])
        # print(trie[state])
        prev_state = state
        for next_state, edge_properties in current_state_edges.items():
            if edge_properties['transition'] == letter:
                state = next_state
                break
        if (state == prev_state):
            return None

    queue = [(state, input)]
    autocomplete_list = []

    while len(queue) > 0 and len(autocomplete_list) < 5:
        tupla = queue.pop(0)
        currrent_state = tupla[0]
        if trie.nodes[currrent_state]["final"]:
            autocomplete_list.append(tupla[1])
        current_state_edges = dict(trie[currrent_state])
        for next_state, edge_properties in current_state_edges.items():
            queue.append((next_state, tupla[1]+edge_properties['transition']))

    return autocomplete_list

def read_trie():
    trie = nx.read_gpickle("generated_trie")
    return trie