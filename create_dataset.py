import pandas as pd
import numpy as np
import config
import random

filename = "u.data"
dataset = "ourdata"
data_path = config.main_path

train_filename = data_path + "{}.train.rating".format(dataset)
test_rating = data_path + '{}.test.rating'.format(dataset)
test_negative = data_path + '{}.test.negative'.format(dataset)

file_dataframe = pd.read_csv(
	data_path + filename,
	sep='\t', header=None, names=['user', 'item', 'timestamp'], 
	usecols=[0, 1, 3], dtype={0: np.int32, 1: np.int32, 3: np.int32})

# print(file_dataframe.head())

item_ids = []
interactions_dict = {}

for index, entry in file_dataframe.iterrows():
	if(entry['user'] not in interactions_dict.keys()):
		interactions_dict[entry['user']] = []
	
	interactions_dict[entry['user']].append([entry['item'],entry['timestamp']])

for key in interactions_dict.keys():
	interactions_dict[key] = sorted(interactions_dict[key], key=lambda x: x[1])

myKeys = list(interactions_dict.keys())
myKeys.sort()
interactions_dict = {i: interactions_dict[i] for i in myKeys}

# Create list with all unique item ids
for key in interactions_dict.keys():
	for item, timestamp in interactions_dict[key]:
		if item not in item_ids:
			item_ids.append(item)

item_ids = set(item_ids)

# Create test negative dataset
negative_samples = pd.DataFrame()

for user in interactions_dict.keys():
	last_element = interactions_dict[user][-1]
	item_interactions = {i[0] for i in interactions_dict[user]}
	
	sample_space = item_ids - item_interactions
	samples = random.sample(sample_space, k=100)
	
	# add the tuple of the user interaction
	new_negative_entry = [str((user, last_element[0]))]

	# add the negative samples to the array
	for sample in samples:
		new_negative_entry.append(sample)

	new_negative_entry = pd.Series(new_negative_entry)

	# add the row to the dataset
	negative_samples = pd.concat([negative_samples, new_negative_entry], axis=1)

negative_samples = negative_samples.T

negative_samples.to_csv(test_negative, sep='\t', index=False, index_label=None, header=False)

# Create training dataset
training_df = pd.DataFrame([(k, val[0]) for k, vals in interactions_dict.items() for val in vals[0:-1]])

training_df.to_csv(train_filename, sep='\t', index=False, index_label=None, header=False)