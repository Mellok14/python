'''
import os
info = {'$NAME1':'data', '$NAME2':'table', .................}
source_dir = '/path/source_folder'
dest_dir = '/path/dest_folder'
files = os.listdir(source_dir)

for f in files:
    in_file = open(source_dir+f, 'r')
    in_file_string = in_file.read()
    out_file = open(dest_dir+f, 'w')
    for i in info.keys():
        in_file_string = in_file_string.replace(i, info[i])
    out_file.write(in_file_string)
    out_file.close
    in_file.close
'''
