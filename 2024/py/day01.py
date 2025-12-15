import numpy as np

year = '2024'
input_folder = '../../input/' + year + '/'
day = '01'

filename = input_folder + 'day' + day + '.txt'

x = np.loadtxt(filename)
 
left = np.sort(x[:, 0])
right = np.sort(x[:, 1])

distance = int(np.abs(left - right).sum())

print('Distance:', distance)