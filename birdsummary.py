# -*- coding: utf-8 -*-
"""
@author: Ketakee Nimavat
"""
from urllib.request import urlopen
import urllib
import re
from nltk import sent_tokenize, word_tokenize


link="https://en.wikipedia.org/wiki/Greylag_goose"

#List of bird names
list1=["Knob-billed duck","Black-winged stilt","Greylag goose","Blue-cheeked Bee-eater"]
#list of features
list_=["build", "bill","pattern","body","young","neck","head","tail","plumage","call","breeds","migrate","feed on","pair","courtship"]

for elem in list1[2:3]:
        print(elem + ",",end="")
        name= elem.replace(" ","_")
        strname='https://en.wikipedia.org/wiki/'
        urlname=strname+name
        openwebsite= None
        try:
            openwebsite = urlopen(urlname)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("none")
        if(openwebsite):
            html = openwebsite.read()


        if(html):
            s=re.findall(b'<p>(.*)</p>',html)
            if(s):
                st=""
                for elem in s:
                    st+=str(elem)
                    st+=" "
                st=re.sub('<.*?>',' ',st)
                st=re.sub('\[.*?\]',"",st)
                st=re.sub('b\''," ",st)

        print(len(st))
        summary=""
        s=sent_tokenize(st)
        for elem in s:
            if any(word in elem for word in list_):
                summary+=elem
        print(summary)
        print(len(summary))

"""
#Further classifying each sentence of the summary into body, habitat, food habits, young ones etc.
#However, the given strategy of bag of words doesn't work very well. LDA could be used. Needs to be explored.

        body=[]
        habitat=[]
        food=[]
        young=[]
        others=[]
        summarylist=sent_tokenize(summary)
        for elem in summarylist:
            if any(word in elem for word in ['plumage','bill','head','tail']):
                body+=elem
            if any(word in elem for word in ['habitat', 'migrate','migration','wetland','breeds']):
                habitat+=elem
            if any(word in elem for word in ['feed on']):
                food+=elem
            if any(word in elem for word in ['young']):
                young+=elem
            else:
                others+=elem

        print("Physical Description")
        for elem in body:
            print(elem,end='')
        print("")
        print("--------------------")

        print("Habitat")
        for elem in habitat:
            print(elem,end='')
        print("")
        print("--------------------")



        print("Food")
        for elem in food:
            print(elem,end='')
        print("")
        print("--------------------")



        print("Young ones")
        for elem in young:
            print(elem,end='')
        print("")
        print("--------------------")


        print("Other info")

        print("Physical Description")
        for elem in others:
            print(elem,end='')
        print("")
        print("--------------------")

"""
