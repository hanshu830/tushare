import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_history_data(code):
    return ts.get_hist_data(code)


def total_gained(code):
    df = get_history_data(code)
    tlist = []
    total_change = 0;
    for i in range(df['p_change'].size):
       # print str(i)+", "+str(df['p_change'][i])+", "+str(df.index[i])
       total_change = total_change + df['p_change'][-i-1]
       # print "total_change: "+str(total_change)
       tlist.append(total_change)

    tlist.reverse();
    df['total_gained'] = tlist
    return df


if __name__ == "__main__":
    import sys
    print sys.argv

    zgpa = total_gained('601318')
    plt.plot(zgpa['total_gained'])
    sh = total_gained('sh')
    plt.plot(sh['total_gained'])
    sz50 = total_gained('sz50')
    plt.plot(sz50['total_gained'])
    cyb = total_gained('cyb')
    #plt.plot(cyb['total_gained'])
    plt.show()

