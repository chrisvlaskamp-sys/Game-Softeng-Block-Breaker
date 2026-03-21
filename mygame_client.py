import sys
import zmq
import pygame

from Action import Action
from game_state import Game_State
prev_mouse_pressed = (False, False, False)


def main(name, port, host):
    # connect to server
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{host}:{port}")
    print(f"Connecting to port '{port}' of host '{host}'.")

    # start pygame
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('mygame')
    surface = pygame.display.get_surface()
    clock = pygame.time.Clock()
    background_color = (0,0,0)
    name_textures = Name_Textures()
    game_state = None
    
    running = True
    while running:
        display.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        socket.send_pyobj(get_action(name, pygame.key.get_pressed())) # send action
        if game_state:
            game_state.draw(surface, name_textures) # draw while waiting for answer
        game_state = socket.recv_pyobj() # receive game_state
        #print("game_state:",game_state)        
        
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

def get_action(name,keys):
    #reset game
    if keys[pygame.K_r]:
        return Action(name, 'reset')
    pos = pygame.mouse.get_pos()


    # change difficulty/ball speed
    global prev_mouse_pressed
    mouse = pygame.mouse.get_pressed()
    if mouse[0] and not prev_mouse_pressed[0]:
        prev_mouse_pressed = mouse
        pos = pygame.mouse.get_pos()
        return Action(name, 'mouse', pos)
    prev_mouse_pressed = mouse

    if keys[pygame.MOUSEBUTTONDOWN]:
        return Action(name, 'mouse', event.pos)
    if keys[pygame.K_1]:
        return Action(name, 'difficulty', 0)
    if keys[pygame.K_2]:
        return Action(name, 'difficulty', 1)
    if keys[pygame.K_3]:
        return Action(name, 'difficulty', 2)
    if keys[pygame.K_4]:
        return Action(name, 'difficulty', 3)
    
    #start game
    if keys[pygame.K_s]:
        return Action(name, 'start')


    # paddle acceleration:
    acceleration=pygame.Vector2(0,0)
    accel=0.5

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        acceleration.x -= accel
        return Action(name, 'accelerate', acceleration)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        acceleration.x += accel
        return Action(name, 'accelerate', acceleration)
    # If none of the above keys have been pressed:
    return Action(name, 'accelerate', acceleration)
    


class Name_Textures: # class to generate and store textures of user names

    def __init__(self):
        self.name_textures={}

    def get_texture(self, name):
        if not name in self.name_textures:
            font = pygame.font.SysFont('Comic Sans MS', 20)
            name_texture = font.render(name, False, (255,255,255))
            self.name_textures[name] = name_texture
        return self.name_textures[name]
        
if __name__ == "__main__":
    name = "_"
    port = 2345
    host = "0.0.0.0"
    if len(sys.argv)>1:
        name = sys.argv[1]
    if len(sys.argv)>2:
        port = int(sys.argv[2])
    if len(sys.argv)>3:
        host = sys.argv[3]
    main(name, port, host)
