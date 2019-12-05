# __author__ = 'uidn7432' #

import xml.etree.ElementTree as ET
import os
import shutil

abspath = os.path.abspath(__file__)
file_dir = os.path.dirname(abspath)
c_sourceList_Path=file_dir + '\c_sourcelist_algo.xml'
#print file_dir

#c_sourceList_Path='C:\\Users\uidn7432\Desktop\EM\c_sourcelist_SW_SRR320NN28.xml'
#sanboxpath= "D:\\Backup_data\Polyspace_sandbox\ARS410VW26\Algo\\06_03_2019"
sanboxpath=file_dir
source_command_txt= file_dir+ '\_Config\\'


tree = ET.parse(c_sourceList_Path)
cList = []
Model_List=[]
root = tree.getroot()
#print(root.tag)
global x
global Model_name
Model_count=0

for elem in root:
    #print'model name: ',elem.tag
    Model_name= elem.attrib['id']
    #f1 = open("C:\\Users\uidn7432\Desktop\EM\\"+Model_name+'.txt', 'a')
    #f1.close()
    if elem.tag == 'model':
        #cList.append(elem.attrib['id'])
        Model_List.append(elem.attrib['id'])
        
        newpath = source_command_txt + Model_name + '\\'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            for subelem in elem:
                if subelem.tag == 'files':
                    for subsubelem in subelem:
                        sourcePath = subsubelem.text
                        if sourcePath.endswith(".c"):
                            x = sanboxpath + '\\'+ sourcePath
                            # print x
                            # f1 = open(source_command_txt+'source_command_'+Model_name+'.txt', 'a')
                            f1 = open(newpath + 'source_command' + '.txt', 'a')
                            f1.write(x + '\n')
                            f1.close()



                        #cList.append(sanboxpath + sourcePath)


#print cList
#print Model_List

#for i in cList:
#    if i.startswith('D:\\'):
 #           print(i)

f2=open(file_dir+'\\component_list.txt','w')
for i in Model_List:
    f2.writelines(i+ '\n')
f2.close()
#f1 = open(psprj_path, "w")
#for i in cList:
#    if i.startswith('D:\\'):
#        f1.writelines(i + '\n')

#print Model_count
f3="D:\\Backup_data\Polyspace_sandbox\options_command\options_command.txt"
shutil.copy2(f3,source_command_txt)
f4=source_command_txt+"\\options_command.txt"
projectname=str(raw_input("Enter the project name: "))
with open(f4) as f:
    s = f.read()
    #if s.startswith('-prog'):
    s = s.replace("-prog", "-prog "+projectname )
    with open(f4, "w") as f:
        f.write(s)
