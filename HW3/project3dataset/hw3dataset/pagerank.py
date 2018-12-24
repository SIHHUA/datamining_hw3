from numpy import linalg
import numpy as np
import scipy.stats as ss

damping_factor = 0.15
text_file = open("graph_4.txt", "r")
lines = text_file.readlines()
lines_temp = lines[len(lines)-1].split(',')
max_value = max(lines_temp[0],lines_temp[1])

connect_ar=[ [0]* (int(max_value)+1) for i in range(int(max_value)+1)]
connect_new=[ 0* 1 for i in range(int(max_value))]

temp = lines[0][0]

for text in lines:
	temp_sp = text.split(',')
	connect_ar[int(temp_sp[0])-1][int(temp_sp[1])-1] = 1
	if temp_sp[0] == temp:
		connect_ar[int(temp_sp[0])-1][int(max_value)] += 1
	else:
		temp = temp_sp[0]
		connect_ar[int(temp_sp[0])-1][int(max_value)] += 1

#初始化PR
for i in range(int(max_value)):
	connect_ar[int(max_value)][i] = damping_factor/int(max_value)
	connect_new[i] = damping_factor/int(max_value)

norm = 100
while norm > 0.01:
	temp1 = connect_ar[int(max_value)].copy()
	for i in range(int(max_value)):
		for j in range(int(max_value)):
			if connect_ar[j][i] != 0:
				connect_new[i] = connect_new[i] + (1-damping_factor)*(connect_ar[int(max_value)][j]/connect_ar[j][int(max_value)])
	norm = linalg.norm(connect_new, ord=2)
	for i in range(int(max_value)):
		connect_new[i] = connect_new[i] /norm
	sub = []
	temp1.pop()
	sub = np.array(temp1) - np.array(connect_new)
	norm = linalg.norm(sub, ord=2)
	for i in range(int(max_value)):
		connect_ar[int(max_value)][i] = connect_new[i]
connect_ar[int(max_value)].pop()
print("pagerank:{}".format(connect_ar))