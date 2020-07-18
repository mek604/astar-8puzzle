# Node of 8puzzle board for A* search algorithm
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

	# mismatches + depth
	def calculateCost(self, goal):
		cost = 0
		for i, val in enumerate(self.board):
			if val != "*" and val != goal.board[i]:
				cost += 1
		self.cost = cost + self.depth
