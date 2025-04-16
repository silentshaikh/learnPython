from matplotlib import pyplot as plt
import random

# ab = random.random()*100
# print(ab)
# randUnif = random.uniform(4,10)*34
# print(randUnif)
# print(random.randint(2,10)*2)
# print(random.randrange(2,10,2)*2)
# print(random.getrandbits(1))
# print(random.choice("Hello World"))
# print(random.choices([1,2,3,4,5,6,7,8,9,10],k=11))
# print(random.sample([1,2,3,4,5,6,7,8,9,10],k=10))
# shufList = [1,2,3,4,5,6,7,8,9,10]
# random.shuffle(shufList)
# print(shufList)

print(random.gauss(50,10))

# mu = 50
# sigma = 10

# data = [random.gauss(mu, sigma) for _ in range(10000)]

# plt.hist(data, bins=50, density=True, alpha=0.6, color='b')
# plt.title("Gaussian Distribution (mu=0, sigma=1)")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

# import matplotlib.pyplot as plt

# Samxlabel("Scores")
# plt.ylabel("Number of Students")
# plt.title("Student Score Distribution")
# plt.show()ple student scores
# scores = [50, 72, 68, 50, 75, 90, 50, 40, 90, 50, 71, 69]

# # Plot a histogram to see distribution
# plt.hist(scores, bins=5, edgecolor="black")
# plt.

import numpy as np

# Real student scores
# real_scores = [80, 85, 78, 80, 82, 90, 40, 50, 90, 85]

# # Real Mean & Standard Deviation
# real_mu = np.mean(real_scores)
# real_sigma = np.std(real_scores)

# print("📌 Real Mean:", real_mu)
# print("📌 Real Standard Deviation:", real_sigma)




# Predicting student scores using Gaussian
# predicted_scores = [random.gauss(70, 5) for _ in range(10)] # mostly (60-80)

# print("📌 Predicted Scores:", predicted_scores)

# plt.hist(predicted_scores, bins=50, density=True, alpha=0.6, color='b')
# plt.title("Gaussian Distribution (mu=0, sigma=1)")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

mu = 50
sigma_small = 5
sigma_large = 20

values_small = [random.gauss(mu, sigma_small) for _ in range(1000)]
values_large = [random.gauss(mu, sigma_large) for _ in range(1000)]

# Plot histogram
# plt.hist(values_small, bins=30, alpha=0.5, label="sigma = 5", color="blue")
plt.hist(values_large, bins=30, alpha=0.5, label="sigma = 20", color="red")
plt.legend()
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Effect of sigma on distribution")
plt.show()
