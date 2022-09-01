"""
Reinforcement learning environment of maze

Red rectangle:      explorer.
Black rectangle:    hells       [reward = -1].
Yellow bin clrcle:  paradise    [reward = +1].
All other states:   groud       [reward = 0].

the environment is maze_env.py
the rl algorithm is RL_brain.py

"""
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

UNIT = 40 # pixels
MAZE_H = 4 # grid height
MAZE_W = 4 # grid width

class Maze(t k.TK, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')


if __name__ == '__main__':
    maze = Maze()