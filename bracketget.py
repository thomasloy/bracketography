import sys
import random

len_away = 10
f = open('pagesave.txt','r')
lines = f.readlines()
f.close()
count = 0
line = lines[538]
line = line.split("<span")
teams = []
counts = []

for a in line:
	if "class=\"name\"" in a and "class=\"state\"" not in a and "class=\"name\"><a></a></span>" not in a:
		if "class=\"name\">Rnd1 Winner</span>" in a:
			teams.append("WILDCD")
		else:
			teams.append(a[69:79].split('\'')[0])
			print teams[-1],"     \t",a[69:].split('>')[1].split('<')[0].replace('&amp;','&')
		counts.append(count)
	count += 1
count = 0
for x in xrange(1,len(counts)):
	a = counts[x]-counts[x-1]
	if a > 100:
		count = 0
	count += 1
teams =teams[8:72]
divisions = []
l = []
for a in xrange(0,len(teams),2):
	if a%16 == 0 and a!= 0:
		divisions.append(l)
		l = []
	l.append((teams[a],teams[a+1]))
divisions.append(l)
count = 0

def Sim_Game(team1,team2,alg):
	if alg == 0:
		r = random.randint(0,1)
		if r == 1:
			return team2
		return team1
	if alg == 1:
		return team1

def NCAA(d,al):
	final_list = []
	ltmp = []
	for a in xrange(0,len(d)):
		ltmp.append(d[a][0])
		ltmp.append(d[a][1])
	final_list.append(ltmp)
	co = 1
	while True:
		final_list.append(d)
		#print "-------Round " , co,"--------"
		co += 1
		for a in xrange(0,len(d)):
			#print "game",a,"--\t",d[a][0],"\t",d[a][1]
			d[a] = Sim_Game(d[a][0],d[a][1],al)
			#print d[a] , "wins"
		if len(d) == 1:
			#print d[0] + " Won!"
			final_list.append(d[0])
			return final_list
		new_d = []
		for a in xrange(0,len(d),2):
			new_d.append((d[a],d[a+1]))
		d = new_d

final4  = []
midwest = NCAA(divisions[0],0)
south   = NCAA(divisions[1],0)
west    = NCAA(divisions[2],0)
east    = NCAA(divisions[3],0)
final4.append((midwest[-1],west[-1]))
final4.append((south[-1],east[-1]))
finals  = NCAA(final4,0)

def Print_Brackets():
	#print   MIDWEST  SOUTH
		#               x
		#        WEST      EAST
		# 	team1 										team1
		# 		team1 								team1
		# 	team2 	 									team2
		# 			team1 						team1
		# 	team3 	 									team3
		# 		team3 								team3
		# 	team4 		 								team4
		# 				team1 				team1
		# 	team5 										team5
		# 		team5 								team5
		# 	team6 	 									team6
		# 			team5 						team5
		# 	team7 										team7
		# 		team17 								team7
		# 	team8 			 							team8
		# 					team1 		team1
		# 	team9 										team9
		# 		team9								team9
		# 	team10 	 									team10
		# 			team9 						team9
		# 	team11 										team11
		# 		team11 								team11
		# 	team12 	 									team12
		# 				team9 				team9
		# 	team13 										team13
		# 		team13 								team13
		# 	team14 	 									team14
		# 			team13 						team13
		# 	team15 										team15
		# 		team15 								team15
		# 	team16 										team16

	#do midwest / south first 
	print midwest[0][0] + "\t"*len_away + south[0][0]
	print "\t"*1 + midwest[1][0] + "\t"*(len_away-2) + south[1][0]
	print midwest[0][1] + "\t"*len_away + south[0][1]
	print "\t"*2 + midwest[2][0] + "\t"*(len_away-4) + south[2][0]
	print midwest[0][2] + "\t"*len_away + south[0][2]
	print "\t"*1 + midwest[1][1] + "\t"*(len_away-2) + south[1][1]
	print midwest[0][3] + "\t"*len_away + south[0][3]
	print "\t"*3 + midwest[3][0] + "\t"*(len_away-6) + south[3][0]
	print midwest[0][4] + "\t"*len_away + south[0][4]
	print "\t"*1 + midwest[1][2] + "\t"*(len_away-2) + south[1][2]
	print midwest[0][5] + "\t"*len_away + south[0][5]
	print "\t"*2 + midwest[2][1] + "\t"*(len_away-4) + south[2][1]
	print midwest[0][6] + "\t"*len_away + south[0][6]
	print "\t"*1 + midwest[1][3] + "\t"*(len_away-2) + south[1][3]
	print midwest[0][7] + "\t"*len_away + south[0][7]
	print "\t"*4 + midwest[4][0] + "\t"*(len_away-8) + south[4][0]
	print midwest[0][8] + "\t"*len_away + south[0][8]
	print "\t"*1 + midwest[1][4] + "\t"*(len_away-2) + south[1][4]
	print midwest[0][9] + "\t"*len_away + south[0][9]
	print "\t"*2 + midwest[2][2] + "\t"*(len_away-4) + south[2][2]
	print midwest[0][10] + "\t"*len_away + south[0][10]
	print "\t"*1 + midwest[1][5] + "\t"*(len_away-2) + south[1][5]
	print midwest[0][11] + "\t"*len_away + south[0][11]
	print "\t"*3 + midwest[3][1] + "\t"*(len_away-6) + south[3][1]
	print midwest[0][12] + "\t"*len_away + south[0][12]
	print "\t"*1 + midwest[1][6] + "\t"*(len_away-2) + south[1][6]
	print midwest[0][13] + "\t"*len_away + south[0][13]
	print "\t"*2 + midwest[2][3] + "\t"*(len_away-4) + south[2][3]
	print midwest[0][14] + "\t"*len_away + south[0][14]
	print "\t"*1 + midwest[1][7] + "\t"*(len_away-2) + south[1][7]
	print midwest[0][15] + "\t"*len_away + south[0][15]

	print "\n\n\n\n"

	print west[0][0] + "\t"*len_away + east[0][0]
	print "\t"*1 + west[1][0] + "\t"*(len_away-2) + east[1][0]
	print west[0][1] + "\t"*len_away + east[0][1]
	print "\t"*2 + west[2][0] + "\t"*(len_away-4) + east[2][0]
	print west[0][2] + "\t"*len_away + east[0][2]
	print "\t"*1 + west[1][1] + "\t"*(len_away-2) + east[1][1]
	print west[0][3] + "\t"*len_away + east[0][3]
	print "\t"*3 + west[3][0] + "\t"*(len_away-6) + east[3][0]
	print west[0][4] + "\t"*len_away + east[0][4]
	print "\t"*1 + west[1][2] + "\t"*(len_away-2) + east[1][2]
	print west[0][5] + "\t"*len_away + east[0][5]
	print "\t"*2 + west[2][1] + "\t"*(len_away-4) + east[2][1]
	print west[0][6] + "\t"*len_away + east[0][6]
	print "\t"*1 + west[1][3] + "\t"*(len_away-2) + east[1][3]
	print west[0][7] + "\t"*len_away + east[0][7]
	print "\t"*4 + west[4][0] + "\t"*(len_away-8) + east[4][0]
	print west[0][8] + "\t"*len_away + east[0][8]
	print "\t"*1 + west[1][4] + "\t"*(len_away-2) + east[1][4]
	print west[0][9] + "\t"*len_away + east[0][9]
	print "\t"*2 + west[2][2] + "\t"*(len_away-4) + east[2][2]
	print west[0][10] + "\t"*len_away + east[0][10]
	print "\t"*1 + west[1][5] + "\t"*(len_away-2) + east[1][5]
	print west[0][11] + "\t"*len_away + east[0][11]
	print "\t"*3 + west[3][1] + "\t"*(len_away-6) + east[3][1]
	print west[0][12] + "\t"*len_away + east[0][12]
	print "\t"*1 + west[1][6] + "\t"*(len_away-2) + east[1][6]
	print west[0][13] + "\t"*len_away + east[0][13]
	print "\t"*2 + west[2][3] + "\t"*(len_away-4) + east[2][3]
	print west[0][14] + "\t"*len_away + east[0][14]
	print "\t"*1 + west[1][7] + "\t"*(len_away-2) + east[1][7]
	print west[0][15] + "\t"*len_away + east[0][15]

def Print_Finals():
	print "\t"*3 + finals[0][0] + "\t"*(len_away-6) + finals[0][2]
	print "\t"*4 + finals[1][0] + "\t"*(len_away-8) + finals[1][1]
	print "\t"*3 + finals[0][1] + "\t"*(len_away-6) + finals[0][3]
	print "\t"*4 + "Winner:: " + finals[3]


Print_Brackets()
Print_Finals()










