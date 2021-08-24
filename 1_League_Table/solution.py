from collections import Counter
from collections import OrderedDict
from operator import itemgetter


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        name, score, games_played = [], [], []
        for p, c in self.standings.items():
            name.append(p)
            score.append(-c['score'])
            games_played.append(c['games_played'])
            indices = list(range(len(name)))
        ranked = list(zip(name, score, games_played, indices))
        ranked.sort(key=itemgetter(slice(1, None)))
        return ranked[rank - 1][0]


if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))
