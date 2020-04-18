def my_agent(observation, configuration):
    from random import choice
    #print(configuration.columns) # its 7
    #print(observation.board)
    # print(observation.board[c])
    return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
