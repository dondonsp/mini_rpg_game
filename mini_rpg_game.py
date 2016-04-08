# -*- coding : latin 1 -*-

##Class for attributes
class Attribute:
	def __init__(self, stre, res, dex, sta, inte, cha, per, luck):
		self.strength = stre
		self.resistance = res
		self.dexterity = dex
		self.stamina = sta
		self.inteligence = inte
		self.charisma = cha
		self.perception = per
		self.luck = luck
	
	def get_strength(self):
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
		self.luck = luck
	
## Class for char
class Char:
	def __init__(self, genre, name, race, classe, attr):
		self.genre = genre
		self.name = name
		self.race = race
		self.classe = classe
		self.attributes = attr
		
## Function for create a char
def create_char():
	##Define inf
	char = {'genre':'', 'name':'', 'race':'', 'classe':''}
	char['genre'] = raw_input('Genre of your char: M or F').upper()
	char['name'] = raw_input('Type name of char: ')
	## Define race
	race = ['human', 'elf', 'dwarf', 'undead', 'mecha']
	print "Define chars´s race"
	print 'human\n\n'
	print 'elf\n\n'
	print 'dwarf\n\n'
	print 'undead\n\n'
	print 'mecha\n\n'
	c_race = raw_input('->')
	for r in race:
		if c_race == r:
			char['race'] = c_race
		else:
			print 'Inexistent race!'
	##Define class
	classe = ['warrior', 'mage', 'thief', 'archer']
	print 'Define char´s class'
	print 'warrior\n\n'
	print 'mage\n\n'
	print 'thief\n\n'
	print 'archer\n\n'
	c_classe = raw_input('->')
	for c in classe:
		if c_classe == c:
			char['classe'] = c_classe
		else:
			print 'Inexistent class!'
	## Defining attributes
	points = 0
	if char['genre'] == 'F':
		points = 80
	else:
		points = 100
	
	attr = {'stre': '', 'res' : '', 'dex' : '', 'sta' : '', 'inte': '', 'cha': '', 'per': '', 'luck': ''}
	print 'You have ' + points + 'points of attribures. Distribute them in the fallowing: '
	print 'strength\n'
	print 'dexterity\n'
	print 'stamina\n'
	print 'inteligence\n'
	print 'charisma\n'
	print 'perception\n'
	print 'luck\n'
	
	print "classe inexistent"
	