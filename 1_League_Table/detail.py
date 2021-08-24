from collections import Counter
from collections import OrderedDict


players = ['Mike', 'Chris', 'Arnold']

standings = OrderedDict([(player, Counter()) for player in players])

print('standings:', standings)

standings['Mike']['game_played'] += 1
standings['Mike']['score'] = 2

standings['Mike']['game_played'] += 1
standings['Mike']['score'] = 3

standings['Arnold']['game_played'] += 1
standings['Arnold']['score'] = 5

standings['Chris']['game_played'] += 1
standings['Chris']['score'] = 5

rank = 1

print("standings.items:", standings.items())
standings_with_index = enumerate(standings.items())
print("standings.items.enum:", standings_with_index)

ranks = [(-counter['score'], counter['games_played'], i, name)
         for i, (name, counter) in enumerate(standings.items())]


print("ranks", ranks)

print("Winner: {}".format(sorted(ranks)[rank - 1][3]))
