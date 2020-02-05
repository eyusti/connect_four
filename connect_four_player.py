import connect_four
from tabulate import tabulate
import multiprocessing

def play_games(player_1, player_2,label):
    games_to_play_counter = 100
    games_to_play = games_to_play_counter
    all_games = []

    while games_to_play_counter > 0:
        new_game = connect_four.Game()
        new_game.player1 = player_1
        new_game.player2 = player_2
        winner = new_game.play_game()
        all_games.append(winner)
        games_to_play_counter -= 1

    wins_player_1 = all_games.count("1")
    percent_wins_player_1 = wins_player_1 / games_to_play
    wins_player_2 = all_games.count("2")
    percent_wins_player_2 = wins_player_2 / games_to_play
    ties = all_games.count("tie")
    percent_ties = ties / games_to_play
    print(label)
    print(tabulate([[new_game.player1,"1", str(wins_player_1),str(percent_wins_player_1)],[new_game.player2,"2", str(wins_player_2),str(percent_wins_player_2)],["tie", None, str(ties),str(percent_ties)]],headers=["AI","Turn order","Games won","%"]))

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=play_games, args=("minmax2","minmax2_w","depth of 3"))
    p2 = multiprocessing.Process(target=play_games, args=("minmax2_w","minmax2","depth of 3"))
    #p3 = multiprocessing.Process(target=play_games, args=("minmax2_w","RNG","depth of 3"))
    #p4 = multiprocessing.Process(target=play_games, args=("RNG","minmax2_w","depth of 3"))

    p1.start()
    p2.start()
    #p3.start()
    #p4.start()

    p1.join()
    p2.join()
    #p3.join()
    #p4.join()
