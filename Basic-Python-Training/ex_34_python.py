#Topic : BASIC PYTHON
#Exercise Number : 34
##PROBLEM STATEMENT:
# Convert below python_xml_exe.xml file to the equivalent csv file
# Python Version : 3.7
"""
NOTE: Use ElementTree for XML data handling.
USE : python-xml_exe.xml from files folder.
"""
import xml.etree.ElementTree as Xet
import pandas as pd
cols = ["NODE", "ST_DURATION", "DT_VAL", "ST_VAL", "EXIST"]
rows = []
xmlparse = Xet.parse('python_xml_exe.xml')
root = xmlparse.getroot()
for i in root:
    NODE = i.find("NODE").text
    ST_DURATION = i.find("ST_DURATION").text
    DT_VAL = i.find("DT_VAL").text
    ST_VAL = i.find("ST_VAL").text
    EXIST = i.find("EXIST").text

    rows.append({"NODE": NODE,
                 "ST_DURATION": ST_DURATION,
                 "DT_VAL": DT_VAL,
                 "ST_VAL": ST_VAL,
                 "EXIST": EXIST})
df = pd.DataFrame(rows, columns=cols)
df.to_csv('output.csv')

