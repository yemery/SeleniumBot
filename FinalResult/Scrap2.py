

from turtle import color
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

import numpy as np
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
Path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(Path)



def getData(webPath,grName,selectId):
    
    driver.get(webPath)
    selectBtn=Select(driver.find_element(By.ID,selectId)) 
    selectBtn.select_by_visible_text(grName)

    driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='emploi']/iframe"))
 
    emp=driver.find_elements(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table[2]/tbody/tr/td/font/a")
    Color=driver.find_elements(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table[2]/tbody/tr/td")
    colorArr=[]
    for i in Color:
        # print(i.get_attribute('bgcolor'))
        if(i.get_attribute('bgcolor') in ["#1F3341","#ECCD6F","#428BCA"]):
            colorArr.append(i.get_attribute('bgcolor'))
    # print(colorArr,len(colorArr))

    storeData=[]
    for i in emp:
        # print(i.text,"*")
        storeData.append(f'{i.text}')
    # print(storeData)


    finalArr=[]
    for i in storeData:
        # print(i)
        if i.startswith("M"):
            
            finalArr.append(i)
    # print(finalArr,len(finalArr))

    nestedArr=[]
    for i in range(0,len(finalArr)):
        for j in range(0,len(colorArr)):
            if(i==j):
                nestedArr.append([finalArr[i],colorArr[j]])
    print(nestedArr)
    return nestedArr





def checkChanges(arr):
    bool=True
   
    wf=open("FinalResult\data.txt","r+")
    lines=wf.readlines()
    semiArr=[]
    for i in range(0,len(lines)):
        # print(lines[i].rstrip().split(','),'*')
        semiArr.append(lines[i].rstrip().split(','))
    npSemiArr=np.array(semiArr)
    npOldData=np.array(arr)
    if(np.array_equal(npSemiArr,npOldData)==False or len(npSemiArr)!=len(npOldData)):
        bool=False
    
     
    print(bool)
    wf.close()
    if(bool==False):
        rf=open("FinalResult\data.txt",'w+')
        for i in npOldData:
            # print(i)
            joinArr=",".join(i)
            rf.writelines(f'{joinArr}\n')
        rf.close()
    return bool

grabData=getData("https://www.nticrabat.com/","DEVOWFS201","coursera-front-search-banner-input")
# print(checkChanges(grabData))

def sendMsg():
    payload={
            "content":'schedule has been changed , Go check it'
    }
    header={
           "authorization":"OTE3ODYwMTM4NTc1MTAyMDMy.Gfqt6Y.COrDXpoZr9hYd2as3Oa2H2eMqSjgnrHu-Y3FGA"
    }
    requests.post("https://discord.com/api/v9/channels/1027556314865487895/messages",data=payload,headers=header)
    
if(checkChanges(grabData)==False):
    sendMsg()






time.sleep(10)
