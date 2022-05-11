import pandas as pd
import numpy as np
import seaborn as sns
import subprocess
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:\python project\district wise rainfall normal-2.csv')
print(df)
df.STATE_UT_NAME.unique()
df.DISTRICT.unique()
#India State Wise Annual img-1
plt.figure(figsize = (20,5))
sns.barplot(x='STATE_UT_NAME', y= 'ANNUAL', data = df)
plt.xticks(rotation = 90)
plt.title('India State WISE ANNUAL RAINFALL')
plt.savefig('img1.png', format='png')

#Function for Gujarat State
df_guj = df[df.STATE_UT_NAME=='GUJARAT']

#District wise Annual Rainfall img-2
plt.figure(figsize = (20,5))
sns.barplot(x='DISTRICT', y= 'ANNUAL', data = df_guj)
plt.xticks(rotation = 90)
plt.title('GUJARAT DISTRICT WISE ANNUAL RAINFALL')
plt.savefig('img2.png', format='png')

#for india with state wise rainfall img-3
plt.figure(figsize=(20,5))
sns.lineplot(x = 'ANNUAL', y= 'JAN', hue = 'STATE_UT_NAME', data = df)
plt.title('India with state wise rainfall')
plt.savefig('img3.png', format='png')

#for Rainfall in inch in Gujarat img-4
plt.figure(figsize=(20,5))
sns.lineplot(x = 'ANNUAL', y= 'JAN', hue = 'STATE_UT_NAME', data = df_guj)
plt.title('Rainfall in inch in Gujarat')
plt.savefig('img4.png', format='png')

#List of District in Gujarat img-5
plt.figure(figsize=(20,5))
sns.lineplot(x = 'ANNUAL', y= 'JAN', hue = 'DISTRICT', data = df_guj)
plt.title('District in Gujarat')
plt.savefig('img5.png', format='png')

#For Gujarat Monthly Rainfall data in inch img-6
plt.figure(figsize=(10,5))
df_guj.groupby(['ANNUAL']).sum().plot.line(figsize=(15,5))
plt.title('Monthly Rainfall Data in inch in Gujarat')
plt.savefig('img6.png', format='png')

#District Wise Monthly Rainfall Data img-7
plt.figure(figsize=(20,5))
df_guj.groupby(['DISTRICT']).sum().plot.line(figsize=(15,5))
plt.title('District Wise Monthly Rainfall Data')
plt.savefig('img7.png', format='png')

#Yearly Rainfall Data of India img-8
plt.figure(figsize=(10,5))
df.groupby(['DISTRICT'])['ANNUAL'].sum().sort_values(ascending=False).head(12).plot(kind='bar', color = 'c')
plt.ylabel('Yearly Rainfall')
plt.title('Yearly Rainfall Data of India')
plt.savefig('img8.png', format='png')

#yearly Rainfall Data of Gujarat img-9
plt.figure(figsize=(10,5))
df_guj.groupby(['DISTRICT'])['ANNUAL'].sum().sort_values(ascending=False).head(12).plot(kind='bar', color = 'c')
plt.ylabel('Yearly Rainfall')
plt.title('Yearly Rainfall Data of Gujarat')
plt.savefig('img9.png', format='png')

#Average Monthly Rainfall in india img-10
plt.figure(figsize=(10,5))
df[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG','SEP', 'OCT', 'NOV', 'DEC']].mean().plot(kind= 'bar')
plt.xlabel('Months')
plt.ylabel('Avg. Rainfall')
plt.title('Avg. Monthly Rainfall Data of India')
plt.savefig('img10.png', format='png')

#Average Monthly Rainfall in Gujarat  img-11
plt.figure(figsize=(10,5))
df_guj[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG','SEP', 'OCT', 'NOV', 'DEC']].mean().plot(kind= 'bar')
plt.xlabel('Months')
plt.ylabel('Avg. Rainfall') 
plt.title('Avg. Monthly Rainfall Data of Gujarat')
plt.savefig('img11.png', format='png')
subprocess.call("show.py", shell=True)