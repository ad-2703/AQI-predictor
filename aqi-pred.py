import csv
import math
import random
import numpy as np
from sklearn.linear_model import LinearRegression

def calc_err(w1, w2,  b, pm, dates, y_all):
    total = 0
    for i in range (len(pm)):
        y_hat = (w1*pm[i])+ (w2*dates[i]) + b
        squared_err = (y_all[i]-y_hat)**2
        total+=squared_err
    return total/len(pm)

def calc_err_one(w1, w2, b, pm_10, aqi, dates):
    y_hat = (w1*pm_10)+ (w2*dates) + b
    print(y_hat)
    print(aqi)
    return (aqi-y_hat)**2


learning_rate = 0.6

def get_date(x):
    x = x.split("/")
    return float(x[0])+ (10*float(x[1])) + (float(x[2]))


def minimize_err(w1, w2, b, pm_10, aqi, dates):
    # stochastic gradient descent

    i = random.randint(0, len(aqi)-1)
    err = calc_err_one(w1, w2, b, pm_10[i], aqi[i], dates[i])

    w1_new =w1- 2*err*pm_10[i]*learning_rate

    w2_new =0
    print(w1_new, w2_new)
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

     
    pm_10 = [[float(data_line[4][1:-1]) , float(data_line[-1][1:-3])]for data_line in data]

    aqi = [float(data_line[6][1:-1]) for data_line in data]


    #lati = [float(data_line[-1][1:-1]) for data_line in data]



    reg = LinearRegression().fit(pm_10[0:len(pm_10)//2], aqi[0:len(pm_10)//2])
    print(reg.coef_)

    #calc error

    tot = 0

    for i in range(len(pm_10)//2, len(pm_10)):
        y = reg.predict(np.array([pm_10[i]]))
        err = (y - aqi[i])**2
        tot += err

    print("err")
    print(tot/len(aqi))









    
