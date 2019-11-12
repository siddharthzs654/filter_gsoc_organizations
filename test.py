import lxml.etree
import lxml.html
import requests

r19 = requests.get("https://summerofcode.withgoogle.com/archive/2019/organizations/")
r18 = requests.get("https://summerofcode.withgoogle.com/archive/2018/organizations/")
r17 = requests.get("https://summerofcode.withgoogle.com/archive/2017/organizations/")
r16 = requests.get("https://summerofcode.withgoogle.com/archive/2016/organizations/")


r19 = lxml.html.fromstring(r19.content)
r18 = lxml.html.fromstring(r18.content)
r17 = lxml.html.fromstring(r17.content)
r16 = lxml.html.fromstring(r16.content)


list2018 = []
list2019 = []
list2017 = []
list2016 = []

i = 1
while(True):
    try:
        title19 = r19.xpath(f'/html/body/main/section/div/ul/li[{i}]/a/md-card/div/h4') 
        title18 = r18.xpath(f'/html/body/main/section/div/ul/li[{i}]/a/md-card/div/h4') 
        title17 = r17.xpath(f'/html/body/main/section/div/ul/li[{i}]/a/md-card/div/h4') 
        title16 = r16.xpath(f'/html/body/main/section/div/ul/li[{i}]/a/md-card/div/h4')

        list2019.append(title19[0].text)
        list2018.append(title18[0].text)
        list2017.append(title17[0].text)
        list2016.append(title16[0].text)


        i+=1
    
    except:
        break

allyears = open('allyears.txt','a+')
newone = open('newone.txt','a+')

for name19 in list2019:
    if ((name19 in list2018) and (name19 in list2017) and (name19 in list2016)):
        allyears.write(f'{name19}\n')
    
print(" ==================================== ")
for name19 in list2019:
    if ((name19 not in list2018) and (name19 not in list2017) and (name19 not in list2016)):
        newone.write(f'{name19}\n')



# for name18 in list2018:
#     if ((name18 in list2019) and (name19 in list2017) and (name19 in list2016)):
#         print(name19,end=" || ")



    
    