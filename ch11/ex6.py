import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

notes_df = pd.DataFrame({
    "Maths": [12, 15, 9, 14, 11, 16, 8, 13, 10, 17],
    "Algo":  [11, 16, 10, 13, 12, 15, 9, 14, 10, 18],
    "Anglais": [14, 10, 12, 9, 15, 11, 13, 10, 16, 12],
})

corr = notes_df.corr()
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", vmin=-1, vmax=1, square=True)
plt.title("Corrélation entre les notes des matières")
plt.show()