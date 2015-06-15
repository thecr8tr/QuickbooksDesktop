__author__ = 'thecr8tr'

#####################################
# This is an example file for turning a list xml
# into a csv with ListID and Name Attributes
#####################################

import xml.etree.ElementTree as ET

xmlfile = open('C:\\Users\\Travis\\Desktop\\QB Sandbox\\Vendor.xml', 'r')
data = xmlfile.read()
xmlfile.close()
tree = ET.fromstring(data)

outputfile = open('C:\\Users\\Travis\\Desktop\\QB Sandbox\\Vendor.csv', 'w')

for branch in tree.iter('VendorRet'):
    print(branch[4])
    ListID = branch[0].text
    outputfile.write(ListID + ', ')
    Name = branch[4].text
    outputfile.write(Name + '\n')

outputfile.close()