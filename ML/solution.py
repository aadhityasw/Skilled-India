import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

x = pd.read_csv('/Users/aravind/Documents/dbms_project.csv')
x = x.replace(np.nan, 100)
feature_columns = []

z = x['Sector'].drop_duplicates()
for i, j in enumerate(z):
    x['Sector'] = x['Sector'].replace(j, i)

z = x['place of project'].drop_duplicates()
for i, j in enumerate(z):
    x['place of project'] = x['place of project'].replace(j,i)

feature_df = x[['Sector', 'Budget', 'Skilled workers', 'Unskilled workers', 'Salary for skilled workers',
                'Salary for unskilled workers']]
target = x['Time required']

clf = RandomForestRegressor()
clf.fit(feature_df, target)

#print("The weights for Sector, Budget, Skilled workers, Unskilled workers, Salary for skilled workers and Salary for unskilled workers is:")
#print(clf.feature_importances_)

print("NOT FOUND IN DATABASE. COULDN'T RETRIEVE THE NECESSARY INFORMATION")
Y = input("Do you want to know the estimated years for a specific project")
if Y:
    test_sector = input("Enter 0 for rural areas and 1 for urban areas")
    test_budget = input("Enter budget amount(in Crores)")
    test_skilled_workers_count = input("Enter number of skilled workers that are needed")
    test_unskilled_workers_count = input("Enter number of unskilled workers that are needed")
    test_skilled_salary = input("Enter salary of skilled worker(in rupees/month):") 
    test_unskilled_salary = input("Enter salary of unskilled worker(in rupees/month):")

    Feature = [test_sector, test_budget, test_skilled_workers_count, test_unskilled_workers_count, test_skilled_salary, test_unskilled_salary]
    print("Time required(in years)", clf.predict([Feature]))
else:
    print("Thanks for visiting our site! Have a nice day!!")