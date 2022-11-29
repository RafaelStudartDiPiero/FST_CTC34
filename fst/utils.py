def findMinimizedState(state, minimal_states, max_word_size):
    for frozen_state in minimal_states:
        if frozen_state.is_equal(state):
            # print("Estado Equivalente, {}, Final:{}, Edges:{}".format(frozen_state.name, frozen_state.final, len(frozen_state.edges)))
            # for edge in frozen_state.edges:
            #     print("Origem:{}, Destino:{}, Transicao:{}, Output:{}".format(edge.origin, edge.destiny, edge.transition, edge.output))
            return frozen_state
    new_state = state.copy()
    new_state.rename(len(minimal_states)+max_word_size+1)
    # print("Novo Estado Minimizado, {}, Final:{}, Edges:{}".format(new_state.name, new_state.final, len(new_state.edges)))
    # for edge in new_state.edges:
    #     print("Origem:{}, Destino:{}, Transicao:{}, Output:{}".format(edge.origin, edge.destiny, edge.transition, edge.output))
    minimal_states.append(new_state)
    # for stat in minimal_states:
    #     print("Estado: {}, Final:{}, Edges:{}".format(stat.name, stat.final, len(stat.edges)))
    return new_state


def findMaxWordSize(dictionary):
    max_word_size = 0
    for word in dictionary:
        if len(word) > max_word_size:
            max_word_size = len(word)
    return max_word_size
