import pickle


class dndClass:
    def __init__(self, name, pri, sec):
        self.level = 1
        self.name=name
        self.primaryStat=pri
        self.secondaryStat=sec

    def levelUp(self):
        self.level+=1


barbarian=dndClass('Barbarian', 'Str', 'Con')
classes=[barbarian]
bard=dndClass('Bard', 'Cha', 'Dex')
classes.append(bard)
cleric=dndClass('Cleric', 'Wis', 'Con')
classes.append(cleric)
pickle.dump(classes, open("classes.p", "wb"))
