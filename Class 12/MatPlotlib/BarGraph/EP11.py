import matplotlib.pyplot as plt
Info=['Gold','Silver','Bronze','Total']
Aus=[80,59,59,198]
plt.bar(Info,Aus)
plt.xlabel("Medal Type")
plt.ylabel("Australia medal count")
plt.title("Australia Medal Tally")
plt.show()