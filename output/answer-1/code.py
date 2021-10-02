import pandas
import numpy

dataframe = pandas.read_csv(r"C:\Users\pavan\Desktop\BUNGEE TECH\internship-test2-master\input\question-1\main.csv")
print(dataframe)
dataframe.set_index('Year')
dataframe['Year'] = dataframe['Year']//10
dataframe['decade'] = dataframe['Year']*10

final = dataframe.groupby(['decade']).agg({'Population' :'last' , 'Total':sum, 'Violent':sum , 'Property':sum, 'Murder':sum, 'Forcible_Rape':sum, 'Robbery':sum, 'Aggravated_assault':sum, 'Burglary':sum,'Larceny_Theft':sum,'Vehicle_Theft':sum})
final.to_csv(r"output\question-1\main.csv")