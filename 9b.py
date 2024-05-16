import random

class Agent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.x = None
        self.y = None

    def move(self, world):
        empty_patch = world.find_empty_patch()
        if empty_patch:
            self.x, self.y = empty_patch
            world.grid[self.x][self.y] = self.agent_id

    def __str__(self):
        return f'Agent {self.agent_id} at ({self.x}, {self.y})'

class World:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.agents = [Agent(agent_id) for agent_id in range(num_agents)]

    def find_empty_patch(self):
        empty_patches = [(x, y) for x in range(self.width) for y in range(self.height) if self.grid[x][y] is None]
        return random.choice(empty_patches) if empty_patches else None

    def __str__(self):
        return '\n'.join([' '.join([str(self.grid[x][y]) if self.grid[x][y] is not None else '.' for y in range(self.width)]) for x in range(self.height)])

def initialize_world():
    width, height = 5, 5
    num_agents = 5
    world = World(width, height, num_agents)
    return world

def run_simulation(world, num_loops):
    for _ in range(num_loops):
        for agent in world.agents:
            agent.move(world)
        print(world)
        print('-' * 20)


if __name__ == '__main__':
    world = initialize_world()
    num_loops = 3
    run_simulation(world, num_loops)