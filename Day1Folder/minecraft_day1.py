# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def move_forward(steps):
    agent.move(FORWARD, steps)
def move_back(steps):
    agent.move(BACK, steps)
def move_up(height):
    agent.move(UP, height)
def move_down(height):
    agent.move(DOWN, height)
def turn_left() : 
    agent.turn(TurnDirection.LEFT)
def turn_right():
    agent.turn(TurnDirection.RIGHT)
def teleport():
    agent.teleport_to_player()
    
    

player.on_chat("come",teleport)
player.on_chat("f1",move_forward)
player.on_chat("b1",move_back)
player.on_chat("up",move_up)
player.on_chat("down",move_down)
player.on_chat("tr",turn_right)
player.on_chat("tl",turn_left)


def obby1():
    agent.move(FORWARD,5),
    agent.turn(TurnDirection.LEFT)
    agent.move(FORWARD,5)
    agent.turn(TurnDirection.RIGHT)
    agent.move(FORWARD,3)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)

player.on_chat("obby1",obby1)