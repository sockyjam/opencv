#!/usr/bin/env python
# coding: utf-8

# In[183]:


import cv2
import time
from matplotlib import pyplot as plt


# In[ ]:


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print(face_cascade)


# In[204]:


img1 = cv2.imread('face4.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = img1.copy()

# plt.imshow(img1)
# plt.show()


# In[205]:


plt.figure(figsize=(12, 12))

faces = face_cascade.detectMultiScale(img1, 1.3, 5)
print("找到",len(faces),"张人脸")

for (x,y,w,h) in faces:
    cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),6)

plt.imshow(img1)
plt.show()


# In[206]:


i = 1
# print(img1.shape)
# print(faces)
for (x,y,w,h) in faces:
    item = img2[y:y+h, x:x+w]
    sub = plt.subplot(2,2,i)
    i = i + 1
    sub.imshow(item)
plt.show()


# In[ ]:




