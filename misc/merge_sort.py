def msort(lst):
	if not lst:
		return []
	if len(lst) == 1:
		return lst
	else:
		first_half = lst[0:len(lst)/2]
		second_half = lst[len(lst)/2:]
		return merge(msort(first_half), msort(second_half))

def merge(lsta, lstb):
	"""
	loop over lsta and lstb to create sorted array
	"""
	new_lst = []
	current_a_index = 0
	current_b_index = 0

	print "lsta: ", lsta
	print "lstb: ", lstb

	while len(new_lst) != (len(lsta) + len(lstb)):
		if len(lsta) == current_a_index:
			new_lst.append(lstb[current_b_index])
			current_b_index += 1
		elif len(lstb) == current_b_index:
			new_lst.append(lsta[current_a_index])
			current_a_index += 1
		elif lsta[current_a_index] < lstb[current_b_index]:
			new_lst.append(lsta[current_a_index])
			current_a_index += 1
		elif lsta[current_a_index] > lstb[current_b_index]:
			new_lst.append(lstb[current_b_index])
			current_b_index += 1

	print "new list: ", new_lst
	return new_lst

ques = [4,3,8,6,7,1,2,9,5]
sol = [1,2,3,4,5,6,7,8,9]
mysol = msort(ques)

print ""
print "ques: ", ques
print "sol: ", sol
print "mysol: ", mysol
print "correct: ", sol == mysol