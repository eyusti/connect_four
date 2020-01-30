import connect_four
from tabulate import tabulate

games_to_play_counter = 1000
games_to_play = games_to_play_counter
all_games = []

while games_to_play_counter > 0:
    new_game = connect_four.Game()
    new_game.player1 = "rng"
    new_game.player2 = "minmax"
    winner = new_game.play_game()
    all_games.append(winner)
    games_to_play_counter -= 1

print(all_games)
wins_player_1 = all_games.count("1")
percent_wins_player_1 = wins_player_1 / games_to_play
wins_player_2 = all_games.count("2")
percent_wins_player_2 = wins_player_2 / games_to_play
ties = all_games.count("tie")
percent_ties = ties / games_to_play
print(tabulate([[new_game.player1,"1", str(wins_player_1),str(percent_wins_player_1)],[new_game.player2,"2", str(wins_player_2),str(percent_wins_player_2)]],headers=["AI","Turn order","Games won","%"]))
