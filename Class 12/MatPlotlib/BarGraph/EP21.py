import matplotlib.pyplot as plt
pr=[74.25,76.06,69.5,72.55,81.5]
plt.bar(range(len(pr)),pr,width=0.4)
plt.xlim(-2,10)
plt.title("Prices of ABC.Co")
plt.ylabel("Prices")
plt.show