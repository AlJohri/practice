from itertools import tee
from collections import deque

DEBUG = True

def pairwise(iterable):
    a,b = tee(iterable)
    next(b)
    return zip(a,b)

class Tower(object):

	def __init__(self, disks=[]):
		self.disks = disks

	def assert_disk_order(self):
		if not len(self.disks) <= 1:
			assert all([x > y for x,y in pairwise(self.disks)])
		return True

	def __str__(self):
		return str(self.disks)

class Game(object):

	def __init__(self, num_disks):
		self.num_disks = num_disks
		self.towers = [
			Tower(list(range(num_disks, 0, -1))),
			Tower(list(range(0, 0))), # prevent lists from linking
			Tower(list(range(0, 0))),
		]

	def moveOne(self, tower1, tower2):
		disk = tower1.disks.pop()
		tower2.disks.append(disk)
		self.assert_towers_order()

	def transfer(self, towerStart, towerEnd, n):
		towerOther = [tower for tower in self.towers if tower != towerStart and tower != towerEnd][0]

		if n > 0:
			self.transfer(towerStart, towerOther, n-1) # start to other
			self.moveOne(towerStart, towerEnd)
			if DEBUG: print(self)
			self.transfer(towerOther, towerEnd, n-1) # other to end
		return

	def play(self):
		game.transfer(game.towers[0], game.towers[2], self.num_disks)

	def assert_towers_order(self):
		assert all([tower.assert_disk_order() for tower in self.towers])
		return True

	def __str__(self):
		ret = "-----------------------------------\n"
		for i, tower in enumerate(self.towers):
			ret += chr(65+i) +  ":" + str(tower) + "\n"
		ret += "-----------------------------------\n"
		return ret

game = Game(5)
print(game)
game.play()
