from numpy import linalg
import numpy as np
import scipy.stats as ss

text_file = open("graph_4.txt", "r")
lines = text_file.readlines()
lines_temp = lines[len(lines)-1].split(',')
max_value = max(lines_temp[0],lines_temp[1])

connect_ar=[ [0]* (int(max_value)) for i in range(int(max_value))]
authority = np.mat([[1] for i in range(int(max_value))])
hub = np.mat([[1] for i in range(int(max_value))])

for text in lines:
	temp_sp = text.split(',')
	connect_ar[int(temp_sp[0])-1][int(temp_sp[1])-1] = 1
connect_mat = np.mat(connect_ar)

authority_new = authority
norm = 100
while norm > 1:
    authority_sub_temp = authority_new.copy()
    hub_sub_temp = hub.copy()
    num_authority = []
    num_hub = []
    authority_new = (connect_mat.T).dot(hub)
    hub_new = connect_mat.dot(authority_new)
    norm_authority = linalg.norm(authority_new, ord=2)
    norm_hub = linalg.norm(hub_new, ord=2)
    for i in range(len(authority_new)):
        temp_authority = authority_new[i].tolist()
        temp_hub = hub_new[i].tolist()
        num_authority.append([temp_authority[0][0] / norm_authority])
        num_hub.append([temp_hub[0][0] / norm_hub])
    authority_new = np.mat(num_authority)
    hub = np.mat(num_hub)
    sub_authority = authority_sub_temp - authority_new
    sub_hub = hub_sub_temp - hub
    norm = linalg.norm(sub_authority, ord=2) + linalg.norm(sub_hub, ord=2)

print("hub:{}".format(hub))
print("authority:{}".format(authority_new))
