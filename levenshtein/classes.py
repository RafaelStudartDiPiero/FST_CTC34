class SparseLevenshteinAutomaton:
    def __init__(self, string):
        self.string = string
        self.max_edits = 1

    def start(self):
        return range(self.max_edits+1), range(self.max_edits+1)

    def step(self, state, c):
        indices, values = state
        if indices and indices[0] == 0 and values[0] < self.max_edits:
            new_indices = [0]
            new_values = [values[0] + 1]
        else:
            new_indices = []
            new_values = []

        for j, i in enumerate(indices):
            if i == len(self.string):
                break
            cost = 0 if self.string[i] == c else 1
            val = values[j] + cost
            if new_indices and new_indices[-1] == i:
                val = min(val, new_values[-1] + 1)
            if j+1 < len(indices) and indices[j+1] == i+1:
                val = min(val, values[j+1] + 1)
            if val <= self.max_edits:
                new_indices.append(i+1)
                new_values.append(val)

        return (new_indices, new_values)

    def is_match(self, state):
        indices = state[0]
        return bool(indices) and indices[-1] == len(self.string)

    def can_match(self, state):
        indices = state[0]
        return bool(indices)

    def transitions(self, state):
        indices = state[0]
        return set(self.string[i] for i in indices if i < len(self.string))

    def read_input(self, input):
        state = self.start()
        for letter in input:
            state = self.step(state, letter)
            if not self.can_match(state):
                return False
        return True
