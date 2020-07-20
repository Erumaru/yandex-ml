#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
get_ipython().magic(u'matplotlib inline')


# ## генерация выборок и расчет выборочных средних

# In[22]:


l=1.0
n=3 #задаем объем выборки
obj_exp=sts.expon(scale=1/l) #создаем объект на основе экпоненциального распределения
exmpl_mean_ar=list() #создаем список
for i in range(1000):#в цикле производим генерацию выборок
    #exmpl_mean.append(i)
#exmpl_mean  
    exmpl=obj_exp.rvs(n)  #создаем выборку, состоящей из пяти элементов 
    exmpl_mean=sum(exmpl)/n #производим расчет средней
    exmpl_mean_ar.append(exmpl_mean) #добавляем среднюю в список
#print exmpl_mean_ar
exmpl_mean_ar=np.array(exmpl_mean_ar) #преобразуем список в массив
#print exmpl_mean_ar


# ## гистограмма с наложением графика функции плотности нормального распределения

# In[19]:


fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('PDF(X)')
plt.title('n=3')
plt.hist(exmpl_mean_ar,density=True,bins=20) #строим гистограмму по выборке выборочных средних
norm =sts.norm(loc=1/l,scale=np.sqrt(1/(l**2)/n)) #создаем объект на основе нормального распредения
x=np.linspace(0,7,500)
plt.plot(x, norm.pdf(x))


# In[23]:


l=1.0
n=5 #задаем объем выборки
obj_exp=sts.expon(scale=1/l) #создаем объект на основе экпоненциального распределения
exmpl_mean_ar=list() #создаем список
for i in range(1000):#в цикле производим генерацию выборок
    #exmpl_mean.append(i)
#exmpl_mean  
    exmpl=obj_exp.rvs(n)  #создаем выборку, состоящей из пяти элементов 
    exmpl_mean=sum(exmpl)/n #производим расчет средней
    exmpl_mean_ar.append(exmpl_mean) #добавляем среднюю в список
#print exmpl_mean_ar
exmpl_mean_ar=np.array(exmpl_mean_ar) #преобразуем список в массив
#print exmpl_mean_ar
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('PDF(X)')
plt.title('n=5')
plt.hist(exmpl_mean_ar,density=True,bins=20) #строим гистограмму по выборке выборочных средних
norm =sts.norm(loc=1/l,scale=np.sqrt(1/(l**2)/n)) #создаем объект на основе нормального распредения
x=np.linspace(0,7,500)
plt.plot(x, norm.pdf(x))


# In[24]:


l=1.0
n=10 #задаем объем выборки
obj_exp=sts.expon(scale=1/l) #создаем объект на основе экпоненциального распределения
exmpl_mean_ar=list() #создаем список
for i in range(1000):#в цикле производим генерацию выборок
    #exmpl_mean.append(i)
#exmpl_mean  
    exmpl=obj_exp.rvs(n)  #создаем выборку, состоящей из пяти элементов 
    exmpl_mean=sum(exmpl)/n #производим расчет средней
    exmpl_mean_ar.append(exmpl_mean) #добавляем среднюю в список
#print exmpl_mean_ar
exmpl_mean_ar=np.array(exmpl_mean_ar) #преобразуем список в массив
#print exmpl_mean_ar
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('PDF(X)')
plt.title('n=10')
plt.hist(exmpl_mean_ar,density=True,bins=20) #строим гистограмму по выборке выборочных средних
norm =sts.norm(loc=1/l,scale=np.sqrt(1/(l**2)/n)) #создаем объект на основе нормального распредения
x=np.linspace(0,7,500)
plt.plot(x, norm.pdf(x))


# ### вывод
# Экспоненциальное распределение расмотрено при выборке 3; 5; 10 с наложнием нормального распределения показывает, см выше графики, что при увеличении объема выборки экспоненциальное распределение приближается к нормальному распределению
