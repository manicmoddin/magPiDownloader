import requests

from bs4 import BeautifulSoup

for i in range(111):
    #print(i + 1)
    j = i + 1
    downloadPage = requests.get("https://magpi.raspberrypi.com/issues/"+ str(j) +"/pdf/download")
    detailsPage = requests.get("https://magpi.raspberrypi.com/issues/"+ str(j))
    downloadSoup = BeautifulSoup(downloadPage.content, "html.parser")
    detailsSoup = BeautifulSoup(detailsPage.content, "html.parser")

    links = downloadSoup.find(class_="c-link")
    link_url = links["href"]

    print(str(j) +" : " + link_url)
    pdf = requests.get("https://magpi.raspberrypi.com" + link_url)
    with open('MagPi' + str(j) + ".pdf", "wb") as file:
        file.write(pdf.content)

    details = detailsSoup.find(class_="rspec-issue__description")
    listItems = details.find_all("li")

    detailsFile = open('MagPi'+ str(j) + ".txt", 'a')
    for listItem in listItems:
        detailsFile.write(listItem.prettify())
        #print(listItem.prettify())

    detailsFile.close()
    #quit()

        
    
