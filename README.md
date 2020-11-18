# analysis-of-911calls
For this capstone project we will be analyzing some 911 call data from Kaggle. The data contains the following fields:
•	lat : String variable, Latitude
•	lng: String variable, Longitude
•	desc: String variable, Description of the Emergency Call
•	zip: String variable, Zipcode
•	title: String variable, Title
•	timeStamp: String variable, YYYY-MM-DD HH:MM:SS
•	twp: String variable, Township
•	addr: String variable, Address
•	e: String variable, Dummy variable (always 1)

1.	After reading the data, clean and manipulate it. 
2.	Once your data is ready, answer the following questions:
a.	What are the top 5 zipcodes for 911 calls?
b.	What are the top 5 townships (twp) for 911 calls?
c.	Take a look at the 'title' column, how many unique title codes are there?
d.	In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value
e.	What is the most common Reason for a 911 call based off of this new column
3.	Visualisation:
a.	Now use seaborn to create a countplot of 911 calls by Reason
b.	Use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.
i.	This part would require you to do some data cleaning in time and date columns. 
ii.	Figure out first what to be done and then use apt method to do it
c.	Redo b. for month
d.	Compare the result from b and c
e.	Create a simple plot off of the dataframe indicating the count of calls per month. 
f.	Use seaborn's lmplot() to create a linear fit on the number of calls per month. 
g.	Create a new column called 'Date' that contains the date from the timeStamp column. 
h.	Groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.
i.	Recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call
j.	Heatmaps – Try to explore all the possibilities of different heatmap and create those. Once you create heatmaps, you should analyse the output. 
