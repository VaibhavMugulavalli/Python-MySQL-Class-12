import matplotlib.pyplot as plt
Info=['Gold','Silver','Bronze','Total']
Aus=[80,59,59,198]
Ind=[26,20,20,66]
plt.bar(Info,Aus)
plt.bar(Info,Ind)
plt.xlabel("Medal Type")
plt.ylabel("Medal Tally")
plt.show()