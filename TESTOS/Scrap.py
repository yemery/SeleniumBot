

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
Path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(Path)


# open a website
# driver.get("https://www.nticrabat.com/")
# # select=  driver.find_elements(By.ID,)
# selectBtn=Select(driver.find_element(By.ID,"coursera-front-search-banner-input")) 
# selectBtn.select_by_visible_text('DEVOWFS201')
# oldArr=['M. YAHYAOUI', 'Mme. BOUZARZAR', 'Mme. BOUZARZAR', 'Mme. BENTALEB', 'M. YAHYAOUI', 'M. MOUSTAID', 'M. MOUSTAID', 'M. EL AISSAOUI', 'M. RHANDARI', 'M. MOUSTAID', 'M. MOUATASSIM']
def getData(webPath,grName,selectId):
    
    driver.get(webPath)
    selectBtn=Select(driver.find_element(By.ID,selectId)) 
    selectBtn.select_by_visible_text(grName)
    # aElm=driver.find_elements(By.TAG_NAME, 'a')
    # print(aElm)
    # section=driver.find_element(By.ID,'emploi')
    # try:
    #     # sectionEmp = WebDriverWait(driver, 10).until(
    #     # EC.presence_of_element_located((By.ID, "main-container"))
    #     # )

    #     # print(sectionEmp.text)
    #     driver.switch_to(driver.find_element(By.XPATH,"//*[@id='emploi']/iframe"))
    #     emp=driver.find_element(By.XPATH,"/html/body/div")
    #     print(emp.text)
        
    # except:
    #     driver.quit()
    driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='emploi']/iframe"))
    # driver.switch_to.frame("emploi")
    # emp=driver.find_element(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table[2]/tbody")
    emp=driver.find_elements(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table[2]/tbody/tr/td/font/a")
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
    # print(finalArr)
    return finalArr

    # atag=emp.find_elements(By.TAG_NAME,'a')
    # for i in emp:
    #     atag=i.find_element(By.TAG_NAME,'a')
    #     print(atag.text)

    # print(atag.text)
    # print(emp.text)
    # print(emp.text.split(' '))
    # Arrsplit=emp.text.split(' ')
    # arr=[]
    # for i in Arrsplit:
    #     i=i.split('\n')
    #     arr.append(i) 
    # print(arr)


    
    
   

# time.sleep(5)
# updatedArr=[]


# def storeData(arr):
#     df=open('Data.py','w+')
#     for i in arr:
#         df.writelines(f'"{i}"\n')
#     df.close()
    


# grabData=getData("https://www.nticrabat.com/","DEVOWFS201","coursera-front-search-banner-input")
# storeData(grabData)



def checkChanges(arr):
    bool=True

    wf=open("Data.txt","r+")
    lines=wf.readlines()
    for line in range(0,len(lines)):
        for i in range(0,len(arr)):
            # print(f'"{arr[i]}"',f'"{lines[line].rstrip()}"')
            if(i==line):
                if(lines[line].rstrip() !=arr[i]):
                    # print(lines[line]+arr[i])
                    bool=False
                    break
     
    wf.close()
    print(bool)
    if(bool==False):
        rf=open("Data.txt",'w+')
        for i in arr:
            # print(i)
            rf.writelines(f'"{i}"\n')
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




# def checkChanges(Arr):
#     boolVar=False
#     for i in range(0,len(Arr)):
#         for j in range(0,len(oldArr)):
#             if(i==j):
#                 if(Arr[i]!=oldArr[j]):
#                     print("Stop")
#                     updatedArr=Arr.copy()
#                     boolVar=True
                    
                    
#                     break
    
#     return boolVar
#     # print(updatedArr)       


# RData=getData("https://www.nticrabat.com/","DEVOWFS201","coursera-front-search-banner-input")
# print(checkChanges(RData))  


# def SendMsg():
#         payload={
#             "content":'schedule has been changed , Go check it'
#         }
#         header={
#            "authorization":"OTE3ODYwMTM4NTc1MTAyMDMy.GlM0pX.3_4PcqxUfBkH-N7yKuv7AKXWCczRXA8tZHMuag"
#         }
#         r=requests.post("https://discord.com/api/v9/channels/928725601546813513/messages",data=payload,headers=header)

# res= print(checkChanges(RData))   

# if(res==True):

#     SendMsg()
#     time.sleep(2)

time.sleep(30)