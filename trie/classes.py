class State():
    def __init__(self, name):
        self.name = name
        self.final = False
        self.output = None
        self.edges = []

    def add_edge(self, destiny, transition):
        edge = Edge(self.name, destiny, transition)
        self.edges.append(edge)

    def add_state_to_trie(self, trie):
        trie.add_node(self.name, final=self.final, output=self.output)

    def add_edges_to_trie(self, trie):
        for edge in self.edges:
            trie.add_edge(edge.origin, edge.destiny,
                          transition=edge.transition)

    def set_final(self, is_final):
        self.final = is_final

    def set_output(self, output):
        self.output = output

    def is_equal(self, state):
        if self.final != state.final:
            return False
        if len(self.edges) != len(state.edges):
            return False
        for edge in self.edges:
            found_equivalent = False
            for state_edge in state.edges:
                if (edge.destiny == state_edge.destiny and edge.transition == state_edge.transition):
                    found_equivalent = True
                    break
            if found_equivalent:
                continue
            return False
        return True


class Edge():
    def __init__(self, origin, destiny, transition):
        self.origin = origin
        self.destiny = destiny
        self.transition = transition
