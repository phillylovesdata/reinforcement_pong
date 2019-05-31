import src.game_objects as go
import src.strategies as strat

TRAIN_MODE = True

def train(p_nepisodes):
    for i in range(p_nepisodes):
        new_game = go.Game()
        new_game.setPlayers(TRAIN_MODE)
        new_game.play()

        loss1 = new_game.player1.strategy.avg_loss
        loss2 = new_game.player2.strategy.avg_loss
        print("Player1 - AVG Loss - ", loss1)
        print("Player2 - AVG Loss - ", loss2)

        new_game.player1.points = 0
        new_game.player2.points = 0

def normal():
    want_new_players = True
    want_new_game = True
    new_game = go.Game()

    while want_new_game:
        want_new_game = False
        print('Let\'s Play Pong!!!')
        
        if want_new_players:
            want_new_players = False
            new_game.setPlayers()
            print('Players are set!')
            print('Player 1, Welcome!: '+new_game.player1.name)
            print('Player 2, Welcome!: '+new_game.player2.name)
        
        new_game.play()
        winner = new_game.winner
        
        print("Game finished!!!")
        print(winner.name + " won! Congratulations")
        
        user_input = input("Do you want to play a new game?[Yes/No] ")

        if user_input == "Yes":
            want_new_game = True

            user_input = input("Do you want to set new players?[Yes/No] ")

            if user_input == "Yes":
                want_new_players = True
            elif user_input == "No":
                new_game.player1.points = 0
                new_game.player2.points = 0

def main():
    if TRAIN_MODE:
        train(2)
    else:
        normal()
    

if __name__ == '__main__': 
    main() 