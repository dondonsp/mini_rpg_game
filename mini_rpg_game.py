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
		self.health = (stre + res + sta) / 3
		self.max_health = (stre + res + sta) / 3
		self.magic = (dex + inte + per) / 3
		self.max_magic = (dex + inte + per) / 3
	

## Class for char
class Char:
	def __init__(self, genre, name, race, classe, attr):
		self.genre = genre
		self.name = name
		self.race = race
		self.classe = classe
		self.attributes = attr
		self.level = 1
	
	def get_level(self):
		return self.level

	def get_genre(self):
		return self.genre
	
	def get_name(self):
		return self.name
	
	def get_race(self):
		return self.race
	
	def get_classe(self):
		return self.classe
	
	def get_attributes(self, source):
		dataSource = getattr(self.attributes, source)
		return dataSource

	def set_attributes(self, source, val):
		dataSource = getattr(self.attributes, source)
		dataSource = val

	def set_health(self, flag, val):
		if flag == 'pos':
			self.attributes.health += val
		elif flag == 'neg':
			self.attributes.health -= val
		else:
			return

	def set_magic(self, flag, val):
		if flag  == 'pos':
			self.attributes.magic += val
		elif flag == 'neg':
			self.attributes.magic -= val
		else:
			return 

## Tests for classes
attr1 = Attributes(10, 10 ,10, 10, 5, 10, 10 ,10)
char1 = Char('M', 'Adan', 'ork', 'warrior', attr1)

attr2 = Attributes(8, 8, 8, 8, 4, 8, 8, 8)
char2 = Char('F', 'Aria', 'elf', 'mage', attr2)

## Function to show char's profile
def show_char(char):
	print char.get_name()
	print 'Level: ' + str(char.get_level())
	if char.get_genre() == 'F':
		print 'Genre: Famale'
	else:
		print 'Genre: Male'
	print 'Race: ' +  char.get_race()
	print 'Class: ' + char.get_classe()

	print 20 * '-'
	## Show attributes
	print 'Attributes'
	print 'HP: ' + str(char.get_attributes('health')) + '/' + str(char.get_attributes('max_health'))
	print 'MP: ' + str(char.get_attributes('magic')) + '/' + str(char.get_attributes('max_magic'))
	print 'Strength: ' + str(char.get_attributes('strength'))
	print 'Resistance: ' + str(char.get_attributes('resistance'))
	print 'Dexterity: '  + str(char.get_attributes('dexterity'))
	print 'Stamina: ' + str(char.get_attributes('stamina'))
	print 'Inteligence: ' + str(char.get_attributes('inteligence'))
	print 'Charisma: ' + str(char.get_attributes('charisma'))
	print 'Perception: ' + str(char.get_attributes('perception'))
	print 'Luck: ' + str(char.get_attributes('luck'))

	print 20 * '#'

char1.set_health('neg', 6)
char1.set_magic('sss', 4)
char2.set_magic('neg', 3)
char2.set_attributes('luck', 5)
show_char(char1)
show_char(char2)

## Testing git
## Testing git again
	