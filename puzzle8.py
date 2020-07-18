# A* Search Algorithm to solve 8-Puzzle problem
# Author: Mek Obchey
# using the heuristic cost of manhattan distance + tiles differences


from heapq import *
from node_a8 import *

def main():
	
	# for testing only: simpler initial state and goal state
	# s1 = "1 2 3 4 5 6 * 7 8".split(" ")
	# s1 = "* 1 3 4 2 5 7 8 6".split(" ")

	s1 = "7 4 5 2 * 6 8 3 1".split(" ")
	goal = "1 2 3 4 5 6 7 8 *".split(" ")

	n = 3

	# precheck
	goal = Node(goal, n, 0, 0) #for printing only
	start = Node(s1, n, 0, 1)
	start.calculateCost(goal)

	# sanity check
	print("Goal:\n%s\n" % goal.string())
	print("Start state:\n%s\n" % start.string())
	print("goal allowed moves", goal.moves)
	print("start allowed moves", start.moves)

	openPQ = [start]
	closedPQ = []

	print(start.cost)
	while len(openPQ) > 0:
		current = heappop(openPQ)
		print("expanding cost= %d, depth= %d, board=\n%s\n" % (current.cost, current.depth, current.string()))
		if current.board == goal.board:
			print("^^^^^^^^^ Found the goal state ^^^^^^^^^\n")
			trace(current)
			break
		heappush(closedPQ, current)
		for i in current.moves:
			if i != current.pos:
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

# traceback the path from goal state to initial state
def trace(goal):
	current = goal
	order = []
	while current.parent != current:
		order.append(current)
		current = current.parent
	# add back the initial state before printing
	order.append(current)
	print("The optimal path to follow:\n")
	for i in range(len(order)-1, -1, -1):
		print(order[i].string(), "\n")

def hcost(current, goal):
	cost = 0
	for i, val in enumerate(current.board):
		if val != "*" and val != goal.board[i]:
			cost += 1
	return cost

if __name__ == "__main__":
	main()



