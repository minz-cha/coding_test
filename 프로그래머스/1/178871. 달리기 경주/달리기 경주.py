def solution(players, callings):
    player_index = {player: i for i, player in enumerate(players)}

    for i in range(len(callings)):
        calling = callings[i]
        start_index = player_index[calling]
        players[start_index], players[start_index - 1] = players[start_index - 1], players[start_index]

        player_index[calling] = start_index - 1
        player_index[players[start_index]] = start_index

    return players
