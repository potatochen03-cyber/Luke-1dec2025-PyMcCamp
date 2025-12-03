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
