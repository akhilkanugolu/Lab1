

from bs4 import BeautifulSoup
import urllib.request


url = "https://catalog.umkc.edu/course-offerings/graduate/comp-sci/"
source_code = urllib.request.urlopen(url)
soup = BeautifulSoup(source_code, "html.parser")

    
for block in soup.find_all('div',{"class":"courseblock"}):
    title = block.find('span',{'class':'title'})
    over_view = block.find('p',{'class':'courseblockdesc'})
    result = "Course Title:"+str(title.text) + "\n" +"Course Overview:"+ str(over_view.text.strip())
    print(result+"\n")
    
 

