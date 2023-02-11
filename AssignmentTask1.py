#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install pdf2image')


# In[2]:


import pytesseract as tess
import cv2


# In[3]:


tess.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


# In[8]:


file_path= r'D:\hackathon and intern\internship\Data\Task1'


# In[9]:


import os


# In[10]:


lis= os.listdir(file_path)


# In[13]:


def file_write(text,name):
    with open(name+'.txt','w') as f:
        f.write(text)


# In[17]:


from pdf2image import convert_from_path


# In[24]:


def pdf_text_extract(path):
    pages= convert_from_path(path)
    for i,pg in enumerate(pages):
        pg.save('ImageFolder/pg{}.jpg'.format(i))
        img= cv2.imread('ImageFolder/pg{}.jpg'.format(i))
        pri= tess.image_to_string(img)
        file_write(pri,'pdfimg{}'.format(i))
    


# In[25]:



# ig= cv2.imread
# cv2.imshow(ig)


# In[28]:


for i in lis:
    path= os.path.join(file_path,i)
    if i[-3:] !='pdf':
        img= cv2.imread(path)
        pr= tess.image_to_string(img)
        file_write(pr,i[:-3])
    
    if i[-3:] == 'pdf':
        pdf_text_extract(path)


# In[ ]:




