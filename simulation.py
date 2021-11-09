import random

from agent import *
from food_token import *
from arena import *
from utils import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from celluloid import Camera

import numpy as np



class Simulation():
    def __init__(self, timesteps=50):
        self.metadata = dict(title='Movie Test', artist='Matplotlib',
                        comment='Movie support!')
        self.timesteps = timesteps
        self.anim_frames = []
        self.fig = plt.figure()


    def run(self):
        fig, ax = plt.subplots()
        camera = Camera(fig)

        arena = Arena(1000, 1000)
        arena.add_agent(Agent(type="robot",
                              position=[500, 500],
                              orientation=0,
                              speed=[4, 0, 0]))

        arena.add_agent(Agent(type="robot",
                              position=[250, 350],
                              orientation=90,
                              speed=[4, 0, 0]))

        arena.add_food_token(FoodToken(type="food",
                                       position=[250, 250]))

        for x in range(15):
            arena.add_agent(Agent(type="robot",
                                  position=[random.randint(0,1000), random.randint(0,1000)],
                                  orientation=random.randint(0,359),
                                  speed=[4, 0, 0]))

        for i in range(self.timesteps):
            self.step(arena)
            # print(i)
            self.write_frame(arena, i, camera, fig, ax)

        anim = camera.animate(interval=50)
        anim.save('sim_output.mp4')

    def step(self, arena):
        for agent in arena.agents:
            agent.process_observation()
            update_position(agent)
            # print(agent.position)
            self.process_collisions(agent, arena)

    def process_collisions(self, agent, arena, threshold=20):
        for food_token in arena.food_tokens:
            dist = calc_distance(agent.position[0], agent.position[1], agent.size, food_token.position[0], food_token.position[1], food_token.size)
            if dist < threshold:
                arena.food_tokens.remove(food_token)
                agent.food_eaten += 1
                print("food eaten")

    def write_frame(self, arena, i, camera, fig, ax):
        plt.xlim(0, arena.width)
        plt.ylim(0, arena.height)
        for agent in arena.agents:
            ax.scatter(agent.position[0], agent.position[1], marker=(3, 0, 270+agent.orientation))
        for food_token in arena.food_tokens:
            ax.scatter(food_token.position[0], food_token.position[1], color='red', marker='*')
        camera.snap()
