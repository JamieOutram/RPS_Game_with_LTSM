def telepath(opponent_guess):
    if(opponent_guess == 'R'):
        return 'P'
    elif(opponent_guess == 'P'):
        return 'S'
    elif(opponent_guess == 'S'):
        return 'R'