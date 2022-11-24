import agentpy as ap
import random
import clear_screen

banco = (5, 5)


def output(grid):
    clear_screen.clear_screen()
    for row in grid.grid:
        for cell in row:

            if str(cell[0]) == 'AgentSet (1 object)':
                print('X', end='  ')
            else:
                print('.', end='  ')

        print()


model = ap.Model()
agents = ap.AgentList(model, 10)
grid = ap.Grid(model, (10, 10), track_empty=True)
grid.add_agents(agents)
# print(grid.positions)


check: bool = True
while check:
    for i in range(10):
        grid.move_by(agents[i], (random.randint(-1, 1), random.randint(-1, 1)))
    output(grid)
    if grid.positions[agents[0]] == banco:
        check = False
