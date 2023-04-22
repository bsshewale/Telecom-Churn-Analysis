# -*- coding: utf-8 -*-
"""Copy of Sample EDA Submission Template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12MCiZVrK1XSMF4P5xEl-PPq65Xm2dpEE

# **Project Name**    -

##### **Project Type**    - EDA
##### **Contribution**    - Individual
##### **Team Member** - Bharat Shewale

# **Project Summary -**

*   Every telecom company want to be on a height, so that everyone like it and suscribe it, but it is only possible when company solve each and every problem faced by customer


*   Customer only trust on company service if company solve the problem without any delay.


* Therefore to improve the quality of service company has to look for certain area with problem and analysis of which is the main moto behind this project

# **GitHub Link -**

https://github.com/bsshewale/Telecom-business-analysis

# **Problem Statement**

* Every customer want a service which fullfil their needs, if the telecom company solve their problem, then customer will retain the service.
  * To analyse the dataset to find the reasons for the churn

#### **Define Your Business Objective?**

* **To improve telecom business by churn analysis**

# ***Let's Begin !***

## ***1. Know Your Data***

### Import Libraries
"""

# Import Libraries
import numpy
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

"""### Dataset Loading"""

# Load Dataset
from google.colab import drive
drive.mount('/content/drive',force_remount=True)

df=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Assignments/Module 1/Telecom Churn.csv')

"""### Dataset First View"""

# Dataset First Look
# head of data
df.head()

# Dataset tail
df.tail()

"""### Dataset Rows & Columns count"""

# Dataset Rows & Columns count
f'Shape of Dataset is:{df.shape}'

"""### Dataset Information"""

# Dataset Info
df.info()

"""#### Duplicate Values"""

# Dataset Duplicate Value Count
f'Dataset have {df.duplicated().sum()} duplicate value'

"""#### Missing Values/Null Values"""

# Missing Values/Null Values Count
df.isna().sum()

"""* ***Insights:Dataset doesn't have any null or missing value***"""

# Visualizing the missing values
import missingno as msno
msno.bar(df)

"""### What did you know about your dataset?

*   The dataset contains 3333 rows and 20 columns
*   The dataset does not have any missing value

## ***2. Understanding Your Variables***
"""

# Dataset Columns
df.columns

# Dataset Describe
df.describe()

"""### Variables Description

**Variables are:** 

* **State** = 51 unique states
* **Account length** = 212 unique length
* **Area code**= 3 unique code
* **International plan**= shows yes, no type of data
* **Voice mail plan**= shows yes, no type of data
* **Number vmail messages**= total messages
* **Total day minutes**= total minutes per day
* **Total day calls**= total calls per day
* **Total day charge**= total charge per day
* **Total eve minutes**= total minutes per evening
* **Total eve calls**= total calls per evening
* **Total eve charge**= total charge per evening
* **Total night minutes**= total minutes per night
* **Total night calls**= total calls per night
* **Total night charge**= total charge per night
* **Total intl minutes**= total international minutes
* **Total intl calls**= total international calls
* **Total intl charge**= total international charge
* **Customer service calls**= total calls to service centre
* **Churn**= return true if churn and false if not churn

### Check Unique Values for each variable.
"""

# Check Unique Values for each variable.
lst=list(df.columns)
for var in lst:
  print(f'The unique variables for {str(var)}, are : {len(df[var].unique())}')

"""## 3. ***Data Wrangling***

* Question:


1.   Which states are more likely under churn rate?
2.   How much is the price rate per minutes?
3.   Is there any relation of the price rate with churn rate
4.   Is there any reduction in the customer due to poor service

### Data Wrangling Code
"""

from pickle import TRUE
# Write your code to make your dataset analysis ready.
# Total number of customers churn
print(f'Length of churned customer is { len(df[df.Churn==True])}')

# Total current customer
print(f'Length of retain customer is {len(df[df.Churn==False])}')

"""### **Analysis of churn customers**


---




"""

# To find the customer churn
df_churn=df[df['Churn']==True]
df_churn

"""* ***DataFrame showing states with churning customers, the shape is 483 row and 20 columns.***"""

# Making a column that represent total talktime in day
df_churn['Day talktime']=df_churn['Total day calls']*df_churn['Total day minutes']

# Making a column that represent total talktime in evening
df_churn['Evening talktime']=df_churn['Total eve calls']*df_churn['Total eve minutes']

# Making a column that represent total talktime in night
df_churn['Night talktime']=df_churn['Total night calls']*df_churn['Total night minutes']

df_churn.describe()

# State with talktime less than 25% of total talktime
print(list(df_churn[df_churn['Day talktime']<14163.250000].State))

# State with talktime less than 25% of total talktime
print(list(df_churn[df_churn['Evening talktime']<14163.250000].State))

# State with talktime less than 25% of total talktime
print(list(df_churn[df_churn['Night talktime']<14163.250000].State))

"""* ***Above are the list of state which have day talktime less than 25% of the total talktime***"""

# Sorting 'Account length' column to get 'State' with higher 'account length'
dfc_h_len=df_churn.sort_values('Account length').tail(10)
dfc_h_len

"""* ***As data subset shows the state with highest acount length.***"""

# Grouping the data by state with international plan for churned customers
dfc_intl_plan=df_churn.groupby('State')['International plan'].value_counts().reset_index(name='Intl_plan_count')
dfc_intl_plan

# International plan active customer states 
dfc_intl_plan[dfc_intl_plan['International plan']=='Yes']

# International plan not active customer statewise
dfc_intl_plan[dfc_intl_plan['International plan']=='No']

"""* ***This are the state having customers with no international plan active, so this can be made separate plan for those who want to subscribe***"""

# Voice mail plan active states
df_churn[df_churn['Voice mail plan']=='No']

# zero vmail messages by the customers
df_churn[df_churn['Number vmail messages']==0]

"""* ***Above Dataframe shows that from the churned customers 483, majority of customers i.e. 403 did't had any vmail messages, and this might be the reason to make plan costier, and it can be separated from the current plan.*** 

"""

# Customer having vmail messages above 0 are
df_churn[df_churn['Number vmail messages']>0]

"""* ***As we can see from the data above 80 customers have vmail messages above zero.***"""

# To get Total intl calls statewise
df_churn.groupby('State')['Total intl calls'].value_counts().reset_index(name='Count')

"""* ***This can provide hint which state make international calls, From the analysis it is found that every customer use to make atleast 1 international call, It can be included in the plan.***"""

# Getting the state from which the customer made most service calls
print(list(df_churn[df_churn['Customer service calls']>5].State))

"""* ***Above state are more likely call for service so there may be problem for which they are asking for service.***"""

# Customer churn rate statewise
dfc=pd.DataFrame(df_churn.groupby('State')['Churn'].value_counts().reset_index(name="Count"))

# Sorting the value count to higher churn rate state
pd.DataFrame(df_churn.groupby('State')['Churn'].value_counts().reset_index(name="Count").sort_values('Count',ascending=False)).head(10)

"""* ***From the above dataframe we get the state which are under most churn state category.***"""

# Churn rate area code wise
dfc1=pd.DataFrame(df_churn.groupby('Area code')['Churn'].value_counts().reset_index(name='Count'))
dfc1

"""* ***As we can see Area code 415 is the most danger zone for which company should look first and followed by 510 and 408.***

### **Analysis of Retain customers**
"""

# To find retain customers
dfr=df[df['Churn']==False]
dfr

"""***Insights: The shape of retain customer dataset is (2850,20).***"""

# Description of retain customers
dfr_describe=pd.DataFrame(dfr.describe())

# Customer retain group by state
dfr1=dfr.groupby('State')['Churn'].value_counts().reset_index(name='Count')
dfr1

# Retain customers groupby area code
dfr.groupby('Area code')['Churn'].value_counts().reset_index(name='Count')

"""* ***This will help to focus on retain customers solve their problems to improve business***

### **Overall analysis for whole dataset**
"""

# Checking price rate
df1=df
# Price per minutes in the day 
df1['Price/min in day']=df['Total day charge']/df['Total day minutes']

# Price per minutes in the evening
df1['Price/min in evening']=df['Total eve charge']/df['Total eve minutes']

# Price per minutes in the night
df1['Price/min in night']=df['Total night charge']/df['Total night minutes']

# Price per minutes for international calls
df1['Price/min for intl']=df['Total intl charge']/df['Total intl minutes']
df1

# Average Price per minutes in the day 
df['Price/min in day'].mean()

# Average Price per minutes in the evening
df['Price/min in evening'].mean()

# Average Price per minutes in the night
df['Price/min in night'].mean()

# Average Price per minutes for international calls
df['Price/min for intl'].mean()

# Statewise Total international calls
df_intl_calls=pd.DataFrame(df.groupby('State')['Total intl calls'].value_counts().reset_index(name='Count'))
df_intl_calls

"""### What all manipulations have you done and insights you found?

1. Comparing state with churn rate, we can get which states have highest churn rate we can then check problems in that area like network problem etc. and try to solve them.


2. Calculating prices per minutes it is found that overall price is same throught all the state that is nearly *0.1700032343415996* in *daytime*, *0.08500117298813872* in *evening* and *0.045000345702212126* in the night, and for *international call* is *0.27005654558216224*, so it might not be the reason behind the churn rate.


3. As we can see Area code 415 is the most danger zone for which company should look first and followed by 510 and 408.


4. From the analysis it is found that every customer use to make atleast 1 international call, It can be included in the plan.


5. Above Dataframe shows that from the churned customers 483, majority of customers i.e. 403 did't had any vmail messages, and this might be the reason to make plan costier, and it can be separated from the current plan.

## ***4. Data Vizualization, Storytelling & Experimenting with charts : Understand the relationships between variables***

## ***OVERALL ANALYSIS***

---

#### **Chart - 1** 
### **Customers across the State (Univariate analysis)**
"""

# Chart - 1 visualization code
# Total customers across the State
# Setting figuresize
plt.figure(figsize=(15,5))

# Plotting countplot
sns.countplot(x='State',data=df)

# Setting title 
plt.title('Count of Customers by states')

"""##### 1. Why did you pick the specific chart?

* To get count of customers across the states

##### 2. What is/are the insight(s) found from the chart?

*   State WV has highest customers,followed by NY, MN, and AL
*   State CA has lowest customers, followed by PA, IA, and LA

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

*   As the state CA, PA, IA and LA has the lowest customers the company look into these area for problems like network issues etc to solve, so that the customers will be increase by the time.

#### **Chart - 2**
### **Overall percentage of churn (Univariate)**
"""

# Chart - 2 visualization code
# To get percentage of Churn 
# Setting figuresize
plt.figure(figsize=(10,5))

# Plotting pie chart
plt.pie(df['Churn'].value_counts(),
        labels=['No','Yes'],
        autopct='%1.1f%%')

# Setting title
plt.title('Overall churn rate')

"""##### 1. Why did you pick the specific chart?

* To visualize churn and retain customer in term of percentage.

##### 2. What is/are the insight(s) found from the chart?

* There are about 14.5% churn occur all over region, with retainer percentage 85.5%.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* From the chart company will get idea of churned customers so that company has to make certain changes to avoid the churning of customers

## ***ANALYSIS OF CHURNED CUSTOMERS***

#### **Chart - 3(Churned Analysis)**
### **Frequency of State with account length**
"""

# Plotting Histogram
df_churn['Account length'].plot(
              figsize=(10,5),
              title='State Frequency of Account length ', 
              kind='hist')

"""#### **Chart - 4(Churned Analysis)**
### **Day talk time vs State(Bivariate - Numerical to categorical)**

"""

# Chart - 3 visualization code
# State vs day talktime boxplot
# Setting figersize
sns.set(rc={'figure.figsize':(17,5)})

# Plotting violin chart
sns.violinplot(x='State',
               y='Day talktime',
               data=df_churn,
               color='r')

# Setting title
plt.title('Violinplot between State and Day talk time')

"""#### **Chart - 5(Churned Analysis)**
### **Evening talk time vs State(Bivariate)**
"""

# State vs evening talktime boxplot
# Setting figuresize
sns.set(rc={'figure.figsize':(17,5)})

# Plotting violin plot
sns.violinplot(x='State',
               y='Evening talktime',
               data=df_churn,
               color='b')

# Setting Title 
plt.title('Violinplot between State and Evening talk time')

"""#### **Chart - 6(Churned Analysis)**
### **Night talk time vs State(Bivariate)**
"""

# State vs evening talktime boxplot
# Setting figuresize
sns.set(rc={'figure.figsize':(17,5)})

# Making violinplot
sns.violinplot(x='State',
               y='Night talktime',
               data=df_churn,
               color='g')

# Setting Title
plt.title('Violinplot between State and Night talk time')

"""##### 1. Why did you pick the specific chart?

* To get idea of call time of customers in the daytime, evening and night time.

##### 2. What is/are the insight(s) found from the chart?

* Customer more active on call in daytime and evening time than night 
* How much time the particular state uses service.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* Company can visualize statewise total talktime combining all customers in a particular state in daytime, night and evening.

#### **Chart - 7(Churned Analysis)**
### **Churn rate by area code(Univariate)**
"""

# Chart - 4 visualization code
# Plot showing Churn rate by area code
# Plotting bar chart
dfc1.plot(x='Area code',
          kind='bar',
          figsize=(5,5))

# Setting title
plt.title('Churn rate by area code')

"""#### **Chart - 8(Churned Analysis)**
### **Churn rate by state(Univariate)**
"""

# Plot showing Churn rate by State 
# Plotting bar chart
dfc.plot(x='State',
         kind='bar', 
         figsize=(12,5))

# Setting title
plt.title('Churn rate by State')

"""##### 1. Why did you pick the specific chart?

* To get churn rate area-code and state wise respectively

##### 2. What is/are the insight(s) found from the chart?

* We get areas under the churn
* We get State under the churn

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* Company can take the area/state for problems to avoid the churning

#### **Chart - 9(Churned Analysis)**
### **Total day calls vs State (Bivariate analysis)**
"""

# Chart - 5 visualization code
# Statewise Total day calls for Churn customers plot
# Plotting Scatterplot
df_churn.plot(kind='scatter',
              x='State',y='Total day calls', 
              figsize=(17,5),
              title=("Total day calls by State"),
              color='r')

"""##### 1. Why did you pick the specific chart?

* To find calls made by churn customers.

##### 2. What is/are the insight(s) found from the chart?

* The range of calls made by the customer in daytime is 50 to 130.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* By the pattern of call made by the customers we can get insight as there may be chances of poor network in the states AZ,LA, AK, RI, MO, NE, IL, IA and HI as they have made very less calls in daytime.

#### **Chart - 10 (Churned Analysis)**
### **Total evening calls vs State(Bivariate- Categorical to numerical)**
"""

# Chart - 6 visualization code
# Statewise Total evening calls made by churn customers plot
df_churn.plot(kind='scatter',
              x='State',y='Total eve calls',
              figsize=(15,5),
              title=("Total evening calls by State"),
              color='b')

"""##### 1. Why did you pick the specific chart?

* To get statewise call made by customer in the evening.

##### 2. What is/are the insight(s) found from the chart?

The range of call made by the customers in evening is between 60 to 140.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* Just like day, in the evening also, By the pattern of call made by the customers we can get insight as there may be chances of poor network in the states AZ,LA, AK, RI, MO, NE, IL, IA and HI as they have made very less calls in daytime.

#### **Chart - 11(Churned Analysis)**
### **Total night calls vs State(Bivariate)**
"""

# Chart - 7 visualization code
# Statewise Total night calls made by churn customers plot
df_churn.plot(kind='scatter',
              x='State',
              y='Total night calls', 
              figsize=(15,5),
              title=("Total night calls by State"),
              color='g')

"""##### 1. Why did you pick the specific chart?

* To get information about call made by the customer in the night

##### 2. What is/are the insight(s) found from the chart?

* In the night range of the calls made by the customers is between 65 to 130.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* Similar as above plots for the day and evening calls night also follows same trend so we can say that there are some state should have some problem.
* The state includes AZ,LA, AK, RI, MO, NE, IL, IA and HI

#### **Chart - 12(Churned Analysis)**
### **Voice mail plan active percentage(Univariate)**
"""

# Chart - 8 visualization code
# Customer with and without voice mail plan
# Plotting pie chart 
plt.pie(df_churn['Voice mail plan'].value_counts(),
        labels=['No','Yes'], 
        autopct='%1.1f%%')

# Setting title
plt.title('Voice mail plan percentage')

"""##### 1. Why did you pick the specific chart?

* To show the percentage of voice mail plan customers

##### 2. What is/are the insight(s) found from the chart?

* There are only 16.6% customers had subscribed the voice mail plan, rest 83.4% handn't.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* May be some customers don't uses voice mail plan, so it should have separate plan because those want to suscribe the same will subscribe and cost of the current plan can be reduced as these voice mail plan separated

#### **Chart - 13(Churned Analysis)**
### **Vmail messages count by state(Univariate)**
"""

# Chart - 9 visualization code
# Number of vmail messages suscriber
# Setting figersize
plt.figure(figsize=(20,10))

# Setting title 
plt.title('Vmail messages count by state',size='15')

# Setting x label
plt.xlabel('State')

# Plotting bar chart
plt.bar(df_churn['State'], 
        df_churn['Number vmail messages'],
        color="red")

"""##### 1. Why did you pick the specific chart?

* To visualize customers with voice mail plan

##### 2. What is/are the insight(s) found from the chart?

As shown in the chart above states like IN, AZ, DC, AK, etc don't have any customer with voice mail plan.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* From the above chart we can draw insight that customers from the state like IN, AZ, DC, AK, etc don't want to buy the same.
* If the company cutout the plan of voicemail then the plan value can be reduced so the customer will get attract again.

#### **Chart - 14(Churned Analysis)**
### **Highest churn rate by state(Bivariate- Categorical to numerical)**
"""

# Chart - 10 visualization code
# Ploting Highest account length with state
dfc_h_len.plot(x='State',
               y='Account length',
               kind= 'bar')

# Setting title for chart
plt.title('State with highest churn rate')

"""##### 1. Why did you pick the specific chart?

* To get state with highest account length

##### 2. What is/are the insight(s) found from the chart?

* This chart show state that have undergone highest churn as the account length of these state is very high.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* Company got the state which are of more impacted with churn

## ***ANALYSIS OF RETAIN CUSTOMER***

#### **Chart - 15(Retain analysis)**
### **Count of customer retain by state(Univariate)**
"""

# Chart - 11 visualization code
# Customers retain across the states
plt.figure(figsize=(18,8))
sns.countplot(x='State',data=dfr)

"""##### 1. Why did you pick the specific chart?

* To visualize the state that has very less customers

##### 2. What is/are the insight(s) found from the chart?

* There are some State whose customer count is very less, company should improve these states telecom quality

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* It will help company to work on less active state by which company can improve the quality lead to growth of the business

* ***

#### **Chart - 16(Retain analysis)**
### **Total international calls by state (Bivariate)**
"""

# Chart - 12 visualization code
# figure size in inches
sns.set(rc={'figure.figsize':(17,5)})
sns.barplot(x='State', y='Total intl calls', data=df)
plt.show()

"""##### 1. Why did you pick the specific chart?

* To visualize the international calls made by the customers

##### 2. What is/are the insight(s) found from the chart?

* We can take note of the customers international calls, so that plan can be modified accordingly

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* Business can be improve if international calls plan will be separated

#### **Chart - 17(Retain analysis)**
### **Customer retain by state(Bivariate)**
"""

# Chart - 13 visualization code
dfr1.plot(x='State',y='Count',kind='bar')

"""##### 1. Why did you pick the specific chart?

* To get retain customer by states, this plot show clear visualization of same.

##### 2. What is/are the insight(s) found from the chart?

* There are state like PA, CA, IA which have less customer.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

* To improve business company should look into low customer state for problem

#### **Chart - 18(Retain analysis)**
### **Customer have ask for service by state(Bivariate)**
"""

# State that have ask for service frequently
print(list(df[df['Customer service calls']>5].State))
df[df['Customer service calls']>5].plot(x='State',
                                        y='Customer service calls',
                                        kind='bar',
                                        title='State with customer have ask more for service')

"""What is/are the insight(s) found from the chart?
* This analysis give state which have call more frequently for service

## **Chart - 19 - Correlation Heatmap**
"""

# Correlation Heatmap visualization code
# Setting figersize
sns.set(rc={'figure.figsize':(20,8)})

# Plotting heatmap
sns.heatmap(df.corr(),
            annot=True,
            linecolor='white',
            linewidths=2,
            annot_kws={"size":8})

"""##### 1. Why did you pick the specific chart?

* To get corelations between variables

##### 2. What is/are the insight(s) found from the chart?

* Every variable show either positive or negative relation 
* Positive relation shows linear relationship between variable
* It mean if a variable gives profit, other postively related one also give profit

### **Chart - 20 - Pair Plot**
"""

# Pair Plot visualization code
sns.pairplot(df_churn, hue="Churn")

"""##### 1. Why did you pick the specific chart?

* It gives overall look of whole dataset by comparing each variable with other of the dataset and give presentation in the form of small chart in a single window

##### 2. What is/are the insight(s) found from the chart?

* By using smaller scatter plot it give trend of variable with other variable in a window

## **5. Solution to Business Objective**

#### What do you suggest the client to achieve Business Objective ?

* Some state are more likely call for service so there may be problem for which they are asking for service.

* MT, NM, ID, AL, TX, SC, DE, and MI are the state which undergone most churned, look into thes state for any problem, why they are churning?

* By the pattern of call made by the customers I get insight as there may be chances of poor network in the states AZ, LA, AK, RI, MO, NE, IL, IA and HI as they have made very less calls in daytime, evening and also in night.

* From the above chart insight drown that some customers from the state like IN, AZ, DC, AK, etc don't want to buy the voicemail plan 

* If the company make the plan of voicemail and international separate then the current plan value can be reduced, so the customer will get attract again.

* There are state like PA, CA, IA which have less customer, there may be chances of problems.

# **Conclusion**

* Some state have ask for service more than 5 times in the churn customer list.
* Some state have very less customer may be due to network problem.
* If the areas identified by the analysis, are supervised for the problem there may be chances of business improvement.

### ***Hurrah! You have successfully completed your EDA Capstone Project !!!***
"""