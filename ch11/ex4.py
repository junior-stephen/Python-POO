import matplotlib.pyplot as plt

semaines = list(range(1, 11))
notes = [11.5, 11.0, 10.0, 9.5, 10.5, 12.0, 11.0, 13.0, 12.5, 14.0]
presence = [90, 85, 92, 80, 88, 95, 70, 90, 85, 98]

fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)

axes[0].plot(semaines, notes, color="#1f4e79")
axes[0].set_ylabel("Note (/20)")
axes[0].set_title("Notes et présence")

axes[1].bar(semaines, presence, color="#2e75b6")
axes[1].set_ylabel("Présence (%)")
axes[1].set_xlabel("Semaine")

plt.tight_layout()
plt.show()