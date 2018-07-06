"""
created by kunal on 03-07-2018@15:53
"""

"""
Parses all the XML files and returns a formatted output file 
"""
import xml.etree.ElementTree as ET


txt = ""
for i in range(1,301):
    i_str = str(i)
    f_name = "C-"+ i_str +".xml"

    #parses xml file
    tree = ET.parse(f_name)
    root = tree.getroot()



    #append start and end of temporal expressions with X
    for movie in root.findall("./TEXT/ILTIMEX"):
        movie.text = list(movie.attrib.values())[0] + " "+ movie.text + " "+ list(movie.attrib.values())[0]



    str_var = ET.tostring(root, encoding='utf8', method='text').decode('utf8')
    str_list = str_var.split()

    #Split । (period in Hindi) from word
    y = '।'
    for i in range(len(str_list)):
        if(str_list[i].find(y)!=-1 and len(str_list[i])>1):
            str_list[i]=str_list[i][:str_list[i].find(y)]
            str_list.insert(i+1,y)



    flag = 0
    t_flag = ''

    for token in str_list:
        if token == "P" or token=="D" or token == "F":
            t_flag = token
            if flag == 0:
                flag = 1
            elif flag == -1:
                flag = 0;
            continue
            
        if flag==0:
            txt += token + " O " + '\n'
        if flag==-1:
            txt += token + " I-" + t_flag +  '\n'    
        if flag==1:
            txt += token + " B-" + t_flag + ' \n'
            flag = -1
    


#export 
f = open("output.txt", 'w+')
f.write(txt)
f.close()