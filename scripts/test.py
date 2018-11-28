input_list = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0]
counter = 0
i = 0
first_index = 0
min_length = 5

while True:
	if i >= len(input_list):
		break
	if input_list[i] == 1:
		i += 1
	else:
	 	counter = 0
		first_index = i
		while input_list[i] == 0:
			i += 1	
			counter += 1
			if i >= len(input_list):
				break
		last_index = i
		if counter < min_length:
			while first_index < last_index:
				input_list[first_index] = 1
				first_index += 1	

output_list = input_list
output_list = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
left_first_empty = -1
right_first_empty = -1
for i in reversed(range(len(output_list)//2)):
	if output_list[i] == 0:
		left_first_empty = i
		break

for i in range(len(output_list)//2, len(output_list)):
	if output_list[i] == 0:
		right_first_empty = i
		break

print(output_list)
print(left_first_empty)
print(right_first_empty)
print(input_list)
