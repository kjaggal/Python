import os

abspath = os.path.abspath(__file__)
file_dir = os.path.dirname(abspath)
#file_dir='D:\\test\MFC431TA19\X_SCT\PolySpace\precise'

file_dir=file_dir.replace('\\','/')
#print file_dir

components_list_file=open(file_dir+'/excel_inputs.txt','r')
#components_list_file=open('D:\\test\MFC431TA19\X_SCT\PolySpace\precise'+'/excel_inputs.txt','r')
component_list=components_list_file.readlines()
components_list_file.close()

component_list[:] = [s.replace('\n', '') for s in component_list]
#print component_list
#path = r"D:\\test\LD\\test"
#com_list=['LDDebugArray','LDDebugCommon']
string="_"

output = ["{}{}".format(i,string) for i in component_list]
print output
projectname=str(raw_input("Enter the project name: "))

for root, dirs, files in os.walk( file_dir ): # parse through file list in the current directory
    for i in output:
        for filename in files:
        #print(filename)
            if i in filename:

                source_filename = os.path.join(root, filename)
                #print(source_filename)
                target_filename = os.path.join(root, filename.replace( i, projectname+"_")) # convert spaces to _'s
                print target_filename
                os.rename(source_filename, target_filename) # rename the file
                #os.rename(i, "MFC431TA19")