#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script Python Example
import time
import sys
import simulator
import numpy as np

data_php = sys.argv #[2].replace('_',' ')

tmp = []
for x in data_php:
	tmp.append(x.replace('_',' '))

user_team1 =tmp[1:15]
user_team2 =tmp[16:30]

# Name of the databse containing the players' profiles
data_file = 'player_better_dataframe.pkl'

#Specify any number of players per team

#~ if user_team1 == 'England':
	#~ team1 = ['John Mallett']

#~ if user_team1 == 'France':
	#~ team1 = ['Morgan Sienawski']

#~ if user_team1 == 'Scotland':
	#~ team1 = ['Phil De Glanville']

#~ if user_team1 == 'Wales':
	#~ team1 = ['Gideon Koegelenberg']
	
#~ if user_team1 == 'Rd':
	#~ team1 = [['John Mallett','Morgan Sienawski','Phil De Glanville','John Mallett'][np.random.randint(0,3,1)]]
	
#~ if user_team2 == 'England':
	#~ team2 = ['John Mallett']

#~ if user_team2 == 'France':
	#~ team2 = ['Morgan Sienawski']

#~ if user_team2 == 'Scotland':
	#~ team2 = ['Phil De Glanville']

#~ if user_team2 == 'Wales':
	#~ team2 = ['Gideon Koegelenberg']
	
#~ if user_team2 == 'Rd':
	#~ team2 = [['John Mallett','Morgan Sienawski','Phil De Glanville','John Mallett'][np.random.randint(0,3,1)]]
	
#~ with open(data_file, 'rb') as input:
		#~ df = pickle.load(input)

# Any of these work
simulator.simul_get_caracs(data_file,user_team1,user_team2)
#~ simulator.simul_get_caracs(data_file,team1)
#~ simulator.simul_get_caracs(data_file,team2)
#~ simulator.simul_get_caracs(data_file)
#~ print(sys.argv)

#~ print(user_team1,'\n\n',user_team2, len(user_team1.append(user_team2)))