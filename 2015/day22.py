from heapq import heappush, heappop

# BFS exploration without need for memoization
# (mana spent, turn number, own HP, mana left, boss HP, rem shield turns, rem poison turns, rem recharge turns)
heap = [(0, 0, 50, 500, 51, 0, 0, 0)]
while True:
	spent, turn, hp0, mana, hp1, shield, poison, recharge = heappop(heap)
	hp0 -= 1 if turn % 2 == 0 else 0 # comment out for part 1
	if hp0 > 0:
		armor = 7 if shield > 0 else 0
		hp1 -= 3 if poison > 0 else 0
		if hp1 <= 0: break
		mana += 101 if recharge > 0 else 0
		shield = max(shield - 1, 0)
		poison = max(poison - 1, 0)
		recharge = max(recharge - 1, 0)
		turn += 1
		if turn % 2 == 1: # player turn
			if mana >= 53:
				heappush(heap, (spent+53, turn, hp0, mana-53, hp1-4, shield, poison, recharge))
			if mana >= 73:
				heappush(heap, (spent+73, turn, hp0+2, mana-73, hp1-2, shield, poison, recharge))
			if mana >= 113 and shield == 0:
				heappush(heap, (spent+113, turn, hp0, mana-113, hp1, 6, poison, recharge))
			if mana >= 173 and poison == 0:
				heappush(heap, (spent+173, turn, hp0, mana-173, hp1, shield, 6, recharge))
			if mana >= 229 and recharge == 0:
				heappush(heap, (spent+229, turn, hp0, mana-229, hp1, shield, poison, 5))
		else: # boss turn
			hp0 -= 9 - armor
			if hp0 > 0:
				heappush(heap, (spent, turn, hp0, mana, hp1, shield, poison, recharge))
print(spent)
