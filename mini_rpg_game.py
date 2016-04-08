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
	
	'''def get_strength(self):
		return self.strength
	
	def get_resistance(self):
		return self.resistance
	
	def get_dexterity(self):
		return self.dexterity
	
	def get_stamina(self):
		return self.stamina
	
	def get_inteligence(self):
		return self.inteligence
	
	def get_charisma(self):
		return self.charisma
	
	def get_perception(self):
		return self.perception
		
	def get_luck(self):
		return self.luck
	
	def set_strength(self, stre):
		self.strength = stre
	
	def set_resistance(self, res):
		self.resistance = res
	
	def set_dexterity(self, dex):
		self.dexterity = dex
	
	def set_stamina(self, stre):
		self.stamina = sta
	
	def set_inteligence(self, inte):
		self.inteligence = inte
	
	def set_charisma(self, cha):
		self.charisma = cha
		
	def set_perception(self, per):
		self.perception = per
	
	def set_luck(self, luck):
		self.luck = luck'''

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
	
	def get_attributes(self):
		return self.attributes.inteligence

## Tests for classes
attr1 = Attributes(10, 10 ,10, 10, 5, 10, 10 ,10)
char1 = Char('M', 'Adan', 'human', 'warrior', attr1)

print char1.get_name()
print char1.get_genre()
print char1.get_race()
print char1.get_classe()
print char1.get_attributes()
	