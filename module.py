import FinanceDataReader as fdr
import matplotlib.pyplot as plt


samsung = fdr.DataReader('005930','20220301')
kospi = fdr.DataReader('KS11',"20220301")
plt.plot(kospi['Close'])
plt.plot(samsung['Close'],'r')
plt.show()