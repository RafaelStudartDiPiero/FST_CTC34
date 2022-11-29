class State():
    def __init__(self, name):
        self.name = name
        self.final = False
        self.edges = []

    def add_edge(self, destiny, transition, output=0):
        edge = Edge(self.name, destiny, transition, output)
        self.edges.append(edge)
        # print("Adicionei edge de {} para {} com {} e output {}".format(
        #     edge.origin, edge.destiny, edge.transition, edge.output))

    def add_state_to_fst(self, fst):
        fst.add_node(self.name, final=self.final)

    def add_edges_to_fst(self, fst):
        for edge in self.edges:
            fst.add_edge(edge.origin, edge.destiny,
                         transition=edge.transition, output=edge.output)

    def set_final(self, is_final):
        self.final = is_final

    def is_equal(self, state):
        if self.final != state.final:
            # print("Final Diferente")
            return False
        if len(self.edges) != len(state.edges):
            # print("Numero edges diferente")
            return False
        for edge in self.edges:
            found_equivalent = False
            for state_edge in state.edges:
                if (edge.destiny == state_edge.destiny and edge.transition == state_edge.transition and edge.output == state_edge.output):
                    found_equivalent = True
                    break
            if found_equivalent:
                continue
            # print("Nao achou equivalente")
            return False
        return True

    def output(self, destiny):
        for edge in self.edges:
            if (edge.destiny == destiny):
                return edge.output
        return None

    def clear(self):
        self.final = False
        self.edges = []

    def copy(self):
        new_state = State(self.name)
        new_state.set_final(self.final)
        for edge in self.edges:
            new_state.add_edge(edge.destiny, edge.transition, edge.output)
        return new_state

    def rename(self, name):
        self.name = name
        for edge in self.edges:
            edge.origin = name

    def remove_edge(self, destiny, transition):
        to_be_removed_edge = None
        for edge in self.edges:
            if (edge.destiny == destiny and edge.transition == transition):
                to_be_removed_edge = edge
                break
        if to_be_removed_edge != None:
            # print("Removi edge {} para {} com e output {}".format(
            #     edge.origin, edge.destiny, edge.transition, edge.output))
            self.edges.remove(to_be_removed_edge)

    def set_output(self, destiny, new_output):
        for edge in self.edges:
            if edge.destiny == destiny:
                edge.output = new_output
                # print("Setei {} de {} para {} com {}".format(
                #     edge.output, edge.origin, edge.destiny, edge.transition))

    def correct_edges(self, fator):
        for edge in self.edges:
            # print(edge.output)
            edge.output = edge.output + fator
            # print("Corrigi edge de {} para {} de transicao {} com {}".format(
            #     edge.origin, edge.destiny, edge.transition, edge.output))


class Edge():
    def __init__(self, origin, destiny, transition, output):
        self.origin = origin
        self.destiny = destiny
        self.transition = transition
        self.output = output
