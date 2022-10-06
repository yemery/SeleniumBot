

from turtle import color
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

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
    print(colorArr,len(colorArr))

    

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
    print(finalArr,len(finalArr))
    return finalArr





def checkChanges(arr):
    bool=True
   
    wf=open("mainPrj/Data.txt","r+")
    lines=wf.readlines()
    
    # print(len(arr),len(lines))
    for line in range(0,len(lines)):
        for i in range(0,len(arr)):
            # print(lines[line].rstrip() ,'***', arr[i])
            # print(f'"{arr[i]}"',f'"{lines[line].rstrip()}"')
            if(i==line):
                if(lines[line].rstrip()!= arr[i] or len(arr)!=len(lines) ):
                    # print(lines[line].rstrip() +  arr[i])
                    bool=False
                    break
     
    wf.close()
    print(bool)
    # for i in arr:
    #     print(i.strip())
    if(bool==False):
        rf=open("mainPrj/Data.txt",'w+')
        for i in arr:
            # print(i)
            rf.writelines(f'{i}\n')
        rf.close()
    return bool

grabData=getData("https://www.nticrabat.com/","DEVOWFS201","coursera-front-search-banner-input")
# print(checkChanges(grabData))

def sendMsg():
    payload={
            "content":'schedule has been changed , Go check it'
    }
    header={
           "authorization":"OTE3ODYwMTM4NTc1MTAyMDMy.GUXnHF.uuKPSYu58JAHP9gfjIJ9kzCFKbQvLJENVeY_O8"
    }
    requests.post("https://discord.com/api/v9/channels/1027556314865487895/messages",data=payload,headers=header)
    
if(checkChanges(grabData)==False):
    sendMsg()






time.sleep(10)