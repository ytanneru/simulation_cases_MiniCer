import math
import os
import glob
import linecache

parameters = [[1100, 0.8, 2000], [1100, 0.8, 2500], [1100, 0.8, 3000],
	      [1100, 0.7, 2000], [1100, 0.7, 2500], [1100, 0.7, 3000],
	      [1100, 0.6, 2000], [1100, 0.6, 2500], [1100, 0.6, 3000]]

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
	os.system('rm Torque_Calculation.py')
	os.system('rm torque_data.txt')
	
