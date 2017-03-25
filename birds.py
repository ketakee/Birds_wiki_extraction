# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:46:53 2017

@author: Ketakee Nimavat
"""

from urllib.request import urlopen
import urllib
import re

list=["Knob-billed duck","Black-winged stilt","Greylag goose","Blue-cheeked Bee-eater"]


with open("D:\\code\\birdorder.txt", "w") as text_file:
    for elem in list[1:]:
        print(elem + ",", file=text_file,end="")
        name= elem.replace(" ","_")
        strname='https://en.wikipedia.org/wiki/'
        urlname=strname+name
        openwebsite= None
        try:
            openwebsite = urlopen(urlname)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("none" ,file=text_file)
        if(openwebsite):
            html = openwebsite.read()
            if(html):
                links1=re.findall(b"<td>Order:</td>\n<td><span class=\"order\"><a href=(.*) title=\"(.*)\">(.*)</a></span></td>\n</tr>\n<tr>\n<td>Family:</td>\n<td><span class=\"family\"><a href=(.*)>(.*)</a></span></td>\n</tr>\n<tr>\n<td>Genus:</td>",html)
                links2=re.findall(b"<td>Order:</td>\n<td><span class=\"order\"><a href=(.*) title=\"(.*)\">(.*)</a></span></td>\n</tr>\n<tr>\n<td>Family:</td>\n<td><span class=\"family\"><a href=\"(.*)\" title=\"(.*)\">(.*)</a></span></td>\n</tr>\n<tr>\n<td>Subfamily:</td>\n<td><span class=\"subfamily\"><a href=\"(.*)\" title=\"(.*)\">(.*)</a></span></td>\n</tr>\n<tr>\n<td>Genus",html)
                if(len(links1)>=1):
                    print(elem)
                    print(links1[0][2].decode("utf-8") + ",", file=text_file,end="")
                    print(links1[0][4].decode("utf-8")+ ",",file=text_file,end="")
                    print("none" ,file=text_file)
                    print("",file=text_file)
                else:
                    if(links2):
                        print(elem)
                        print(links2[0][2].decode("utf-8") + ",",file=text_file,end="")
                        print(links2[0][5].decode("utf-8")+ ",",file=text_file,end="")
                        print(links2[0][8].decode("utf-8"),file=text_file)
                        print("",file=text_file)
   
            else:
                print("none" ,file=text_file)
                
