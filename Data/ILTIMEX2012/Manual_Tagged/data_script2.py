"""
created by kunal on 03-07-2018@15:53
modified by rishav on 04-07-2018@11:52

MODIFICATIONS MADE: 
    1. Improved formatting of output text with tabs 
    2. Cleaned up special character deletion process using regex 
    3. Added some code to consider all files in the folder and generate subsequent output text
    4. Fixed bug of missing the ending daari for each document and putting a space after each daari 
"""
import xml.etree.ElementTree as ET
import re 

file_val = []
gg = ['103', '104', '117', '123', '127', '128', '13', '140', '141', '145', '147', '167', '169', '185', '187', '188', '190', '20', '202', '211', '216', '221', '236', '238', '239', '24', '241', '247', '249', '251', '253', '267', '271', '285', '294', '298', '300', '31', '35', '41', '42', '43', '54', '56', '62', '68', '73', '79', '84', '90', '91', '96']
for indexval in gg:
    #parses xml file
    str_index=str(indexval)
    print("Processed File:"+str_index)
    tree = ET.parse('C-'+str_index+'.xml')
    root = tree.getroot()



    #append start and end of temporal expressions with quantity of "Value" attribute
    for timeExpression in root.findall("./TEXT/ILTIMEX"):
    #print(timeExpression.text)
        timeExpression.text = list(timeExpression.attrib.values())[0] + " "+ timeExpression.text + " "+ list(timeExpression.attrib.values())[0]
        #print(timeExpression.text)


    str_text = ET.tostring(root, encoding='utf8', method='text').decode('utf8')
    #str2=str
    # Experimental Split by Daari & Space using regex split  

    str_text= re.sub(r'(,|\(|\)|~|`|\.|;|:|\'|\"|\+|\{|\}|\[|\]|\\|@|#|$|%|\^|&|\*)','', str_text)
    str_text= re.sub(r'(!,?)','।', str_text)
    str_text= re.sub(r'(/)',' ', str_text)
    str_text= re.sub(r'\n',' \n ', str_text)
    #takes care of the case of double daari or "।।" 
    str_text= re.sub(r'( ॥|।।|॥)','।', str_text)
    str2_list=re.split('(।)',str_text)
    # if '-' in str_text:
    #     file_val.append(indexval)
    mod_list=[]
    for sentence in str2_list:
        mod_list.extend(sentence.split(" "))
    str_list = str_text.split()
    check_list=str_list[:]
    skip_list = ['\n']

    # Logical Code of creating the output file 
    flag = 0
    t_flag = ''
    txt = ""
    for token in mod_list:
        if token in skip_list:
            continue
        if token == "P" or token=="D" or token == "F":
            t_flag = token
            if flag == 0:
                flag = 1
            elif flag == -1:
                flag = 0;
            continue
        
        if flag==0:
        # takes care of the condtition of marking ' ' (blank space) as O 
            if token == '':
                txt += token + "\t" + '\n' 
            else:
                txt += token + "\tO" + '\n'
        if flag==-1:
            txt += token + "\tI-" + t_flag +  '\n'    
        if flag==1:
            txt += token + "\tB-" + t_flag + '\n'
            flag = -1
    


    #export 
    f = open("../BIO_TaggedM/C-"+str_index+".txt", 'w+')
    f.write(txt)
    f.close()

#print(file_val)