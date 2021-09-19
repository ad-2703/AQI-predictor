import csv
import math
import random
import numpy as np
def calc_err(w1, w2,  b, pm, dates, y_all):
    total = 0
    for i in range (len(pm)):
        y_hat = (w1*pm[i])+ (w2*dates[i]) + b
        squared_err = (y_all[i]-y_hat)**2
        total+=squared_err
    return total/len(pm)

def calc_err_one(w1, w2, b, pm_10, aqi, dates):
    y_hat = (w1*pm_10)+ (w2*dates) + b
    return (aqi-y_hat)**2


learning_rate = 0.6

def get_date(x):
    x = x.split("/")
    return float(x[0])+ (10*float(x[1])) + (10*float(x[2]))


def minimize_err(w1, w2, b, pm_10, aqi, dates):
    # stochastic gradient descent

    i = random.randint(0, len(aqi)-1)
    err = calc_err_one(w1, w2, b, pm_10[i], aqi[i], dates[i])
    w1_new =w1- 2*err*pm_10[i]

    w2_new =w2- 2*err*dates[i]

    b_new = b-2*err*1
    return w1_new, w2_new, b_new




if __name__=="__main__":
    print("hi")
    f = open("ad_viz_plotval_data.csv")
    data = []

    data_read = f.readlines()[1:]
    for elem in data_read:
        data.append(elem.split(","))
    print(data[0])

    w1 = 0
    w2=0
    b = 0

    pm_10 = [float(data_line[4][1:-1]) for data_line in data]
    aqi = [float(data_line[6][1:-1]) for data_line in data]
    dates = [get_date(data_line[0][1:-1]) for data_line in data]

    while(True):
        w1_bar, w2_bar , b = minimize_err(w1, w2,b, pm_10, aqi, dates)
        
        if (w1_bar - w1)**2 + (w2_bar-w2)**2 < math.exp(-3):
            break
        w1, w2=w1_bar, w2_bar

    print(w1, w2)








    
