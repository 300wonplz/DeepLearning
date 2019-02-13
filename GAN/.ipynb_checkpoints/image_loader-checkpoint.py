
# coding: utf-8

# In[35]:


from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os


# In[93]:


def load(path):
    file_name = os.listdir(path)

    data = []

    for file in file_name:
        img = Image.open(path+file, 'r')
        resized_img = img.resize((224, 224))

        r, g, b = resized_img.split()
        r_resized_img = np.asarray(np.float32(r) / 255.)
        g_resized_img = np.asarray(np.float32(g) / 255.)
        b_resized_img = np.asarray(np.float32(b) / 255.)

        rgb_resized_img = np.asarray([r_resized_img, g_resized_img, b_resized_img])

        data.append(rgb_resized_img)
        
    return data

