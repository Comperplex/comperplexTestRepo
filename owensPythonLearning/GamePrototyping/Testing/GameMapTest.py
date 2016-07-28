import unittest
import os, sys

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
gameDir = rootDir + "\\Game"
sys.path.append(gameDir)
#print(sys.path)
#sys.path.append('C:\\Users\\Nigel Landstalker\\Documents\\comperplexTestRepo\\owensPythonLearning\\GamePrototyping\\Game')
#print(sys.path)

from GameObject import GameObject
from GameMap import GameMap

class TestGameMap(unittest.TestCase):

	def testAddObject(self):
		gameMap = GameMap(100)

		#Testing a valid Game Object
		validGameObject = GameObject([0,0], 'drone', 'owen')
		self.assertTrue(gameMap.addObject(validGameObject))

		#Testing an invalid Game Object
		invalidGameObject = GameObject([500, 0], 'beacon', 'charter')
		self.assertFalse(gameMap.addObject(invalidGameObject))

if __name__ == '__main__':
    unittest.main()
