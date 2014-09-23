import matplotlib.pyplot as plt

t11 = ['aa','bba','cva']

t12 = [42,75,97]


plt.bar(range(len(t12)), t12, align='center')
plt.xticks(range(len(t12)), t11, size='large')
plt.show()