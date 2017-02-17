import csv
import os


datatype = 'train'

with open(datatype+'.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    i = 0
    last_label = ''
    for row in reader:
        i+=1
        if i == 1: continue
        label = row[1]
        image_name = row[0]
        if label != last_label:
            cur_dir = datatype + '/' + label + '/'
            os.system('mkdir ' + cur_dir)
            last_label = label
        os.system('mv images/'+image_name+' ' + cur_dir)

