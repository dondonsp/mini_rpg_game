# -*- coding : latin1 -*-

##Class for attributes
class Attributes:
	def __init__(self, stre, res, dex, sta, inte, cha, per, luck):
		self.strength = stre
		self.resistance = res
		self.dexterity = dex
		self.stamina = sta
		self.inteligence = inte
		self.charisma = cha
		self.perception = per
		self.luck = luck
	

## Class for char
class Char:
	def __init__(self, genre, name, race, classe, attr):
		self.genre = genre
		self.name = name
		self.race = race
		self.classe = classe
		self.attributes = attr
	
	def get_genre(self):
		return self.genre
	
	def get_name(self):
		return self.name
	
	def get_race(self):
		return self.race
	
	def get_classe(self):
		return self.classe
	
	def get_attributes(self, at):
		return self.attributes.

## Tests for classes
attr1 = Attributes(10, 10 ,10, 10, 5, 10, 10 ,10)
char1 = Char('M', 'Adan', 'human', 'warrior', attr1)

print char1.get_name()
print char1.get_genre()
print char1.get_race()
print char1.get_classe()
print char1.get_attributes(inteligence)
print dir(Char)

## Testing git
## Testing git again
	