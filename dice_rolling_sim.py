import random
class Dice_roll:
	def roll(self, dice=1,sides=6):
		if dice != 1:
			for i in range(dice):
				print(random.randrange(1,sides))
		else:
			print(random.randrange(1,sides))
		return;
eric = Dice_roll()
eric.roll()
eric.roll(1,20)