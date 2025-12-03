# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def bw():
    for b in range(31):
        agent.move(UP, 1)
        agent.place(DOWN)
        agent.move(UP, 1)
        agent.place(DOWN)
        agent.move(UP, 1)
        agent.place(DOWN)
        agent.move(RIGHT, 1)
        agent.move(DOWN, 4)

player.on_chat("bw",bw)

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
    agent.move(DOWN,1)

player.on_chat("obby1",obby1)


def chop(height):
    for i in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, height)
    agent.collect_all()

player.on_chat("go",chop)



def mineore(length):
    for m in range(length):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)

player.on_chat("mine",mineore)

def downm():
    agent.destroy(DOWN)

player.on_chat("d",downm)

def coll():
    agent.collect_all()

player.on_chat("col",coll)


def bw():
    for b in range(31):
        agent.move(UP, 1)
        agent.place(DOWN)
        agent.move(UP, 1)
        agent.place(DOWN)
        agent.move(UP, 1)
        agent.place(DOWN)
        agent.move(RIGHT, 1)
        agent.move(DOWN, 4)

player.on_chat("bw",bw)



