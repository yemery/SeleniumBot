

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



def getData(webPath):
    
    driver.get(webPath)
    emp=driver.find_elements(By.XPATH,"/html/body/table/tbody/tr/td")
    print(len(emp))
    arr=[]
    for i in range(2,len(emp)):
        s=driver.find_elements(By.XPATH,"/html/body/table/tbody/tr[{0}]/td".format(i))
        for i in s:
            arr.append(i.text)

    print(arr)
        
       

        
        
 


        

   
    

 
    

    
    # storeData=[]
    # for i in emp:
 
    #     storeData.append(i.text)
    # for i in storeData:
    #     if(i==''):
    #         print('*')
       


    
    # # print(nestedArr)
    # print(storeData)





getData("http://127.0.0.1:5500/Test/Test0.html")
     











time.sleep(10)
