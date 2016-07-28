from GameObject import GameObject

class GameMap:
	size = [500, 500]
	maxEntities = None
	gameObjects = []

	def __init__(self, maxEntities):
		self.maxEntities = maxEntities

	def addObject(self, gameObject):
		if gameObject.loc[0] in range(self.size[0]) and gameObject.loc[1] in range(self.size[1]):
			self.gameObjects.append(gameObject)
			return True
		else: return False
