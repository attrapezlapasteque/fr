import numpy as np
import _pickle as pickle
import pandas as ps

# The model function takes as input the characteristics of the two teams and returns the proba of team 1 winning against team 2
#For now : basically random number between 0 and 1
def modele(var_team1,var_team2):
	#~ print('Team 1: ', var_team1['Minutes played'].sum(),"(Minutes played: ",var_team1['Minutes played'].iloc[0],")\nTeam 2: ",var_team2['Name'].iloc[0],"(Minutes played: ",var_team2['Minutes played'].iloc[0],')\n\n')
	return("L'equipe 1 a " + str(round(var_team1['Minutes played'].sum()*100/(var_team1['Minutes played'].sum()+var_team2['Minutes played'].sum()))) + " % de chance de gagner contre l'equipe 2 !")
	#~ return('Team 1 has ' + str(round(np.random.uniform()*100)) + ' % chance of winning against team 2 !')
	
	
	
# Take the name of the players of the two teams, look for them in the database, get their caracs
def simul_get_caracs(data_base,team1 = None,team2 = None):
	
	#If no teams are provided, generate both at random
	if team1 == None and team2 == None:
		
		with open(data_base, 'rb') as input:
			df = pickle.load(input)
		
		team1 = df['Name'].sample(n=15)
		team2 = df['Name'].sample(n=15)
		
		print('No teams specified ! Here are the two teams battling for victory ! \n Team 1: \n',[x for x in team1], '\n Team 2: \n',[x for x in team2],'\n')
		
		print(modele(df[df['Name'].isin(team1)],df[df['Name'].isin(team2)]))
	
	#If only one team is specified, generate the second at random
	elif team1 != None and team2 == None:
		
		with open(data_base, 'rb') as input:
			df = pickle.load(input)
			
		# Generate a team at random
		team2 = df['Name'].sample(n=len(team1))
		print('Team 2 has been picked at random ! Here are its players: \n',[x for x in team2])
			
		print(modele(df[df['Name'].isin(team1)],df[df['Name'].isin(team2)]))
	
	# If both teams provided
	elif team1 != None and team2 != None:
		
		with open(data_base, 'rb') as input:
			df = pickle.load(input)
		
		print(modele(df[df['Name'].isin(team1)],df[df['Name'].isin(team2)]))
