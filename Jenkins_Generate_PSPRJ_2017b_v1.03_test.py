__author__ = 'uidn7432'

# Information
print '*********************************************************************************************'
print 'STARTED PYTHON SCRIPT TO GENERATE THE POLYSPACE PROJECT (PSPRJ) FILE!!!'
print '*********************************************************************************************'

#***************** Import required modules*****************************************#
#from lxml import etree as ET
import xml.etree.ElementTree as ET
import datetime
import os
import shutil
import time
from xml.dom import minidom
from distutils.dir_util import copy_tree
#***********************************************************************************#
global file_dir

def multi_psprj(Component_list):
    #************Take the inputs from user: component and source_location****************#
    # Take the input as the name of the module
    #name_of_module=raw_input('ENTER THE MODULE NAME FOR WHICH THE POLYSPACE PROJECT FILE IS TO BE CREATED:')
    share_drive_path = 'D:\\'
    #component_name=os.environ['COMPONENT_NAME']
    #sandbox_path=share_drive_path+os.environ['PROJECT_SOURCE_LOCATION']
    #abspath = os.path.abspath(__file__)
    #file_dir = os.path.dirname(abspath)
    #sandbox_path='D:\\Backup_data\Polyspace_sandbox\ARS410VW26\Algo\\06_03_2019'
    sandbox_path=file_dir
    #name_of_module='CML'
    #component_name='CML'
    component_name = Component_list
    #***********************************************************************************#

    #*************To fetch the component form Inputs folder(Config and Template) using the user input****#
    #*******and then copy it to /04_Engineering/03_Workspace/Polyspace_2016a*****************************#
    script_dir = sandbox_path.replace('\\','/')
    sandbox_path1=sandbox_path
    script_dir1=script_dir
    script_dir2=script_dir

    #script_dir1=script_dir1.replace('\\','/')+'/_Config/'+component_name
    #sandbox_path=sandbox_path.replace('\\','/')+'/_inputs/Polyspace_2017b/_Config/'+component_name
    #if not os.path.exists(script_dir1):copy_tree(sandbox_path, script_dir1)

    #script_dir2=script_dir2.replace('\\','/')+'/_Template/'+component_name
    #sandbox_path1=sandbox_path1.replace('\\','/')+'/_inputs/Polyspace_2017b/_Template/'+component_name
    #if not os.path.exists(script_dir2):copy_tree(sandbox_path1, script_dir2)

    #script_dir=os.path.dirname(os.path.abspath(__file__))
    #script_dir=script_dir.replace('\\','/')
    #template_option_file=script_dir.replace('\\','/')+'/_Config/'+component_name+'/options_command.txt'
    template_option_file=sandbox_path+'/_Config/'+'/options_command.txt'
    polyspace_project_name=''
    #****************************************************************************************************#

    #*************options commanad file is fetched and read into file_lines******************************#
    f=open(template_option_file,'r')
    file_lines=f.readlines()
    f.close()
    #****************************************************************************************************#

    #*************Fetch today's date to update in the .psprj file which will be created******************#
    date_today=datetime.datetime.now().strftime("%d/%m/%Y")
    #****************************************************************************************************#


    #**************Declaration of few required variables*************************************************#
    actual_option_file_array=[]
    actual_option_tags=[]
    actual_option_file_array_split=[]
    other_options=''
    target_name=''
    target_node=''
    code_language=''
    #****************************************************************************************************#

    #*Make a list of all the options which have been enabled in the options command file using file_lines#
    #***********************options are saved in actual_option_file_array[]******************************#
    for line in file_lines:
        if not (line.startswith('#')or(line=='\n')):
            actual_option_file_array.append(line[:-1])
            actual_option_tags.append(line.split(None, 1)[0])
    #****************************************************************************************************#

    #********************To join the splitted options from actual_option_file_array to data1*************#
    for i in range(0,len(actual_option_file_array)):
         data=actual_option_file_array[i].split('#')
         data1=' '.join(data[0].split())
         data1=data1.split(' ')
         actual_option_file_array_split.append(data1)#data1 is again saved into actual_option_file_array_split.append
    #****************************************************************************************************#

    #*To handle other option -static-headers-object option and also join the splitted options to data1***#
    #for i in range(0,len(actual_option_file_array)):
    #    data=actual_option_file_array[i].split('#')
    #    if ('-static-headers-object' in data[0]):
    #        other_options=data[0]
    #    data1=' '.join(data[0].split()) # To remove unwanted white spaces
    #    data1=data1.split(' ')
    #    actual_option_file_array_split.append(data1)#data1 is again saved into actual_option_file_array_split.append
    #****************************************************************************************************#

    #********Fetch polyspace project name: using -prog keyword*******************************************#
    for i in range(0,len(actual_option_file_array_split)):
        if ('-prog' in actual_option_file_array_split[i]):
            polyspace_project_name=actual_option_file_array_split[i][1]
    #****************************************************************************************************#

    # To generate the _out folder and create a .psprj inside it******************************************#
    out_folder_path=script_dir+'/_out/'+component_name+'/'+polyspace_project_name+'/X_SCT/PolySpace/precise'
    if not os.path.exists(out_folder_path): os.makedirs(out_folder_path)
    print 'out_path' +out_folder_path
    psprj_path=out_folder_path+'/'+polyspace_project_name+'.psprj'
    print 'psprj_path' +psprj_path
    #if not os.path.exists(script_dir+'/Polyspace_Analysis.py'):shutil.copy2('D:/Jenkins/Python/Polyspace_Analysis.py', script_dir+'/Polyspace_Analysis.py')
    #shutil.copy2(script_dir+'/Polyspace_Analysis.py', out_folder_path)
    #****************************************************************************************************#

    #*****Function definition to start filling the .psprj file for Polysapce 2016a***********************#
    def psprj_2017():
    #*****To create the basic structure of the .psprj xml file: all the optionset tags in the xml tree***#
        print 'WE ARE INSIDE THE FUNCTION' +psprj_path
        root = ET.Element("polyspace_project", name=polyspace_project_name, product="Polyspace Code Prover", path='file:/'+psprj_path, source="Code Prover", version="1.0", rev="1.8", date=date_today)
        all_source_node = ET.SubElement(root, "source") # Create source node
        all_include_node = ET.SubElement(root, "include") # Create include node
        component_node = ET.SubElement(root, "module") # Create module node
        component_node.attrib['name']=polyspace_project_name+'_'+component_name+'_precise' # Create module name attrib
        #component_node.attrib['path']="file:/"+os.path.dirname(psprj_path)+'/precise'+'/'+polyspace_project_name+'_'+component_name+'_precise' # Create module path attrib
        component_node.attrib['path']="file:/"+os.path.dirname(psprj_path)+'/'+'Results_'+polyspace_project_name+'_'+component_name+'_precise' # Create module path attrib
        component_source_node=ET.SubElement(component_node, "source") # Create module source node
        component_optionset_node=ET.SubElement(component_node, "optionset") # Create module optionset node
        component_optionset_node.attrib['name']=polyspace_project_name+'_'+component_name+'_precise' # Create component optionset name attrib
        component_result_node=ET.SubElement(component_node, "result") # Create module result node
        component_result_path_node=ET.SubElement(component_result_node, "file") # Create module result folder path node
        component_result_path_node.attrib['path']="file:/"+os.path.dirname(psprj_path)+'/Results_'+polyspace_project_name+'_'+component_name+'_precise' # Create module result folder path attrib

    #*Declarations required to handle options
        include_order=0
        force_include_order=0
        component_macro_def_node_check=0
        component_macro_undef_node_check=0
    #*To enable batch option and disable add-to-results-repository*
        ET.SubElement(component_optionset_node, "option", flagname="*_batch-code-prover").text = 'true'
    #2017b supports both bug finder and code prover
        ET.SubElement(component_optionset_node, "option", flagname="-bug-finder").text='false'
        #ET.SubElement(component_optionset_node, "option", flagname="-add-to-results-repository").text = 'false'
    #To stop if any compilation errors in the 2017b Analysis
        ET.SubElement(component_optionset_node, "option", flagname="-stop-if-compile-error").text='true'
    #*Check few mandatory options and set it in psprj file*
        if ('-dos' not in actual_option_tags):
            ET.SubElement(component_optionset_node, "option", flagname="-dos").text='false'
        if ('-main-generator' not in actual_option_tags):
            ET.SubElement(component_optionset_node, "option", flagname="*_main").text='true'
            ET.SubElement(component_optionset_node, "option", flagname="main_generator").text = 'false'
        if ((('-misra2' in actual_option_tags)or('-misra-ac-agc' in actual_option_tags)or('-misra3' in actual_option_tags)or('-custom-rules' in actual_option_tags))and('-includes-to-ignore' not in actual_option_tags)):
            ET.SubElement(component_optionset_node, "option", flagname="*_files-and-folders-to-ignore").text='false'
        if (('-entry-points' in actual_option_tags)or('-critical-section-begin' in actual_option_tags)or('-critical-section-end' in actual_option_tags)or('-temporal-exclusions-file' in actual_option_tags)):
            ET.SubElement(component_optionset_node, "option", flagname="*_multitasking").text='true'
        if (('-report-template' in actual_option_tags)or('-report-output-format' in actual_option_tags)):
            ET.SubElement(component_optionset_node, "option", flagname="*_report-generation").text='true'

    #****************************************************************************************************#

        #***To create most of the options using the list of optionset nodes created in the above lines of the code**#
        for i in range(0, len(actual_option_file_array_split)):

            # Add options related to author
            if ('-author' in actual_option_file_array_split[i][0]):
                root.attrib['author'] = actual_option_file_array_split[i][1]
            #****************************************************************************************************#
            # Add options related to source file list
            # Read all the source file paths in source_command.txt and keep it in source_data
            #elif ('-sources-list-file' in actual_option_file_array_split[i][0]):
             #   file_source=open(actual_option_file_array_split[i][1],'r')
            #    source_data=file_source.readlines()
            #    file_source.close()
                # To remove the new line character in source data and create nodes attribs
                # Then add the source files to both project and component
             #   for source_file in source_data:
             #       if ('\n' in source_file):
             #           source_file_path=source_file[:-1]
             #       else: source_file_path=source_file
             #       ET.SubElement(all_source_node, "file", path="file:/"+source_file_path.replace('\\','/')) # Add the source file paths to the main source node
             #       ET.SubElement(component_source_node, "file", path="file:/" + source_file_path.replace('\\', '/')) # Add the source file paths to the module source node
            elif ('-sources-list-file' in actual_option_file_array_split[i][0]):
                source_file=script_dir.replace('\\','/')+'/_Config/'+component_name+'/source_command.txt'
                #source_file = 'C:\\Users\uidn7432\Desktop\EM\c_sourcelist_algo.xml'
                file_source=open(source_file,'r')
                source_list=file_source.readlines()
                file_source.close()
                #sort the file for hierarchical path list.
                source_data=sorted(source_list, key=lambda file: (os.path.dirname(file), os.path.basename(file)))
                # To remove the new line character in source data and create nodes attribs
                # Then add the source files to both project and component
                source_root=[]
                for source_file in source_data:
                    source_file_path=source_file.strip()
                    (head,tail)=os.path.split(source_file_path)
                    if head not in source_root:
                        source_root.append(head)
                        root_source_node=ET.SubElement(all_source_node, "root_folder", path="file:/"+head.replace('\\','/')) # Add the source file paths to the main source node
                        ET.SubElement(root_source_node,"file",path=tail)
                        root_comp_node=ET.SubElement(component_source_node, "root_folder", path="file:/"+head.replace('\\','/')) # Add the source file paths to the module source node
                        ET.SubElement(root_comp_node,"file",path=tail)
                    else:
                        ET.SubElement(root_source_node,"file",path=tail)
                        ET.SubElement(root_comp_node,"file",path=tail)
            #****************************************************************************************************#
            # Add options related to language of the source files
            elif ('-lang' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-lang").text=actual_option_file_array_split[i][1]

            # Add options related to user include paths
            # adding includes only to project and not to component, as component picks it up automatically
            elif ('-I' == actual_option_file_array_split[i][0]):
                ET.SubElement(all_include_node, "file", path="file:/" + actual_option_file_array_split[i][1].replace('\\', '/')+'/', order=str(include_order))
                # checking the include_order in order to add the component include xml header once.
                #if (include_order==0): # To check if component_include_node is already created or not
                #    component_include_node=ET.SubElement(component_optionset_node, "option", flagname="-I")
                #-------------------------------------------------------------------------------------------
                # does not require to add the Include paths to both Project and module, hence commented the code above
                include_order=include_order+1 # Include order to update the order attribute
                #add the same includes for the component
                #ET.SubElement(component_include_node, "element").text="file:/" + actual_option_file_array_split[i][1].replace('\\', '/')+'/'
            #****************************************************************************************************#
            # Add options related to macros
            elif ('-D' == actual_option_file_array_split[i][0]):
                if (component_macro_def_node_check==0): # To check if compoent_macros_def_node is already created or not
                    component_macro_def_node = ET.SubElement(component_optionset_node, "option", flagname="-D")
                    component_macro_def_node_check=1 # Make component_macro_def_node_check=1 to indicate the node creation
                ET.SubElement(component_macro_def_node, "element").text=actual_option_file_array_split[i][1]
            #****************************************************************************************************#
            # Add options related to disabled macros
            elif ('-U' == actual_option_file_array_split[i][0]):
                if (component_macro_undef_node_check==0): # To check if compoent_macro_undef_node is already created or no
                    component_macro_undef_node = ET.SubElement(component_optionset_node, "option", flagname="-U")
                    component_macro_undef_node_check=1 # Make component_macro_undef_node_check=1 to indicate the node creation
                ET.SubElement(component_macro_undef_node, "element").text=actual_option_file_array_split[i][1]
            #****************************************************************************************************#
            # Add options related to OS target
            elif (('-OS-target' == actual_option_file_array_split[i][0])and('no-predefined-OS' != actual_option_file_array_split[i][1])):
                ET.SubElement(component_optionset_node, "option", flagname="-OS-target").text=actual_option_file_array_split[i][1]
            #****************************************************************************************************# 
            elif (('-compiler' == actual_option_file_array_split[i][0])and('generic' != actual_option_file_array_split[i][1])):
                ET.SubElement(component_optionset_node, "option", flagname="-compiler").text=actual_option_file_array_split[i][1]
            # Add options related to target
            elif (('-target' == actual_option_file_array_split[i][0])):
                target_name=actual_option_file_array_split[i][1]
                if (('i386' != actual_option_file_array_split[i][1])and('mcpu' != actual_option_file_array_split[i][1])):
                    ET.SubElement(component_optionset_node, "option", flagname="-target").text=actual_option_file_array_split[i][1]
                elif ('mcpu' == actual_option_file_array_split[i][1]):
                    ET.SubElement(component_optionset_node, "option", flagname="-target").text= polyspace_project_name+'_'+component_name+'_Target'
            #****************************************************************************************************#
            # Add options which are dialect dependent
            elif ('-sfr-types' == actual_option_file_array_split[i][0]):
                sfr_types_option_node = ET.SubElement(component_optionset_node, "option", flagname="-sfr-types")
                sfr_types_option = actual_option_file_array_split[i][1].split(',')
                for i in range(0, len(sfr_types_option)):
                    ET.SubElement(sfr_types_option_node, "element").text = sfr_types_option[i]
            #****************************************************************************************************#
            # Add options related to force includes
            elif ('-include' == actual_option_file_array_split[i][0]):
                if (force_include_order==0): # To check if component_force_include_node is already created or no
                    component_force_include_node=ET.SubElement(component_optionset_node, "option", flagname="-include")
                    force_include_order=1 # Make force_include_order=1 to indicate the node creation
                ET.SubElement(component_force_include_node, "element").text="file:/" + actual_option_file_array_split[i][1].replace('\\', '/')
            #****************************************************************************************************#
            # Add options related to dialect
            elif (('-dialect' == actual_option_file_array_split[i][0])and('none' != actual_option_file_array_split[i][1])):
                ET.SubElement(component_optionset_node, "option", flagname="-dialect").text=actual_option_file_array_split[i][1]
            #****************************************************************************************************#
            # To add few other options
            elif ('-div-round-down' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-div-round-down").text='true'

            elif ('-enum-type-definition' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-enum-type-definition").text=actual_option_file_array_split[i][1]

            elif ('-logical-signed-right-shift' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-logical-signed-right-shift").text='Logical'

            elif ('-data-range-specifications' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-data-range-specifications").text='file:/'+actual_option_file_array_split[i][1].replace('\\','/')

            elif ('-no-automatic-stubbing' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-no-automatic-stubbing").text='true'

            elif ('-no-def-init-glob' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-no-def-init-glob").text='true'

            elif ('-functions-to-stub' == actual_option_file_array_split[i][0]):
                function_stub_option_node = ET.SubElement(component_optionset_node, "option", flagname="-functions-to-stub")
                function_stub_option=actual_option_file_array_split[i][1].split(',')
                for i in range(0,len(function_stub_option)):
                    ET.SubElement(function_stub_option_node, "element").text = function_stub_option[i]

            elif ('-includes-to-ignore' == actual_option_file_array_split[i][0]):
                if ('all-headers' != actual_option_file_array_split[i][1]):
                    ET.SubElement(component_optionset_node, "option", flagname="-includes-to-ignore").text=actual_option_file_array_split[i][1]

            elif ('-entry-points' == actual_option_file_array_split[i][0]):
                entry_point_option_node = ET.SubElement(component_optionset_node, "option", flagname="-entry-points")
                entry_point_option=actual_option_file_array_split[i][1].split(',')
                for i in range(0,len(entry_point_option)):
                    ET.SubElement(entry_point_option_node, "element").text = entry_point_option[i]

            elif (('-critical-section-begin' == actual_option_file_array_split[i][0])or('-critical-section-end' == actual_option_file_array_split[i][0])):
                critical_section_option_node = ET.SubElement(component_optionset_node, "option", flagname=actual_option_file_array_split[i][0])
                critical_section_option=actual_option_file_array_split[i][1].split(',')
                for i in range(0,len(critical_section_option)):
                    critical_section_option_split=critical_section_option[i].split(':')
                    ET.SubElement(critical_section_option_node, "element").text = critical_section_option_split[0]

            elif ('-temporal-exclusions-file' == actual_option_file_array_split[i][0]):
                temporal_exclusion_option_node = ET.SubElement(component_optionset_node, "option", flagname="-temporal-exclusions-file")
                file=open(actual_option_file_array_split[i][1], 'r')
                temporal_exclusion_option=file.readlines()
                file.close()
                for i in range(0,len(temporal_exclusion_option)):
                    ET.SubElement(temporal_exclusion_option_node, "element").text = temporal_exclusion_option[i][:-1]

            elif ('-continue-with-compile-error' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-continue-with-compile-error").text='true'

            elif ('-post-preprocessing-command' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-post-preprocessing-command").text=actual_option_file_array_split[i][1]

             # Add some other options
            elif ('-boolean-types' == actual_option_file_array_split[i][0]):
                boolean_option_node = ET.SubElement(component_optionset_node, "option", flagname="-boolean-types")
                boolean_option=actual_option_file_array_split[i][1].split(',')
                for i in range(0,len(boolean_option)):
                    ET.SubElement(boolean_option_node, "element").text = boolean_option[i]
            #****************************************************************************************************#
            # Add options related to MISRA rules
            elif ('-misra2' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="*_misra2").text = 'true'
                if (('all-rules' == actual_option_file_array_split[i][1])or('SQO-subset1' == actual_option_file_array_split[i][1])or('SQO-subset2' == actual_option_file_array_split[i][1])):
                    ET.SubElement(component_optionset_node, "option", flagname="-misra2").text=actual_option_file_array_split[i][1]
                elif('required-rules' != actual_option_file_array_split[i][1]):
                    misra2_option_node = ET.SubElement(component_optionset_node, "option", flagname="-misra2")
                    ET.SubElement(misra2_option_node, "element").text='file:/'+actual_option_file_array_split[i][1].replace('\\','/')

            elif ('-misra-ac-agc' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="*_misra-ac-agc").text = 'true'
                if (('OBL-REC-rules' == actual_option_file_array_split[i][1])or('all-rules' == actual_option_file_array_split[i][1])or('SQO-subset1' == actual_option_file_array_split[i][1])or('SQO-subset2' == actual_option_file_array_split[i][1])):
                    ET.SubElement(component_optionset_node, "option", flagname="-misra-ac-agc").text=actual_option_file_array_split[i][1]
                elif ('OBL-rules' == actual_option_file_array_split[i][1]):
                    misra_ac_agc_option_node = ET.SubElement(component_optionset_node, "option", flagname="-misra-ac-agc")
                    ET.SubElement(misra_ac_agc_option_node, "element").text='file:/'+actual_option_file_array_split[i][1].replace('\\','/')

            elif ('-misra3' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="*_misra3").text = 'true'
                if (('mandatory' == actual_option_file_array_split[i][1])or('all' == actual_option_file_array_split[i][1])or('SQO-subset1' == actual_option_file_array_split[i][1])or('SQO-subset2' == actual_option_file_array_split[i][1])):
                    ET.SubElement(component_optionset_node, "option", flagname="-misra3").text=actual_option_file_array_split[i][1]
                elif ('mandatory-required' != actual_option_file_array_split[i][1]):
                    misra3_option_node = ET.SubElement(component_optionset_node, "option", flagname="-misra3")
                    ET.SubElement(misra3_option_node, "element").text='file:/'+actual_option_file_array_split[i][1].replace('\\','/')

            elif ('-misra3-agc-mode' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-misra3-agc-mode").text='true'

            elif ('-custom-rules' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="*_custom-rules").text = 'true'
                ET.SubElement(component_optionset_node, "option", flagname="-custom-rules").text='file:/'+actual_option_file_array_split[i][1].replace('\\','/')
            #****************************************************************************************************#
            # Add options related to verfication method like verify whole application or verify whole module
            elif ('-main-generator-writes-variables' == actual_option_file_array_split[i][0]):
                if (('custom=' not in actual_option_file_array_split[i][1])and('public' != actual_option_file_array_split[i][1])):
                    ET.SubElement(component_optionset_node, "option", flagname='-main-generator-writes-variables').text = actual_option_file_array_split[i][1]
                elif ('custom=' in actual_option_file_array_split[i][1]):
                    custom_option=actual_option_file_array_split[i][1].split('=')
                    custom_option_split=custom_option[1].split(',')
                    custom_option_node = ET.SubElement(component_optionset_node, "option", flagname="-main-generator-writes-variables")
                    for i in range(0,len(custom_option_split)):
                        ET.SubElement(custom_option_node, "element").text=custom_option_split[i]

            elif ('-main-generator-calls' == actual_option_file_array_split[i][0]):
                if (('custom=' not in actual_option_file_array_split[i][1])and('unused' != actual_option_file_array_split[i][1])):
                    ET.SubElement(component_optionset_node, "option", flagname='-main-generator-calls').text = actual_option_file_array_split[i][1]
                elif ('custom=' in actual_option_file_array_split[i][1]):
                    custom_option=actual_option_file_array_split[i][1].split('=')
                    custom_option_split=custom_option[1].split(',')
                    custom_option_node = ET.SubElement(component_optionset_node, "option", flagname="-main-generator-calls")
                    for i in range(0,len(custom_option_split)):
                        ET.SubElement(custom_option_node, "element").text=custom_option_split[i]
            #****************************************************************************************************#
            # Add few other options
            elif ('-functions-called-before-main' == actual_option_file_array_split[i][0]):
                function_option_node = ET.SubElement(component_optionset_node, "option", flagname="-functions-called-before-main")
                function_option=actual_option_file_array_split[i][1].split(',')
                for i in range(0,len(function_option)):
                    ET.SubElement(function_option_node, "element").text = function_option[i]

            elif ('-unit-by-unit' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-unit-by-unit").text='true'

            elif ('-unit-by-unit-common-source' == actual_option_file_array_split[i][0]):
                unit_option_node = ET.SubElement(component_optionset_node, "option", flagname="-unit-by-unit-common-source")
                unit_option=actual_option_file_array_split[i][1].split(',')
                for i in range(0,len(unit_option)):
                    ET.SubElement(unit_option_node, "element").text = 'file:/'+unit_option[i].replace('\\','/')

            elif (('-respect-types-in-fields' == actual_option_file_array_split[i][0])or('-respect-types-in-globals' == actual_option_file_array_split[i][0])or('-ignore-float-rounding' == actual_option_file_array_split[i][0])or('-green-absolute-address-checks' == actual_option_file_array_split[i][0])):
                ET.SubElement(component_optionset_node, "option", flagname=actual_option_file_array_split[i][0]).text='true'

            elif (('-ignore-constant-overflows' == actual_option_file_array_split[i][0])or('-allow-negative-operand-in-shift' == actual_option_file_array_split[i][0])or('-allow-ptr-arith-on-struct' == actual_option_file_array_split[i][0])or('-size-in-bytes' == actual_option_file_array_split[i][0])or('-permissive-function-pointer' == actual_option_file_array_split[i][0])):
                ET.SubElement(component_optionset_node, "option", flagname=actual_option_file_array_split[i][0]).text='true'

            elif (('-scalar-overflows-checks' == actual_option_file_array_split[i][0])and('signed' != actual_option_file_array_split[i][1])):
                ET.SubElement(component_optionset_node, "option", flagname="-scalar-overflows-checks").text=actual_option_file_array_split[i][1]

            elif (('-scalar-overflows-behavior' == actual_option_file_array_split[i][0])and('truncate-on-error' != actual_option_file_array_split[i][1])):
                ET.SubElement(component_optionset_node, "option", flagname="-scalar-overflows-behavior").text=actual_option_file_array_split[i][1]

            elif (('-uncalled-function-checks' == actual_option_file_array_split[i][0])and('none' != actual_option_file_array_split[i][1])):
                ET.SubElement(component_optionset_node, "option", flagname="-uncalled-function-checks").text=actual_option_file_array_split[i][1]

            elif (('-O0' == actual_option_file_array_split[i][0])or('-O1' == actual_option_file_array_split[i][0])or('-O3' == actual_option_file_array_split[i][0])):
                ET.SubElement(component_optionset_node, "option", flagname="-O").text = actual_option_file_array_split[i][0].replace('-O','')

            elif (('-to' == actual_option_file_array_split[i][0])and('2' != actual_option_file_array_split[i][5])):
                ET.SubElement(component_optionset_node, "option", flagname="-to").text = 'Software Safety Analysis level '+actual_option_file_array_split[i][5]

            elif (('-timeout' == actual_option_file_array_split[i][0])or('-path-sensitivity-delta' == actual_option_file_array_split[i][0])):
                ET.SubElement(component_optionset_node, "option", flagname=actual_option_file_array_split[i][0]).text=actual_option_file_array_split[i][1]

            elif (('-retype-pointer' == actual_option_file_array_split[i][0])or('-retype-int-pointer' == actual_option_file_array_split[i][0])):
                ET.SubElement(component_optionset_node, "option", flagname=actual_option_file_array_split[i][0]).text='true'

            elif ('-context-sensitivity' == actual_option_file_array_split[i][0]):
                if ('auto' == actual_option_file_array_split[i][0]):
                    ET.SubElement(component_optionset_node, "option", flagname="-context-sensitivity").text = actual_option_file_array_split[i][1]
                else:
                    context_sensitivity_option_node = ET.SubElement(component_optionset_node, "option", flagname="-context-sensitivity")
                    context_sensitivity_option=actual_option_file_array_split[i][1].split(',')
                    for i in range(0,len(context_sensitivity_option)):
                        ET.SubElement(context_sensitivity_option_node, "element").text = context_sensitivity_option[i]

            elif ('-modules-precision' == actual_option_file_array_split[i][0]):
                modules_precision_option_node = ET.SubElement(component_optionset_node, "option", flagname="-modules-precision")
                modules_precision_option=actual_option_file_array_split[i][1].split(',')
                for i in range(0,len(modules_precision_option)):
                    modules_precision_option_split=modules_precision_option[i].split(':')
                    ET.SubElement(modules_precision_option_node, "element").text = modules_precision_option_split[0]+'='+modules_precision_option_split[1].replace('O','')

            elif (('-no-fold' == actual_option_file_array_split[i][0])or('-lightweight-thread-model' == actual_option_file_array_split[i][0])):
                ET.SubElement(component_optionset_node, "option", flagname=actual_option_file_array_split[i][0]).text='true'

            elif ('-k-limiting' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-k-limiting").text=actual_option_file_array_split[i][1]

            elif ('-inline' == actual_option_file_array_split[i][0]):
                inline_option_node = ET.SubElement(component_optionset_node, "option", flagname="-inline")
                inline_option=actual_option_file_array_split[i][1].split(',')
                for i in range(0,len(inline_option)):
                    ET.SubElement(inline_option_node, "element").text = inline_option[i]

            elif (('-report-template' == actual_option_file_array_split[i][0])and('Developer.rpt' not in actual_option_file_array_split[i][1])):
                report_template_option = os.path.basename(actual_option_file_array_split[i][1])
                report_template_option_split=report_template_option.split('.')
                ET.SubElement(component_optionset_node, "option", flagname="-report-template").text = report_template_option_split[0]

            elif (('-report-output-format' == actual_option_file_array_split[i][0])and('RTF' != actual_option_file_array_split[i][1])):
                ET.SubElement(component_optionset_node, "option", flagname="-report-output-format").text=actual_option_file_array_split[i][1]

            elif ('-automatic-orange-tester' == actual_option_file_array_split[i][0]):
                ET.SubElement(component_optionset_node, "option", flagname="-automatic-orange-tester").text = 'true'

            elif (('-automatic-orange-tester-tests-number' == actual_option_file_array_split[i][0])and('500' != actual_option_file_array_split[i][1])):
                ET.SubElement(component_optionset_node, "option", flagname="-automatic-orange-tester-tests-number").text=actual_option_file_array_split[i][1]

            elif (('-automatic-orange-tester-loop-max-iteration' == actual_option_file_array_split[i][0])and('1000' != actual_option_file_array_split[i][1])):
                ET.SubElement(component_optionset_node, "option", flagname="-automatic-orange-tester-loop-max-iteration").text=actual_option_file_array_split[i][1]

            elif (('-automatic-orange-tester-timeout' == actual_option_file_array_split[i][0])and('5' != actual_option_file_array_split[i][1])):
                ET.SubElement(component_optionset_node, "option", flagname="-automatic-orange-tester-timeout").text=actual_option_file_array_split[i][1]

            #****************************************************************************************************#
        #****************************end of for loop1***********************************************************#
        # Create options related to target
        if ('mcpu' == target_name):
            target_node=ET.SubElement(root, 'target')
            target_node.attrib['name']=polyspace_project_name+'_'+component_name+'_Target'
            target_node.attrib['language'] = code_language

            if ('-default-sign-of-char' not in actual_option_tags):
                ET.SubElement(target_node, "option", flagname="-default-sign-of-char").text = 'signed'

            if ('-align' not in actual_option_tags):
                ET.SubElement(target_node, "option", flagname="-align").text = '32'

        for i in range(0, len(actual_option_file_array_split)): # loop to check all the target options
            if ('-little-endian' == actual_option_file_array_split[i][0]):
                ET.SubElement(target_node, "option", flagname="-little-endian").text = 'Little'
            elif ('-big-endian' == actual_option_file_array_split[i][0]):
                ET.SubElement(target_node, "option", flagname="-big-endian").text = 'Big'
            elif ('-default-sign-of-char' == actual_option_file_array_split[i][0]):
                ET.SubElement(target_node, "option", flagname="-default-sign-of-char").text = 'unsigned'
            elif ('-align' == actual_option_file_array_split[i][0]):
                ET.SubElement(target_node, "option", flagname="-align").text = actual_option_file_array_split[i][1]
            elif (('-char-is-16bits' == actual_option_file_array_split[i][0])or('-char-is-32bits' == actual_option_file_array_split[i][0])or('-char-is-64bits' == actual_option_file_array_split[i][0])):
                ET.SubElement(target_node, "option", flagname=actual_option_file_array_split[i][0])
            elif (('-short-is-8bits' == actual_option_file_array_split[i][0])or('-short-is-32bits' == actual_option_file_array_split[i][0])or('-short-is-64bits' == actual_option_file_array_split[i][0])):
                ET.SubElement(target_node, "option", flagname=actual_option_file_array_split[i][0])
            elif (('-int-is-8bits' == actual_option_file_array_split[i][0])or('-int-is-32bits' == actual_option_file_array_split[i][0])or('-int-is-64bits' == actual_option_file_array_split[i][0])):
                ET.SubElement(target_node, "option", flagname=actual_option_file_array_split[i][0])
            elif (('-double-is-8bits' == actual_option_file_array_split[i][0])or('-double-is-16bits' == actual_option_file_array_split[i][0])or('-double-is-64bits' == actual_option_file_array_split[i][0])):
                ET.SubElement(target_node, "option", flagname=actual_option_file_array_split[i][0])
            elif (('-long-long-is-8bits' == actual_option_file_array_split[i][0])or('-long-long-is-16bits' == actual_option_file_array_split[i][0])or('-long-long-is-64bits' == actual_option_file_array_split[i][0])):
                ET.SubElement(target_node, "option", flagname=actual_option_file_array_split[i][0])
            elif (('-pointer-is-8bits' == actual_option_file_array_split[i][0])or('-pointer-is-32bits' == actual_option_file_array_split[i][0])or('-pointer-is-64bits' == actual_option_file_array_split[i][0])):
                ET.SubElement(target_node, "option", flagname=actual_option_file_array_split[i][0])
        #******************************end of second for loop for targets***********************************************#
        # Create the .psprj file with the root as its content
        print psprj_path
        #toprettyxml is imported from xml.dom.minidom which requires string input and not an etree
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
        with open(psprj_path, "w") as f:f.write(xmlstr)
        time.sleep(5)
        f.close()
        return
    #****************************************************************************************************#
    # Function call to generate psprj file
    psprj_2017()
    time.sleep(10)
    # Just a prompt before closing the program
    #wait = raw_input('PLEASE PRESS ENTER TO EXIT:') # Just to keep the run window active
    #****************************************************************************************************#


abspath = os.path.abspath(__file__)
file_dir = os.path.dirname(abspath)

components_list_file=open(file_dir+'\\component_list.txt','r')
component_list=components_list_file.readlines()
components_list_file.close()

component_list[:] = [s.replace('\n', '') for s in component_list]
#Component_list=['ALN','VDY_Custom']
for i in component_list:
    multi_psprj(i)
