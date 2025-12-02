# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
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