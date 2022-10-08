

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
 



    colorTd=driver.find_elements(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table[2]/tbody/tr/td")
    # print(len(colorTd))
    colorArr=[]
    for i in range(3,len(colorTd)):
        c=driver.find_elements(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table[2]/tbody/tr[{0}]/td".format(i))
        for i in c:
            # print(i.get_attribute('bgcolor'))
            if(i.get_attribute('bgcolor') in ["#428BCA","#FFFFFF","#1F3341","#ECCD6F"]):
                colorArr.append(i.get_attribute('bgcolor'))

    # print(colorArr,len(colorArr))
   
    # for i in colorTd:
    #     # print(i.get_attribute('bgcolor'))
    #     if(i.get_attribute('bgcolor') in ["#1F3341","#ECCD6F","#FFFFFF"]):
    #         colorArr.append(i.get_attribute('bgcolor'))
    # print(colorArr,len(colorArr))
    # print(emp.text)
    # print(colorArr)
    emp=driver.find_elements(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table[2]/tbody/tr/td")
    
    arrSt=[]
    for i in range(3,len(emp)):
        s=driver.find_elements(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table[2]/tbody/tr[{0}]/td".format(i))
        for i in s:
            arrSt.append(i.text)


    # print(arrSt)

    # storeData=[]
    # for i in emp:
    #     # print(i.text,"*")
    #     storeData.append(f'{i.text}')
    # print(storeData)


    finalArr=[]
    for i in arrSt:
        # print(i)
        if (i.startswith("Mme.") or i.startswith("M.") or i=='' ):
            strip=i.replace('\n',' ')
            finalArr.append(strip)

    # print(finalArr,len(finalArr))
    # print(finalArr)
    nestedArr=[]
    for i in range(0,len(finalArr)):
        for j in range(0,len(colorArr)):
            if(i==j):
                nestedArr.append([finalArr[i],colorArr[j]])
    # print(nestedArr)
    return nestedArr

# getData("https://www.nticrabat.com/","DEVOWFS201","coursera-front-search-banner-input")





def checkChanges(arr):
    bool=True
   
    wf=open("FinalResult/data.txt","r+")
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
        rf=open("FinalResult/data.txt",'w+')
        for i in npOldData:
            # print(i)
            joinArr=",".join(i)
            rf.writelines(f'{joinArr}\n')
        rf.close()
    return bool

grabData=getData("https://www.nticrabat.com/","DEVOWFS201","coursera-front-search-banner-input")
print(checkChanges(grabData))

# def sendMsg():
#     payload={
#             "content":'schedule has been changed , Go check it'
#     }
#     header={
#            "authorization":"OTE3ODYwMTM4NTc1MTAyMDMy.Gfqt6Y.COrDXpoZr9hYd2as3Oa2H2eMqSjgnrHu-Y3FGA"
#     }
#     requests.post("https://discord.com/api/v9/channels/1027556314865487895/messages",data=payload,headers=header)
    
# if(checkChanges(grabData)==False):
#     sendMsg()






time.sleep(10)
