#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# In[ ]:


chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())


# In[ ]:


chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)


# In[ ]:


driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


# In[3]:


driver.get("http://loksabhaph.nic.in/Questions/Qministrysearch.aspx")


# In[4]:


Select(driver.find_element(By.ID, "ContentPlaceHolder1_ddlministry")).select_by_visible_text("WOMEN AND CHILD DEVELOPMENT")


# In[5]:


driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_search1"]').click()


# In[6]:


driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Button1"]').click()
time.sleep(60)


# In[7]:


df=pd.read_html(driver.page_source)[2]


# In[8]:


df=df.drop(0)
df=df.drop(1)


# In[9]:


df['Q.Type']=df['Q.Type'].str.replace(' PDF/WORD', '')
df['Q.Type']=df['Q.Type'].str.replace("\(Hindi\)", '')


# In[10]:


data=BeautifulSoup(driver.page_source)


# In[11]:


links=[]

answers=data.find_all("a", style="color:green;")
for answer in answers:
    link=answer['href']
    
    links.append(link)
    


# In[12]:


df['links']=links


# In[13]:


df.to_csv("LS_WCD.csv", index=False)


# In[14]:


driver.get("https://rajyasabha.nic.in/Questions/IntegratedSearchForm")


# In[15]:


Select(driver.find_element(By.ID, "ministrycode")).select_by_visible_text("WOMEN AND CHILD DEVELOPMENT")


# In[16]:


driver.find_element(By.XPATH, '//*[@id="show"]').click()
time.sleep(60)


# In[17]:


df=pd.read_html(driver.page_source)[0]


# In[18]:


data=BeautifulSoup(driver.page_source)


# In[19]:


links=[]
answers=data.select("tr a")

for answer in answers:
    if answer.text=="English":
        link=answer['href']
        
        links.append(link)


# In[20]:


df['links']=links


# In[21]:


df = df.drop('Answer', axis=1)


# In[22]:


df.to_csv("RS_WCD.csv", index=False)

