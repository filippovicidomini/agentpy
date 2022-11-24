import agentpy as ap


class Student(ap.Agent):
    def setup(self):
        self.pos = (0, 0)

    def setup_pos(self, space):
        self.space = space
        self.pos = space.positions[self]
