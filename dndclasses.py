import pickle


class dndClass:
    def __init__(self, name, pri, sec):
        self.level = 1
        self.name=name
        self.primaryStat=pri
        self.secondaryStat=sec

    def levelUp(self):
        self.level+=1

classes=[]
barbarian=dndClass('Bardbarian', 'Con', 'Str')
classes.append(barbarian)
bard=dndClass('Bard', 'Cha', 'Dex')
classes += [bard]
cleric = dndClass('Clerk', 'Wis', 'Str')
classes += [cleric]
pickle.dump(classes, open("classes.p", "wb"))
