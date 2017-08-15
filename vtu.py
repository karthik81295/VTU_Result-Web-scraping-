
"""program to extract VTU student's semerster result"""


from bs4 import BeautifulSoup as bsoup 
import urllib2
res_url="http://results.vtu.ac.in/results17/result_page.php?usn=1mv13ec038"
page=urllib2.urlopen(res_url)
soup=bsoup(page,'html.parser')
tables=soup.findAll('table')
#print(tables[0].text)
table1=tables[0].findAll('td')
studentUSN=table1[1].text
print(studentUSN)
print("University Seat Number"+studentUSN)
studentName=table1[3].text
print("Student Name"+studentName)

print('************************************************************************************************')
#print(tables[1].text)
fields=[]
theaders=tables[1].findAll('thead')
headers=theaders[0].findAll('th')
for r in range(6):
	fields.append(str(headers[r].text))
print(fields)



table2=tables[1].findAll('td')
for item in table2:
	print(item.text)
print("\n")
rows=[]
BigList=[]
for item in table2:
	rows.append(str(item.text))
	if(len(rows)==6):
		BigList.append(rows)
		rows=[]
print(BigList)
print('************************************************************************************************')

print(tables[2].text)
final=tables[2].findAll('td')
print('************************************************************************************************')
totalMarks=str(final[1].text).strip(':')
FinalResult=str(final[3].text).strip(':')
print(totalMarks,FinalResult)

print("################################")
print(fields)
print(BigList)


#writing individual student score into csv file.
import csv
filename="marksVTU.csv" #already existing csv file
with open(filename,'w') as csvfile:
	csvwriter=csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	csvwriter.writerow([])
	csvwriter.writerow(["USN",studentUSN,"Student Name",studentName])
	csvwriter.writerow([])
	csvwriter.writerow(fields)
	for lists in BigList:
		csvwriter.writerow(lists)
	csvwriter.writerow([])
	csvwriter.writerow(["total marks",totalMarks,"Final Result",FinalResult])
#    csvwriter.writerow(["Final Result",FinalResult])