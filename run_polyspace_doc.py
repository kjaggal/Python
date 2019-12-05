import os
import shutil
from distutils.dir_util import copy_tree
import time

abspath = os.path.abspath(__file__)
file_dir = os.path.dirname(abspath)

file_dir=file_dir.replace('\\','/')
#print file_dir

components_list_file=open(file_dir+'/excel_inputs.txt','r')
component_list=components_list_file.readlines()
components_list_file.close()

component_list[:] = [s.replace('\n', '') for s in component_list]

projectname=str(raw_input("Enter the project name: "))
dest=file_dir
#list=['new1','new2']


for i in component_list:
    #print(dest+'\\'+i)
    dest2=dest+'/'+i+'/'+projectname+'/X_SCT/PolySpace/precise/Results_'+projectname+'_'+i+'_precise/CP_Result_5'
    #command=dest2+'/Polyspace_Doc_Generation.py'
    command=dest+'/'+i+'/Polyspace_Doc_Generation.py'
    print command
    os.system(command)
    time.sleep(4)
    #copy_tree(source,dest+'/'+i)
