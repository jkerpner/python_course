#-​*- coding: utf-8 -*​-
import requests
from bs4 import BeautifulSoup
import csvkit

with open('test.csv', 'w') as csv_file:
    headers = [u"Namn", u"Titel", u"Verksamhetsinriktning", u"Firma", u"Telefon: ", u"Mobiltelefon: ", u"E-post: ",
            u"Födelseår: ", u"Inträdesår: ", u"Status: ", u"Webbsida: ", u"Växel: ", u"Fax: ", u"E-post: ", u"Webbsida: "]
    csv_writer = csvkit.DictWriter(csv_file,headers,delimiter=";")
    csv_writer.writeheader()

    url = "https://www.advokatsamfundet.se/Behover-du-advokat/Sok-advokat/Sokresultat/?positions=102001"
    response = requests.get(url)
    #print(response.text)
    soup = BeautifulSoup(response.text)
    divs = soup.find_all('div', {'class': "col-1"})
    print len(divs)
    for div in divs:
        link = div.find("a")
        if link:
            print(link.text)
            href = link["href"]
            sub_url = "https://www.advokatsamfundet.se" + href
            #print(sub_url)
            response = requests.get(sub_url)
            soup = BeautifulSoup(response.text)
            firm = soup.find("h3")
            print firm
            """
            area = soup.find_all("div", {'class': "heading area-of-law"})
            print area[0]
            
            
            Fungerande kod:
            """
            area = soup.find_all("div", {'class': "space-20"})
            print area[0].text
            print area[1].text
            
            """
            area = soup.find_all("div", {'class': "space-20"})
            for value in area:
                value1 = value.find("heading area-of-law")
                print value1.parent.text
            """

            div_tag_list = soup.find_all("div", {'class': "space-5"})
            print div_tag_list[0]
            dictionary = {}
            dictionary["Namn"] = link.text.strip()
            dictionary["Titel"] = div_tag_list[0].text.strip()
            dictionary["Firma"] = firm.text.strip()
            dictionary["Verksamhetsinriktning"] = area[0].text.strip()
            #for persondiv in div_tag_list:
            #    print persondiv
            #filtered_column = []
            for div_tag in div_tag_list:
                label = div_tag.find("strong")
                if label:
                #print label
                    column = label.parent.text
                    dictionary[label.text]=column.replace(label.text, "")    
            #print dictionary

            print dictionary
            csv_writer.writerow(dictionary)	


					#column_builder = dict("column", {"Inträdesår: "})
		#for row in dictionary:
		#	print row["Inträdesår: "]

#output = [{"Country": "Sweden", "2002": 4}, ...]

"""

	'Telefon: ': ,
	'Mobiltelefon: ': ,
	'E-post: ': ,
	'Födelseår: ': ,
	'Inträdesår: ': ,
	'Status: ': ,
	'Webbsida: ': ,
	'Växel: ': ,
	'Fax: ': ,
	'E-post: ': ,
	'Webbsida: ': , 

			#label = html_soppa.find("strong", text="Inträdesår: ")
			#text = label.parent.text


# Hämta en lista med alla div-taggar
div_tag_list = soup.find_all("div", {'class': "space-5"})
​
# Loopa igenom listan
for div_tag in div_tag_list:
	# Nu är div_tag en tagg, som vi i sin tur kan söka i
	label = div_tag.find("strong")

			#label = div_tag.find("strong", text="Inträdesår: ")
			#entry_year = label.parent.text



		#print(link.text + ";" + div_tag[0].text + ";" + div_tag[1].text + ";" + div_tag[2].text + ";" + div_tag[3].text + ";" + div_tag[4].text)

		#print(link.text + ";" + div_tag[0].text + ";" + div_tag[1].text + ";" + div_tag[2].text + ";" + div_tag[3].text + ";" + div_tag[4].text + ";" + div_tag[5].text + ";" + div_tag[6].text + ";" + div_tag[7].text)

#label = html_soppa.find("strong", text="Inträdesår: ")
#text = label.parent.text

#label = html_soppa.find("strong", text="Inträdesår: ")
#text = label.parent.text


#s.find(text='Inträdesår')


		#if div_tag:
		#if (div_tag[0].text):
		#	name = 
		#if (div_tag[1].text):		
		#if (div_tag[2].text):
		#if (div_tag[3].text):
		#if (div_tag[4].text):
		#if (div_tag[5].text):
		#if (div_tag[6].text):
		#if (div_tag[7].text):
		#print(div_tag[0].text)
		#print(div_tag[1].text)
		#print(div_tag[2].text)
		#print(div_tag[3].text)
		#print(div_tag[4].text)
		#print(div_tag[5].text)
		#print(div_tag[6].text)
		#print(div_tag[7].text)


dictionary = {
	'Telefon: ': ,
	'Mobiltelefon: ': ,
	'E-post: ': ,
	'Födelseår: ': ,
	'Inträdesår: ': ,
	'Status: ': ,
	'Webbsida: ': ,
	'Växel: ': ,
	'Fax: ': ,
	'E-post: ': ,
	'Webbsida: ': , 
}
"""