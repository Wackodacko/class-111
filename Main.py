import plotly.figure_factory as ff
import statistics
import pandas as pd
import csv
import random 

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
poupulation_mean=statistics.mean(data) 
std_deviation=statistics.stdev(data)

#code to find mean and standerd deviation 100 points
print("poupulation mean",poupulation_mean)
print("std deviation",std_deviation)

#function to plot the mean on teh graph

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

#to get the mean of the givin data samples

def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,100):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    #print("sample mean", mean)
    #print("sample standored deviation",std_deviation)
    return mean

#to plot mean on graph

def show_fig(mean_list):
    df = mean_list
    mean=statistics.mean(mean_list)
    print("sample mean", mean)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

#Funtion to get mean of 100 data point 1000 times

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print("mean of something distribution", mean)

setup()
#function to find the standared deviation of the sample data
def std_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_dev=statistics.stdev(mean_list)
    print("stdev of sampling distribution",std_dev)
std_deviation()


