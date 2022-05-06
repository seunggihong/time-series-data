import FinanceDataReader as fdr
import matplotlib.pyplot as plt

# Load data
def loadData(code,start=None,end=None):
    data = fdr.DataReader(code,start,end)
    return data

def graphBuild(data,category):
    plt.plot(data[category])
    plt.show()

def similarityMeasurement(data1, data2):
    return 

if __name__ == "__main__":
    data = loadData('KS11','20220301')
    graphBuild(data, 'Close')