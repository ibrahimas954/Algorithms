def breakingRecords(scores):
	min_count = 0
	max_count = 0
	min_score = scores[0]
	max_score = scores[0]

	for i in range(len(scores)):
		if min_score < scores[i]:
		   min_count += 1
		if max_score > scores[i]:
		   max_count += 1

return min_count,max_count
