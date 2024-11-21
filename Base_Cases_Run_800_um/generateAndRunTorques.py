import math
import os
import glob
import linecache

parameters = [[800, 0.8, 2000], [800, 0.8, 2500], [800, 0.8, 3000],
	      [800, 0.7, 2000], [800, 0.7, 2500], [800, 0.7, 3000],
	      [800, 0.6, 2000], [800, 0.6, 2500], [800, 0.6, 3000]]

variables = ['_um_', '_percent_', '_RPM']

# case names
caseNames = []
for i in range(len(parameters)):
	caseNames.append('run_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2])

home_dir = os.getcwd()
for i in range(len(caseNames)):
	cur_dir = home_dir
	os.chdir(cur_dir)
	run_dir = cur_dir+'/'+caseNames[i]
	os.chdir(run_dir)
	os.system('cp ../Torque_Calculation.py .')
	
c_dir = home_dir
for k in range(len(caseNames)):
	os.chdir(c_dir)
	FolderPath = c_dir+'/'+caseNames[k]
	os.chdir(FolderPath)
	#print(os.getcwd())
	print('Running torque calculation in '+caseNames[k]+' ...'+'\n')
	os.system('python3 Torque_Calculation.py')
