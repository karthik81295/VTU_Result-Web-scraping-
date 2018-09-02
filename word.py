from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen
myUrl="http://www.dictionary.com/wordoftheday/"
uClient=urlopen(myUrl)
page_html=uClient.read()
uClient.close()




page_soup=soup(page_html,"html.parser")

title1=page_soup.findAll("div",{"class":"definition-header"})
print("         Word of the Day:      "+title1[0].strong.string)


wordIs=title1[0].strong.string
#file_name=wordIs+"txt"
#f.open(file_name,"w")
#f.write("todays word is ::  "+wordIs)





lists=page_soup.findAll("ol")
list1=lists[0].findAll('li')
index=1
for l in list1:
	print(str(index)+")"+l.span.text)
    #f.write(l.span.string)
	index=index+1


#f.close()
print("***************###################*********************")
