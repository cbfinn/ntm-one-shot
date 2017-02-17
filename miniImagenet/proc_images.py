"""
Script for converting from csv file datafiles to a directory for each image. (which is how it is loaded by MAML code)

To run, put images.zip in the directory, unzip it, and then run python proc_images.py. Update datatype below to process
train, val, and test images.
"""

path_to_images = 'images/'

import csv
import os


datatype = 'train'

os.system('mkdir ' + datatype)

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

