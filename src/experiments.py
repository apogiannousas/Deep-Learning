# Oh, hello... Didn't see you there... Let's run some experiments (https://media.istockphoto.com/id/91811358/photo/crazy-scientist.jpg?s=612x612&w=0&k=20&c=jiCROB2JZzt5e05CtKGNDbHHYba7FrBc64mgM-PjNys=)
# For the sake of keeping things simple, I will not import the other python files
# I will run them as a new process
import os
from statistics import mean 

do_first = True # CHristo kanto false

if do_first:
	print("----- First experiment: HR@K vs K -----")
	print("---------------- and ------------------")
	print("--- Second experiment: NDCG@K vs K ---")
	# First experiment: HR@K vs K
	# Second experiment: NDCG@K vs K
	ndcg = []
	hr = []

	for k in range (5,11):
		ndcg_tmp = []
		hr_tmp = []
		
		for i in range(5):
			print(i)
			cmd = f"python3 main.py --top_k {k} > tmp.out 2> /dev/null"
			os.system(cmd)
		
			
			with open("tmp.out", "r") as f:
				last_line = f.readlines()[-1]
			last_line = last_line.split(" = ")
			ndcg_tmp.append(float(last_line[-1].strip()))
			hr_tmp.append(float(last_line[1].split(", ")[0].strip()))

		ndcg_tmp.remove(max(ndcg_tmp))
		ndcg_tmp.remove(min(ndcg_tmp))
		hr_tmp.remove(max(hr_tmp))
		hr_tmp.remove(min(hr_tmp))

		ndcg.append(mean(ndcg_tmp))
		hr.append(mean(hr_tmp))
		print(ndcg_tmp, hr_tmp)
		print(f"-> k == {k}: hr = {hr[-1]}, ndgc = {ndcg[-1]}")


	print("HR@K vs K: ", ndcg)
	print("NDCG@K vs K: ", hr)
else:
	# Third experiment: HR@10 vs num_ng
	# Fourth experiment: ndcg@10 vs num_ng
	print("----- Third experiment: HR@10 vs num_ng -----")
	print("------------------- and ---------------------")
	print("--- Fourth experiment: ndcg@10 vs num_ng ---")
	ndcg = []
	hr = []

	for n in range (6,11):
		ndcg_tmp = []
		hr_tmp = []
		for i in range(5):
			print(i)
			cmd = f"python3 main.py --top_k 10 --num_ng {n} > tmp.out 2> /dev/null"
			os.system(cmd)

			with open("tmp.out", "r") as f:
				last_line = f.readlines()[-1]
				last_line = last_line.split(" = ")
				ndcg_tmp.append(float(last_line[-1].strip()))
				hr_tmp.append(float(last_line[1].split(", ")[0].strip()))

		ndcg_tmp.remove(max(ndcg_tmp))
		ndcg_tmp.remove(min(ndcg_tmp))
		hr_tmp.remove(max(hr_tmp))
		hr_tmp.remove(min(hr_tmp))

		ndcg.append(mean(ndcg_tmp))
		hr.append(mean(hr_tmp))
		print(ndcg_tmp, hr_tmp)
		print(f"-> k == {k}: hr = {hr[-1]}, ndgc = {ndcg[-1]}")

	print("HR@10 vs num_ng: ", ndcg)
	print("NDCG@10 vs num_ng: ", hr)
