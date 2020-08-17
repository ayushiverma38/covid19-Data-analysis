#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
import cufflinks as cf
import folium
from plotly .offline import download_plotlyjs,init_notebook_mode,plot,iplot
plt.rcParams['figure.figsize']=20,15


# In[15]:


pyo.init_notebook_mode(connected=True)
cf.go_offline()


# In[149]:


file =r'C:\Users\yash\Desktop\covid-19.xlsx'
df=pd.read_excel(file,usecols=['State/UT','Confirmed','Recovered','Deceased'],inplace=True)
df


# In[150]:


df.dtypes


# In[151]:


df.shape
df.info()


# In[152]:


#df[['Confirmed','Recovered']].astype('int')


# In[153]:


df.dtypes


# In[154]:


df['Active']=df['Confirmed']-df['Recovered']+df['Deceased']
df


# In[155]:


total_cases=df.Active.sum()
print('total_cases  in india is',total_cases)


# In[ ]:





# In[156]:


df.style.background_gradient(cmap ='Reds')


# In[157]:


total_active_cases=df.groupby('State/UT')['Active'].sum().to_frame().sort_values('Active',ascending=False)
total_active_cases


# In[158]:


total_active_cases.style.background_gradient(cmap='Reds')


# In[159]:


df.plot(kind='bar',x='State/UT',y='Active')#pandas vis.
df.iplot(kind='bar',x='State/UT',y='Active')


# In[160]:


#matplotlib visualization
plt.barh(df['State/UT'],df['Active'],label='active cases')
plt.legend()

plt.ylabel('state',fontsize=34)
plt.show()


# In[161]:


px.bar(df,x='State/UT',y='Active')#plotly vis.


# In[162]:


#pandas scatter plot
df.plot(kind='scatter',x='State/UT',y='Active',fontsize=15 )


# In[163]:


#matplotlib scatter
plt.scatter(x='State/UT',y='Active' ,data=df,marker='+',alpha=0.9,color='red')
plt.ylabel('Activecases')
plt.xlabel('state/UT')


# In[164]:


df.iplot(kind='scatter',x='State/UT',y='Active',fontsize=15 ,mode='markers+lines',title='Total Active Cases ',xTitle='state',yTitle='no. of cases',colors='red',size=10)


# In[165]:


px.scatter(df,x='State/UT',y='Active',symbol=df['Deceased'],color=df['State/UT'])


# In[166]:


df.columns


# In[167]:


fig=plt.figure(figsize=(25,12),dpi=200)
ax=fig.add_axes([0,0,1,1])
ax.bar(df['State/UT'],df['Active'] )
plt.title('total cases',size=25)
ax.set_xlabel('state',size=25)
plt.show()


# In[168]:


file=r'C:\Users\yash\Desktop\LON NAD LAT.xlsx'
india_cord=pd.read_excel(file,inplace=True,usecols=['State/UT','LATITUDE','LONGITUDE'])
india_cord


# In[169]:


df_full=pd.merge(df,india_cord,on='State/UT',how='inner')
df_full


# In[37]:


map=folium.Map(location=[20,70],zoom_start=4,tiles='Stamenterrain')

for lat,long,value, name in zip(df_full['LATITUDE'],df_full['LONGITUDE'],df_full['Confirmed'],df_full['State/UT']):
    folium.CircleMarker([lat,long],popup=('<strong>State</strong>: '+str(name).capitalize()+'<br>''<strong>Total Cases</strong>: ' + str(value)+ '<br>'),color='red',fill_color='white',fill_opacity=0.3).add_to(map)
map    


# In[38]:


#how corona virus is rising globally


# In[39]:



dbd_India=pd.read_excel(r"C:\Users\yash\Downloads\per_day_cases.xlsx",parse_dates=True,sheet_name="India",usecols=['Date','Total Cases','New Cases'])


# In[40]:


dbd_India


# In[41]:


#Matplotlib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.bar(dbd_India["Date"],dbd_India["Total Cases"],color='blue')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in India")
plt.show()


#plotly Express

fig=px.bar(dbd_India,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in India')
fig.show()


# In[42]:


fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(dbd_India["Date"],dbd_India["Total Cases"],color='red',marker='+')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in India")
plt.show()


# In[43]:


#plotly Express

fig=px.scatter(dbd_India,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in India')
fig.show()


# In[44]:



#Plotly
dbd_India.iplot(kind='scatter',x='Date',y='Total Cases',mode='lines+markers')


# In[45]:


#fig=go.figure()
#fig.add_trace(go.Scatter(x=dbd_India['Date'],y=dbd_India['Total Cases'],mode='lines+markers'))


# In[60]:


df_world=pd.read_excel(r'C:\Users\yash\Desktop\WORLDREPORT.xlsx')


# In[61]:


df_world


# In[68]:


df_world.query('COUNTRY=="Anguilla"')


# In[76]:


world=df_world['CASES'].sum()
print( world)


# In[78]:


df_world['DEATH'].sum()


# In[131]:


asia=df_world.query('REGION=="Asia"')


# In[170]:


asia


# In[171]:


asia.iplot(kind='bar',x='COUNTRY',y='CASES',color='red')


# In[136]:



confirmed=df.groupby('REGION').sum()['CASES'].reset_index()
death=df.groupby('REGION').sum()['DEATH'].reset_index()
print(confirmed)
print(death)


# In[138]:


fig=go.Figure()
fig.add_trace(go.Scatter(x=confirmed['REGION'],y=confirmed['CASES'],mode='lines+markers',name='Confirmed',line=dict(color='blue',width=2)))

fig.add_trace(go.Scatter(x=death['REGION'],y=death['DEATH'],mode='lines+markers',name='Deaths',line=dict(color='red',width=2)))
#fig.add_trace(go.Scatter(x=rec['Date'],y=rec['Recovered'],mode='lines+markers',name='Recovered',line=dict(color='green',width=2)))


# In[ ]:




