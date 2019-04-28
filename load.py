import pickle
import dndraces

file_name = 'races.p'
data = None
with open(file_name, 'rb') as out_file:
   data = pickle.load(out_file)


for race in data:
	print(race.name)
	print(race.asi)
	if race.subraces is not None:
		for subrace in race.subraces:
			print('    ', subrace.name)
			print('    ', subrace.asi)
			print('    ----')
	print('----')
