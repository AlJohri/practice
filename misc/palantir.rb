def frequentCharacters(input,  frequencyThreshold)
    input.split("").group_by { |x| x }.values.select { |x| x.size >= frequencyThreshold }.map { |x| x.first }.sort.join("")
end

def sumThreeSmallest(input)
	return input.reduce(:+) if input.length < 3
	smallest = 1000
	second_smallest = 999
	third_smallest = 998
	for number in input
		if number < smallest
			temp1 = smallest
			smallest = number
			if temp1 < second_smallest
				temp2 = second_smallest
				second_smallest = temp1
				if temp2 < third_smallest
					third_smallest = temp2
				end
			end
		elsif number < second_smallest # || smallest >= second_smallest
			temp = second_smallest
			second_smallest = number
			if temp < third_smallest # || second_smallest >= third_smallest
				third_smallest = temp
			end
		elsif number < third_smallest # || second_smallest >= third_smallest
			third_smallest = number
		end
	end
	# print smallest, second_smallest, third_smallest
	return [smallest, second_smallest, third_smallest].reduce(:+)
end

_input_cnt = Integer(gets)
_input_i=0
_input = Array.new(_input_cnt)

while (_input_i < _input_cnt)
    _input_item = Integer(gets);
    _input[_input_i] = (_input_item)
    _input_i+=1
end

res = sumThreeSmallest(_input);
print res;

# puts sumThreeSmallest([4,2,1,3,5,0])
# puts sumThreeSmallest([1,2,3,4,5,6,7,8])
# puts sumThreeSmallest([3,3,3,2,2,2,1,1,1])
# puts sumThreeSmallest([-1,-2,-3,-4,-5,-6])
# puts sumThreeSmallest([5,-1,-1,0,2,3])

# ----------------------------------- #

# iter 0
# 1 2 3 4 5
# smallest = 1
# second_smallest = 1
# third_smallest = 1

# ----------------------------------- #

# iter 0
# 4 2 1 3 5 0
# smallest = 4
# second_smallest = 4
# third_smallest = 4

# iter 1
# 4 2 1 3 5 0
# smallest = 2
# second_smallest = 4
# third_smallest = 4

# iter 2
# 4 2 1 3 5 0
# smallest = 1
# second_smallest = 2
# third_smallest = 4

# iter 3
# 4 2 1 3 5 0
# smallest = 1
# second_smallest = 2
# third_smallest = 3

# iter 4 (nothing)
# 4 2 1 3 5 0
# smallest = 1
# second_smallest = 2
# third_smallest = 3

# iter 5
# 4 2 1 3 5 0
# smallest = 0
# second_smallest = 1
# third_smallest = 2
