#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load
file_to_load = "/Users/fernandawolburg/Downloads/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[3]:


list(purchase_data)


# # Player Count

# * Display the total number of players
# 

# In[4]:


# Create a table for total number of players, then display the count of the values
players = set(purchase_data['SN'])
players_table = pd.DataFrame({'Total players': players})

# display value
players_table.count()


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[5]:


# create a variable for amount of unique items
unique_items = purchase_data['Item ID'].nunique()

# variable for average purchase price
average_price = purchase_data['Price'].mean()

# variable for total number of purchases
total_purchases = purchase_data['Price'].count()

# variable for total revenue
total_revenue = purchase_data['Price'].sum()

 # Creating a new DataFrame to display this information
purchasing_analysis_table = pd.DataFrame({"Unique Items": unique_items,
                                      "Average Purchase Price": '${:,.2f}'.format(average_price),
                                      "Total Purchases": total_purchases,
                                      "Total Revenue": '${:,.2f}'.format(total_revenue)},index=['Total'])

# display dataframe
purchasing_analysis_table.round(2)


# # Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[6]:


#create a loc for gender, SN and Age
g_players = purchase_data.loc[:, ['Gender', 'SN', 'Age']]

# drop_duplicates() for this variable
g_players = g_players.drop_duplicates()

# use value_counts to count the amount of each unique value for gender
gender_counts = g_players['Gender'].value_counts()

# create percentage for each gender by dividing over total amount of players
g_percent = (gender_counts/576) * 100

# create dataframe to display coun and gender percentage
gender_table = pd.DataFrame({'Gender Count': gender_counts,
                            'Gender %': g_percent})

# display dataframe
gender_table.round(2)


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[8]:


# create a groupby for gender
gender_purchase = purchase_data.groupby('Gender')

# create variables
g_purchase = gender_purchase['Purchase ID'].count()
g_avg_purchase = gender_purchase['Price'].mean()
g_total_purchase = gender_purchase['Price'].sum()
g_avg_person = g_total_purchase/gender_counts

# create dataframe
gender_summary = pd.DataFrame({'Purchase Count': g_purchase,
                               'Average Purchase': g_avg_purchase,
                              'Total Purchase Amount': g_total_purchase,
                              'Average purchase per person': g_avg_person})

# display dataframe    
gender_summary.round(2)


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[10]:


# create bin for age group and age number
age_group = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-40', '40+']
age_number = [0, 9, 14, 19, 24, 29, 34, 39, 100]

# use pd.cut()
purchase_data["Age Group"] = pd.cut(purchase_data["Age"], age_number, labels= age_group)

# group by age and create table for age group
age_data = purchase_data.groupby('Age Group')

# create age_count and percent_age
age_count = age_data['SN'].nunique()
percent_age = (age_count/576) * 100

# create dataframe
age_data_1 = pd.DataFrame({'Total Count': age_count,
                        'Percentage per group': percent_age})
# display dataframe
age_data_1.round(2)


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[13]:


# create variables
purchase_age = age_data['Purchase ID'].count()
purchase_avg_age = age_data['Price'].mean()
purchase_total = age_data['Price'].sum()
purchase_avg_total = purchase_total/age_count

#create dataframe
age_data_2 = pd.DataFrame({'Purchase Count': purchase_age,
                          'Average Purchase Price': purchase_avg_age,
                          'Total Purchase Value': purchase_total,
                          'Average Total Purchase (per person)': purchase_avg_total})

# Print dataframe
age_data_2.round(2)


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[16]:


# create a groupby for gender
spender_df = purchase_data.groupby('SN')

# create variables
spender_count = spender_df['Purchase ID'].count()
spender_avg = spender_df['Price'].mean()
spender_price = spender_df['Price'].sum()

# create datafram to display purchase count, average purchase price, and total purchase value
spenders_df = pd.DataFrame({'Purchase Count': spender_count,
                           'Average Purchase Price': spender_avg.round(2),
                           'Total Purchase Value': spender_price})

# sort by top spenders
topspenders_df= spenders_df.sort_values(by='Total Purchase Value', ascending=False)

# display dataframe for spenders
topspenders_df.head(5)


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[10]:


# Retrieve the Item ID, Item Name, and Item Price columns
#mostpopulardf = purchase_data[['Item ID', 'Item Name', 'Price']]

# group by item name and item ID
mostpopular_df = purchase_data.groupby(['Item ID', 'Item Name'])

# Perform calculations to obtain purchase count, item price, and total purchase value
pop_purchase = mostpopular_df['Price'].count()
pop_total_purchase = mostpopular_df['Price'].sum()
pop_price = pop_total_purchase / pop_purchase

# create dataframe
mostpopular_df_1 = pd.DataFrame({'Purchase Count': pop_purchase,
                                'Item Price': pop_price,
                                'Total Purchase Value': pop_total_purchase})

# sort in descending order by 'purchase count' column
most_popular_sorted = mostpopular_df_1.sort_values(by='Purchase Count', ascending=False)

# display the dataframe
most_popular_sorted.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[11]:


# Sort the above table by total purchase value in descending order
most_popular_sorted_total = mostpopular_df_1.sort_values(by='Total Purchase Value', ascending=False)

# Display a preview of the data frame
most_popular_sorted_total.head()


# In[ ]:




