import pickle


class dndClass:
    def __init__(self, name, pri, sec):
        self.level = 1
        self.name=name
        self.primaryStat=pri
        self.secondaryStat=sec

    def levelUp(self):
        self.level+=1


bard=dndClass('Bard', 'Cha', 'Dex')
classes=[bard]
pickle.dump(classes, open("classes.p", "wb"))
