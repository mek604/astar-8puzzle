# A* Search Algorithm to solve 8-Puzzle problem
# Author: Mek Obchey

from heapq import *
from node_8puzzle import *
import concurrent.futures

def main():

	s1 = "7 4 5 2 * 6 8 3 1".split(" ")
	goal = "1 2 3 4 5 6 7 8 *".split(" ")
	n = 3

	# precheck
	goal = Node(goal, n, 0, 1) #for printing only
	start = Node(s1, n, 0, 1)
	start.calculateCost(goal)

	# sanity check
	print("Goal:\n%s\n" % goal.string())
	print("Start state:\n%s\n" % start.string())
	print("goal allowed moves", goal.moves)
	print("start allowed moves", start.moves)

	openPQ = [start]
	closedPQ = []

	k = 0
	with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
		while len(openPQ) > 0:
			current = heappop(openPQ)
			print("follow cost= %d, depth= %d, board=\n%s\n" % (current.cost, current.depth, current.string()))
			if current.board == goal.board:
				trace(current)
				break
			heappush(closedPQ, current)
			# print("expanding:\n%s\n" % current.string())
			for i in current.moves:
				if i != current.pos:
					# copy its parent node and make a move
					expandNode = current.copy()
					expandNode.depth += 1
					expandNode.calculateCost(goal)
					expandNode.moveTo(i)
					add = True
					for nd in closedPQ:
						if nd.board == expandNode.board:
							add = False
							break
					if add:
						expandNode.parent = current
						heappush(openPQ, expandNode)
			openPQ.sort()

def trace(goal):
	current = goal
	order = []
	while current.parent != current:
		order.append(current)
		current = current.parent
	for i in order:
		print(i.string())

def hcost(current, goal):
	cost = 0
	for i, val in enumerate(current.board):
		if val != "*" and val != goal.board[i]:
			cost += 1
	return cost

def printPuzzle(string, puzzle):
	formatPuzzle(puzzle)
	print(string)
	for i, val in enumerate(puzzle):
		if i % 3 == 0 and i != 0:
			print("")
		print("%s " % str(val), end="")
	print("\n")

# interpret non puzzle entries
def formatPuzzle(puzzle):
	for i, val in enumerate(puzzle):
		if val == "*":
			puzzle[i] = 0
		puzzle[i] = int(puzzle[i])

if __name__ == "__main__":
	main()



