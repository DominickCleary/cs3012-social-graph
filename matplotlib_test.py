import matplotlib.pyplot as plt
import numpy as np
import mplcursors

ages = [22, 67, 34, 144, 155, 5, 1, 57, 123, 67, 123, 12, 645, 12]

ids = [x for x in range(len(ages))]

plt.bar(ids, ages)

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Other name')
plt.legend()

mplcursors.cursor(highlight=True, hover=True)

plt.show()