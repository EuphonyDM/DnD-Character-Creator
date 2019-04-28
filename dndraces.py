import pickle

class Race:
	def __init__(self, name, asi, subraces):
		self.name = name
		self.asi = asi
		self.subraces = subraces

class SubRace(Race):
	def __init__(self, name, asi):
		Race.__init__(self, name, asi, None)

races = []

#Dwarf & Subraces
subraces = []
asi = []
pair = 'wis', 1
asi.append(pair)
hillDwarf = SubRace('Hill Dwarf', asi)
subraces.append(hillDwarf)
asi = []
pair = 'str', 2
asi.append(pair)
mountDwarf = SubRace('Mountain Dwarf', asi)
subraces.append(mountDwarf)
asi = []
pair = 'con', 2
asi.append(pair)
dwarf = Race('Dwarf', asi, subraces)
races.append(dwarf)

#Elf
subraces = []
asi = []
pair = 'int', 1
asi.append(pair)
highElf = SubRace('High Elf', asi)
subraces.append(highElf)
asi = []
pair = 'wis', 1
asi.append(pair)
woodElf = SubRace('Wood Elf', asi)
subraces.append(woodElf)
asi = []
pair = 'cha', 1
asi.append(pair)
drowElf = SubRace('Drow Elf', asi) 
subraces.append(drowElf)
asi = []
pair = 'dex', 2
asi.append(pair)
elf = Race('Elf', asi, subraces)
races.append(elf)

#Halfling
subraces = []
asi = []
pair = 'cha', 1
asi.append(pair)
lightHalfling = SubRace('Lightfoot Halfling', asi)
subraces.append(lightHalfling)
asi = []
pair = 'con', 1
asi.append(pair)
stoutHalfling = SubRace('Stout Halfling', asi)
subraces.append(stoutHalfling)
asi = []
pair =  'dex', 2
asi.append(pair)
halfling = Race('Halfling', asi, subraces)
races.append(halfling)

#Human
subraces = []
asi = []
pair = 'str', 1
asi.append(pair)
pair = 'dex', 1
asi.append(pair)
pair = 'con', 1
asi.append(pair)
pair = 'int', 1
asi.append(pair)
pair = 'wis', 1
asi.append(pair)
pair = 'cha', 1
asi.append(pair)

stdHuman = SubRace('Human', asi)
subraces.append(stdHuman)

asi = []
pair = 'any', 1
asi.append(pair)
asi.append(pair)
pair = 'feat', 1
asi.append(asi)

varHuman = SubRace('Variant Human', asi)
subraces.append(varHuman)

human = Race('Human', None, subraces)
races.append(human)

#Dragonborn
asi = []
pair = 'str', 2
asi.append(pair)
pair = 'cha', 1
asi.append(pair)
dragonborn = Race('Dragonborn', asi, None)
races.append(dragonborn)

#Gnome
subraces = []
asi = []
pair = 'dex', 1
asi.append(pair)
forestGnome = SubRace('Forest Gnome', asi)
subraces.append(forestGnome)

asi = []
pair = 'con', 1
asi.append(pair)
rockGnome = SubRace('Rock Gnome', asi)
subraces.append(rockGnome)

asi = []
pair = 'int', 2
asi.append(pair)
gnome = Race('Gnome', asi, subraces)
races.append(gnome)

#Half-Elf
asi = []
pair = 'cha', 2
asi.append(pair)
pair = 'any', 1
asi.append(pair)
pair = 'any', 1
asi.append(pair)

halfElf = Race('Half-Elf', asi, None)
races.append(halfElf)

#Half-Orc
asi = []
pair = 'str', 2
asi.append(pair)
pair = 'con', 1
asi.append(pair)

halfOrc = Race('Half-Orc', asi, None)
races.append(halfOrc)

#Tiefling
asi = []
pair = 'cha', 2
asi.append(pair)
pair = 'int', 1
asi.append(pair)

tiefling = Race('Tiefling', asi, None)
races.append(tiefling)

pickle.dump(races, open( "races.p", "wb" ))