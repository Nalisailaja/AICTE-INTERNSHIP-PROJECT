#!/usr/bin/env python
# coding: utf-8

# In[212]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# In[147]:


#reading the data set
shop=pd.read_csv(r"C:\Users\HP\Downloads\shopping_trends_updated.csv")
shop.shape


# In[149]:


shop.to_excel('shopping_trends_updated.xlsx')
shop.head()


# In[32]:


#to find the data types in the data
shop.dtypes


# In[36]:


#to find the data types in the data

shop.columns


# In[43]:


#to find the information about the data
shop.info()


# In[45]:


shop.isnull().sum()


# In[11]:


shop.describe()


# In[47]:


print(f"The unique values of the 'Gender' column are:{shop['Gender'].unique()}")
print()


# In[13]:


shop.describe(include="object")


# In[49]:


print(f"The unique values of the 'Category' column are:{shop['Category'].unique()}")
print()


# In[51]:


print(f"The unique values of the 'Size' column are:{shop['Size'].unique()}")
print()


# In[53]:


print(f"The unique values of the 'Subscription Status' column are:{shop['Subscription Status'].unique()}")
print()


# In[55]:


print(f"The unique values of the 'Shipping Type' column are:{shop['Shipping Type'].unique()}")
print()


# In[57]:


print(f"The unique values of the 'Discount Applied' column are:{shop['Discount Applied'].unique()}")
print()


# In[59]:


print(f"The unique values of the 'Promo Code Used' column are:{shop['Promo Code Used'].unique()}")
print()


# In[61]:


print(f"The unique values of the 'Payment Method' column are:{shop['Payment Method'].unique()}")
print()


# In[ ]:





# # OBSERVATION:
# 
# Upon initial examination of the dataset, it is evident that we have a comprehensive and well-structured dataset with 3900 rows and 18 columns. 
# The data is complete, with no missing values, which allows us to proceed confidently with our analysis.
# 
# Let's delve into the columns and their significance in understanding our customers
# 
# Customer ID: This column serves as a unique identifier for each customer, enabling us to differentiate between individuals.
# 
# Age: The age column provides insights into the age demographics of our customers, helping us understand their preferences and behaviors.
# 
# Gender: This column showcases the gender of the customers, enabling us to analyze buying patterns based on gender.
# 
# Item Purchased: Here, we can identify the specific products that customers have bought, allowing us to gain an understanding of popular choices.
# 
# Category: The category column categorizes the products into different groups such as clothing, footwear, and more, aiding us in analyzing trends within specific product categories.
# 
# Purchase Amount (USD): This column reveals the amount customers spent on their purchases, providing insights into their spending habits.
# 
# Location: The location column indicates the geographical location of customers, which can help identify regional trends and preferences.
# 
# Size: This column denotes the size of the purchased products, assisting in understanding size preferences across different categories.
# 
# Color: Here, we can determine the color preferences of customers, aiding in analyzing color trends and their impact on purchasing decisions.
# 
# Season: The season column allows us to identify the season during which customers made their purchases, enabling us to explore seasonal shopping trends.
# 
# Review Rating: This column showcases the ratings given by customers, providing valuable feedback on product satisfaction and quality.
# 
# Subscription Status: This column indicates whether customers have opted for a subscription status, which can help us understand customer loyalty and engagement.
# 
# Shipping Type: Here, we can identify the different shipping methods used to deliver products to customers, shedding light on preferred shipping options.
# 
# Discount Applied: This column indicates whether a discount was applied to the purchased products, enabling us to analyze the impact of discounts on customer behavior.
# 
# Promo Code Used: Here, we can identify whether customers utilized promo codes during their purchases, helping us evaluate the effectiveness of promotional campaigns.
# 
# Previous Purchases: This column reveals the number of previous purchases made by customers, aiding in understanding customer loyalty and repeat business.
# 
# Payment Method: The payment method column showcases the various methods used by customers to make their purchases, allowing us to analyze preferred payment options.
# 
# Frequency of Purchases: This column provides insights into the frequency at which customers make purchases, helping us identify patterns and customer buying habits.
# 
# Customer buying habits. With this rich and diverse dataset, we are well-equipped to explore customer shopping trends, understand their preferences, and uncover valuable insights that can drive informed decision-making and enhance the overall customer experience. Let's embark on this exciting analysis journey!

# In[ ]:





# # 1.What is the overall distribution of customer ages in the dataset?

# In[65]:


shop['Age'].value_counts()


# In[67]:


shop['Age'].mean()


# In[151]:


shop['Age_Category']=pd.cut(shop['Age'],bins=[0, 15, 18, 30, 50, 70], labels=['child','teen', 'young Adults','Middle-Aged Adults','old'])


# In[153]:


fig = px.histogram(shop, y='Age' , x='Age_Category')
fig.show()


# '''Fig 1.Represents how different age groups (categories) are distributed based on age data.'''

# # 2. How does the average purchase amount vary across different product categories?

# In[91]:


shop.columns


# In[155]:


shop['Category'].unique()


# In[157]:


shop.groupby('Category')['Purchase Amount (USD)'].mean()


# # 3.Which gender has the highest number of purchases?

# In[159]:


sns.barplot(shop,x='Gender',y='Purchase Amount (USD)')


# ''' Fig2:Represents the highest no.of purchases based on gender'''

# # 4. What are the most commonly purchased items in each category?

# In[161]:


shop.groupby('Category')['Item Purchased'].value_counts()


# In[165]:


fig=px.histogram(shop,x='Item Purchased',color='Category')
fig.show()


# Fig3.Represents the distribution of items purchased, categorized by different groups.

# In[ ]:





# # 5. Are there any specific seasons or months where customer spending is significantly higher?

# In[115]:


shop['Season'].unique()


# In[21]:


shop['Season'].value_counts()


# In[23]:


fig=px.histogram(shop,x='Season' ,range_y=[800,1200])
fig.show()


# Fig4.Represents possibly sales are distributed across different seasons

# In[ ]:





# # 6.What is the average rating given by customers for each product category?

# In[27]:


shop.groupby('Category')['Review Rating'].mean()


# In[43]:


shop_groupby = shop.groupby('Category')['Review Rating'].mean().reset_index()
print(shop_groupby)


# In[48]:


fig = px.bar(shop_groupby ,x= 'Category' , y = 'Review Rating' )
fig.show()


# Fig5 Represents average rating given by customers for each product category

# In[ ]:





# # 7 Are there any notable differences in purchase behavior between subscribed and non-subscribed customers?

# In[61]:


shop.columns


# In[63]:


shop['Subscription Status'].value_counts()


# In[71]:


sns.barplot(shop  , x = 'Subscription Status' , y = 'Purchase Amount (USD)')


# Fig6:Represents how purchase amounts (in USD) vary based on different subscription statuses

# In[75]:


shop.groupby('Subscription Status')['Purchase Amount (USD)'].mean()


# In[ ]:





# # 8 Which payment method is the most popular among customers?

# In[80]:


shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().sort_values(ascending= True)


# In[82]:


sns.barplot(shop ,x='Payment Method' , y = 'Purchase Amount (USD)')
plt.show()


# Fig7 Represents Most Popular Payment Method among Customers

# In[ ]:





# # 9 Do customers who use promo codes tend to spend more than those who don't?

# In[95]:


shop_groupby=shop.groupby('Promo Code Used')['Purchase Amount (USD)'].sum().reset_index()


# In[93]:


fig = px.sunburst(shop , path=['Gender' , 'Promo Code Used'] , values='Purchase Amount (USD)')
fig.show()


# In[ ]:





# In[97]:


fig  =  px.bar(shop_groupby , x= 'Promo Code Used' , y = 'Purchase Amount (USD)')
fig.show()


# Fig8:Represents who use promo codes tend to spend more than those who don't.

# In[ ]:





# # 10 How does the frequency of purchases vary across different age groups?

# In[45]:


shop['Age_Category'].unique()


# In[47]:


shop_group = shop.groupby('Frequency of Purchases')['Age'].sum()


# In[49]:


px.sunburst(shop , path=['Frequency of Purchases','Age_Category'] , values='Age')


# # 11 Are there any correlations between the size of the product and the purchase amount?

# In[58]:


shop_group = shop.groupby('Size')['Purchase Amount (USD)'].sum().reset_index()


# In[60]:


fig  = px.bar(shop_group , x = 'Size' , y ='Purchase Amount (USD)'  )
fig.show()


# Fig9:Represents correlations between the size of the product and the purchase amount

# 

# # 12 Which shipping type is preferred by customers for different product categories?

# In[65]:


shop.groupby('Category')['Shipping Type'].value_counts().sort_values(ascending= False)


# In[ ]:





# # 13 How does the presence of a discount affect the purchase decision of customers?

# In[70]:


shop_group = shop.groupby('Discount Applied')['Purchase Amount (USD)'].sum().reset_index()


# In[72]:


px.histogram(shop_group , x = 'Discount Applied' , y = 'Purchase Amount (USD)')


# Fig10:Represents the presence of a discount affect the purchase decision of customers?

# In[ ]:





# # 14 Are there any specific colors that are more popular among customers?

# In[76]:


shop['Color'].value_counts().nlargest(5)


# In[78]:


px.histogram(shop , x = 'Color')


# Fig11:Represents specific colors that are more popular among customers
# 

# In[ ]:





# # 15 What is the average number of previous purchases made by customers?

# In[83]:


shop['Previous Purchases'].mean()


# # 16 Are there any noticeable differences in purchase behavior between different locations?

# In[90]:


shop.groupby('Location')['Purchase Amount (USD)'].mean().sort_values(ascending = True)


# In[96]:


fig = px.bar(shop, x = 'Location' , y = 'Purchase Amount (USD)')
fig.show()


# Fig12:Represents there any noticeable differences in purchase behavior between different locations

# # 17 Is there a relationship between customer age and the category of products they purchase?

# In[175]:


shop_group = shop.groupby('Category')['Age'].mean().reset_index()


# In[177]:


fig = px.bar(shop_group ,y = 'Age' , x= 'Category')
fig.show()


# Fig13:Represents a relationship between customer age and the category of products they purchase

# In[ ]:





# # 18 How does the average purchase amount differ between male and female customers?

# In[189]:


shop_group = shop.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index()


# In[199]:


fig = px.bar(shop_group ,y = 'Purchase Amount (USD)' , x= 'Gender')
fig.show()


# Fig14:Represents the average purchase amount differ between male and female customers

# In[ ]:





# In[ ]:





# In[ ]:




