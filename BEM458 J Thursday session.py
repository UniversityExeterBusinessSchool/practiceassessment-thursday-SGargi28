#######################################################################################################################################################
# 
# Name: Gargi Sarkar
# SID: 740093121
# Exam Date: 27/03/2025
# Module: BEMM458
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-SGargi28.git
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues. we appreciate the effort made to resolve them promptly."""

'''
# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}
'''

# Write your search code here and provide comments. 

#Initialize an empty list called my_list to store (start, end) positions of the words mentioned above
my_list = []

# serach function to find the words, first part of the line of code finds the occurance of the word and the seconf part finds the last occurance as we are calculating and adding the length of the word
my_list = [
    (customer_feedback.find('satisfactory'), customer_feedback.find('satisfactory') + len('satisfactory')),
    (customer_feedback.find('order'), customer_feedback.find('order') + len('order')),
    (customer_feedback.find('effort'), customer_feedback.find('effort') + len('effort')),
    (customer_feedback.find('issues'), customer_feedback.find('issues') + len('issues')),
    (customer_feedback.find('promptly'), customer_feedback.find('promptly') + len('promptly')),
    (customer_feedback.find('appreciate'), customer_feedback.find('appreciate') + len('appreciate')),
    (customer_feedback.find('experience'), customer_feedback.find('experience') + len('experience')),
    (customer_feedback.find('resolve'), customer_feedback.find('resolve') + len('resolve')),
    (customer_feedback.find('overall'), customer_feedback.find('overall') + len('overall')),
    (customer_feedback.find('minor'), customer_feedback.find('minor') + len('minor'))
]

print("Positions of keywords:", my_list)
# Answwer : Positions of keywords: [(38, 50), (12, 17), (114, 120), (88, 94), (142, 150), (99, 109), (18, 28), (129, 136), (51, 58), (82, 87)]

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 74
# Insert last two digits of ID number here: 21

# Write your code for Operating Profit Margin

#Formula to calculate Operating Profit Margin = (Operating Profit / Revenue) × 100
#Initialising a function to calculate Operating Profit Margin based on the above formula. As we need two variables to calculate it, so I'm passing those two variables as arguments with the funtion and writing the formula within the block

def op_margin(op,rev):
    opm = ((op/rev)*100)
    return opm #return the calculated value
   
#calling the function to calculate customer churn rate
result1 = op_margin(21,74)
print("Operating Profit Margin",result1)

#result : Operating Profit Margin 28.37837837837838

# Write your code for Revenue per Customer

#Formula to calculate Revenue per Customer = Total Revenue / Total Number of Customers
#Initialising a function to calculate Revenue per Customer based on the above formula. As we need two variables to calculate it, so I'm passing those two variables as arguments with the funtion and writing the formula within the block

def rev_cust(trev,cust):
    revnue = (trev/cust)
    return revnue #return the calculated value
   
#calling the function to calculate customer churn rate
result2 = rev_cust(74,21)
print("Rev",result2)
#Rev 3.5238095238095237

# Write your code for Customer Churn Rate

#Formula to calculate Customer Churn Rate = (Customers Lost During the Period / Total Customers at the Start of the Period) × 100
#Initialising a function to calculate customer churn rate based on the above formula. As we need two variables to calculate it, so I'm passing those two variables as arguments with the funtion and writing the formula within the block

def cc_rate(customerlost,totalcust):
    cac = ((customerlost/totalcust)*100)
    return cac #return the calculated value
    
#calling the function to calculate customer churn rate
result3 = cc_rate(21,74)
print("Customer Churn Rate",result3)
#customer Churn Rate 28.37837837837838

# Write your code for Average Order Value

# Call your designed functions here

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
prices = np.array([20,25,30,35,40,45,50,55,60,65,70]).reshape(-1, 1)
demand = np.array([33,280,260,240,210,190,160,140,120,100,85])

model = LinearRegression()
model.fit(prices, demand)

predicted_demand = model.predict(np.array([[52]]))
print(f"Predicted demand at price £26: {predicted_demand[0]}")

# Plotting the data points and regression line
plt.scatter(prices, demand, color='blue')
plt.plot(prices, model.predict(prices), color='red')
plt.xlabel("Price (£)")
plt.ylabel("Demand (Units)")
plt.title("Price vs Demand")
plt.show()

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
#max-value = integer(input("Enter your Student ID: "))
#random_numbers = [random.randint(1, max_value) for i in range(0,100)]
'''
# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()
'''

