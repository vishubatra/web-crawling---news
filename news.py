import bs4
import urllib.request as url

path="https://www.indiatvnews.com/"
http_response=url.urlopen(path)
webpage=bs4.BeautifulSoup(http_response,'lxml')

print('''
1. SPORTS
2. INDIA
3. ENTERTAINMENT
4. EDUCATION
5. WORLD
6. BUSINESS
7. LIFESTYLE
8. FYI
9. SCIENCE
10. POLITICS
11. EXIT''')
            
news=['sports','fyi','india','world','science','politics','education','business','jobs']
while True:
    x=input("\tKONSI NEWS DEKHNI HAI? : ")
    if x==("exit"):
        break
    x=x.lower()

    newpath1=path+x
    http_response3 = url.urlopen(newpath1)
    webpage2= bs4.BeautifulSoup(http_response3,'lxml')

    data=webpage2.findAll('p',class_="title")



    print("\t\t\t","~"*20)
    
    print("\t\t\t\t","NEWS: ")
    print("\t\t\t","."*20)
    
    page2=webpage2.findAll('div',class_="content")
    for i in range(0,len(page2)):
        data=page2[i].find('a',)
        print(i+1,data.text)

    print("\t\t\t","~"*19)

    print("\t\t\t","  AUR ZYAADA NEWS:  ")
    page1=webpage2.findAll('ul',class_="list")
    for i in range(0,len(page1)):
        data=page1[i].findAll('p',class_="titel")
        print("\t\t\t","."*19)
        for i in range(0,len(data)):
            print(i+1,data[i].text)

    print("\t\t\t","~"*20)
    
    print("\t\t\t"," BOHOT ZYAADA NEWS: ")
    print("\t\t\t","."*20)
    
    page1=webpage2.find('ul',class_="rhs_story")
    data=page1.findAll('p',class_="title")
    for i in range(0,len(data)):
        print(i+1,data[i].text)
            
    print("\t\t\t","~"*25)            

    print("\t\t\t"," YE NEWS BHI DEKHTE JAA:  ")
    print("\t\t\t","."*25)
    
    if x in news :

        h1=webpage2.find('ul',class_="list")
        href=h1.findAll('p',class_="titel")
        for i in range(0,len(href)):
            print(i+1,href[i].text)

    
