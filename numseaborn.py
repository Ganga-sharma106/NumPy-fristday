import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5]) 
# displot - distribution plot

plt.show()
# renders the generated plot



sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()