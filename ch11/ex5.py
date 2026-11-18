import seaborn as sns
import matplotlib.pyplot as plt

notes = [8, 12, 15, 17, 10, 6, 11, 13, 9, 14, 12, 11, 10, 16, 7]

sns.set_theme(style="whitegrid")
sns.histplot(notes, bins=8, kde=True, color="#2e75b6")
plt.title("Distribution des notes")
plt.xlabel("Note (/20)")
plt.show()