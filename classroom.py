import agentpy as ap
from student import Student


class Classroom(ap.Model):
    def setup(self):
        self.space = ap.grid2d(10, 10)
        self.agents = ap.AgentList(self, Student, 10)
        self.space.add_agents(self.agents)
        self.agents.setup_pos(self.space)

    def step(self):
        self.agents.step()


classroom = Classroom()
print(classroom)
