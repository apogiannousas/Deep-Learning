import matplotlib.pyplot as plt
from statistics import mean, stdev
from scipy.optimize import curve_fit
import numpy as np


plt.figure(figsize=(18, 8))


for filename, title, index in [("u.data.prob", "MovieLens Subset (100K)", 1), ("ml-1m.train.rating.prob", "MovieLens (1M)", 2)]:
	plt.subplot(1, 2, index)

	with open(filename,"r") as f:
		str_num_of_user_ratings = f.readline()
		num_of_user_ratings = eval(str_num_of_user_ratings)

	for _ in range(int(0.05 * len(num_of_user_ratings))):
		num_of_user_ratings.remove(max(num_of_user_ratings))

	(n,x,bs) = plt.hist(num_of_user_ratings, ec="black", bins = 20, alpha=0.5)	
	binwidth = bs[0].get_width()/2
	plt.plot(x[:-1] + binwidth,n, color="red")
	plt.xlabel('# of users')
	plt.ylabel('# of ratings of one user')
	plt.title(f'Probability Distribution of {title}')

	m = mean(num_of_user_ratings)
	print("Mean is : ", m)
	print("Standard deviation is: ", stdev(num_of_user_ratings, m))

plt.show()
