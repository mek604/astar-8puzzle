# Node specifically implemented for A* search algorithm and 8 puzzle
#
# Author: Mek Obchey
# Email: aobchey00@uvic.ca

import copy

class Node:
	def __init__(self, board, size, depth, cost):
		self.board = board
		self.depth = depth
		self.size = size
		self.pos = self.findEmptyCell()	# position of the blank cell (cell with * symbol)
		self.moves = []
		self.cost = cost	# must be set
		self.parent = self
		self.__moveable__() # find valid moves

	def __lt__(self, other):
		if self.cost < other.cost:
			return True
		return False

	def __le__(self, other):
		if self.cost <= other.cost:
			return True
		return False

	def copy(self):
		return copy.deepcopy(self)

	def findEmptyCell(self):
		for i, val in enumerate(self.board):
			if val == "*":
				return i
		return 0

	# assuming there is only one blank cell symbol (*)
	def string(self):
		output = ""
		for i, val in enumerate(self.board):
			if i % self.size == 0 and i != 0:
				output += "\n"
			output += str(val) + " "
		return output

	# get a list of number movable by the empty square
	def __moveable__(self):
		moves = []
		# if the position of the empty square allows the move up, down, left, right
		if self.pos - self.size >= 0:
			moves.append(self.pos - self.size)
		if self.pos + self.size <= self.size * self.size - 1:
			moves.append(self.pos + self.size)
		if self.pos % self.size != 0:
			moves.append(self.pos - 1)
		if (self.pos + 1) % self.size != 0:
			moves.append(self.pos + 1)
		self.moves = moves

	# move empty cell to position x if it is a valid position
	def moveTo(self, x):
		if x in self.moves and x != self.pos:
			tmp = self.board[x]
			self.board[x] = self.board[self.pos]
			self.board[self.pos] = tmp
			self.pos = x
			self.__moveable__()

	# the implementation of this function is specifically for
	# goal state = "1 2 3 4 5 6 7 8 *"
	def calculateCost(self, goal):
		hcost = 0
		n = self.size
		for i, entry in enumerate(self.board):
			if entry != "*":
				val = int(entry) # incase board values are still interpreted as strings
				# -------------- mismatches heuristic-----------------
				if val != goal.board[i]:
					hcost += 1
				# -------------- manhattan heuristic -----------------
				x1 = i % n
				y1 = int((pow(n,2) - 1 - i) / n)
				x2 = (val - 1) % n
				y2 = int((pow(n, 2) - 1 - val) / n)
				hcost += abs(x1 - x2) + abs(y1 - y2)
				# -------------------------------------------
		self.cost = hcost + self.depth
