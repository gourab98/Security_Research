def reset_scores(game_scores):
    new_game_scores = game1_scores.copy()

    for player, score in new_game_scores.items():
        new_game_scores[player]=0

    return new_game_scores


game1_scores = {"Arshi":3, "Catalina":7, "Diego":6}

print(reset_scores(game1_scores))