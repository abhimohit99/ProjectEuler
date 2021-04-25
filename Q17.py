# Idea is to use "building blocks" to build up all the other words

one_to_ten = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
ten_to_twenty = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

sum_1_to_99 = 0

# Get lengths from 1-10
for j in range(0, 10):
  sum_1_to_99+=len(one_to_ten[j])

# Get lengths from 11-19
for j in range(0, 9):
  sum_1_to_99+=len(ten_to_twenty[j])

# Get lengths from 20-99
for i in range(0,8):
  # Get "20", "30", etc.
  sum_1_to_99+=len(tens[i])
  for k in range(0, 9):
    # Get "21", "22", etc.
    sum_1_to_99+=len(tens[i]+one_to_ten[k])

# Now use pattern of "i+hundred+and+num" to get values for 100s, 200s, etc.
hundreds = [ones + 'hundred' for idx,ones in enumerate(one_to_ten)]
# Pop the last item because it is "tenhundred" :')
hundreds.pop()

# First include lengths from 1-99
sum_of_lengths = sum_1_to_99

# Then get lengths of all 100s+ numbers
sum_of_lengths += sum([(99*len(item+'and') + sum_1_to_99) for i,item in enumerate(hundreds)])

# Haven't included "100", "200", etc. so doing that now
sum_of_lengths += sum(len(item) for item in hundreds) + len('onethousand')

print(sum_of_lengths)
