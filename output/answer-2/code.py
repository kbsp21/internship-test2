import pandas
import numpy

dataframe = pandas.read_csv(r"input\question-2\main.csv")
print(dataframe.head)
final = dataframe.groupby(['occupation']).agg({'age':[min,max]})
final.to_csv(r"output\question-2\main.csv")