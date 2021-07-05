


class Arena:
    """This class implements the arena in which agents live"""
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def step(self):
        pass
