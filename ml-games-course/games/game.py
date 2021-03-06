import abc
import pygame
import os


x = int(os.getenv('PYGAME_X_POSITION', 400))
y = int(os.getenv('PYGAME_Y_POSITION', 200))
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

class Game(object):

    def __init__(self, name, grid_width, grid_height):
        pygame.init()
        pygame.display.set_caption(name)
        pygame.key.set_repeat(10, 100)

        self.name = name
        self.COLOR_WHITE = (255, 255, 255)
        self.COLOR_BLACK = (0, 0, 0)
        self.COLOR_GREEN = (25, 255, 0)
        self.COLOR_RED = (255,0,0)
        self.GAME_WIDTH = grid_width
        self.GAME_HEIGHT = grid_height    

    def reset(self):
        self.screen = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.clock = pygame.time.Clock()

        self.current_frame = self.get_frame()
        self.game_over = False
        self.current_reward = 0
        self.score = 0

    def step(self, action):
        self.screen.fill(self.COLOR_BLACK)

        self.execute_action(action)
        self.update_screen_elements()
        self.update_game_state()

        pygame.display.update()
        self.clock.tick(10)

        return self.current_frame, self.environment_action, self.current_reward, self.game_over, self.score

    @abc.abstractmethod
    def execute_action(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update_screen_elements(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update_game_state(self):
        raise NotImplementedError

    def get_frame(self):
        return pygame.surfarray.array3d(self.screen).swapaxes(0,1)
