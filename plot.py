import matplotlib.pyplot as plt

wanted_plot = 'num_neg' #'top_k' or 'num_neg'

hr_top_k     = [0.182, 0.276, 0.366, 0.428, 0.472, 0.534, 0.565, 0.599, 0.622, 0.657]
ndgc_top_k   = [0.182, 0.236, 0.283, 0.307, 0.332, 0.348, 0.348, 0.371, 0.373, 0.388]
hr_num_neg   = [0.639, 0.667, 0.653, 0.653, 0.646, 0.645, 0.668, 0.648, 0.666, 0.646]
ndgc_num_neg = [0.363, 0.381, 0.375, 0.378, 0.373, 0.385, 0.382, 0.387, 0.385, 0.372]
X = [1,2,3,4,5,6,7,8,9,10]

if wanted_plot == 'top_k':
	hr = hr_top_k
	ndgc = ndgc_top_k
else:
	hr = hr_num_neg
	ndgc = ndgc_num_neg

plt.figure(figsize=(18, 8))


#----------- HR ------------#
plt.subplot(1, 2, 1)
plt.plot(X, hr, label='HR', color='red', linestyle='dashed', linewidth = 1,
		marker='^', markerfacecolor='red', markersize=5)

for x,y in zip(X, hr):
	label = "{:.3f}".format(y)
	plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

if wanted_plot == 'top_k':
	plt.xlabel('K value')
	plt.ylabel('HR@K Accuracy')
	plt.title('HR@K vs K')
else:
	plt.xlabel('Number of Negatives')
	plt.ylabel('HR@10 Accuracy')
	plt.title('HR@10 vs Number of Negatives')

#----------- NDGC ------------#
plt.subplot(1, 2, 2)

plt.plot(X, ndgc, label='NDGC', color='blue', linestyle='dashdot', linewidth = 1,
		marker='s', markerfacecolor='blue', markersize=5)

for x,y in zip(X, ndgc):
	label = "{:.3f}".format(y)
	plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

if wanted_plot == 'top_k':
	plt.xlabel('K value')
	plt.ylabel('NDGC@K Accuracy')
	plt.title('NDGC@K vs K')
else:
	plt.xlabel('Number of Negatives')
	plt.ylabel('NDGC@10 Accuracy')
	plt.title('NDGC@10 vs Number of Negatives')

plt.savefig(wanted_plot + ".png")
plt.show()