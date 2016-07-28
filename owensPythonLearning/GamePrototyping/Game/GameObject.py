class GameObject:

	loc, name, player = None, None, None

	def __init__(self, loc, name, player):
		self.loc = loc
		self.name = name
		self.player = player
