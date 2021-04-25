# Idea is to use "building blocks" to build up all the other words

one_to_ten = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
ten_to_twenty = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

sum_of_lengths = 0

# Get lengths from 1-10
for j in range(0, 10):
  sum_of_lengths+=len(one_to_ten[j])

# Get lengths from 11-19
for j in range(0, 9):
  sum_of_lengths+=len(ten_to_twenty[j])

# Get lengths from 20-99
for k in range(20, 100):
  if(20<=k<=29):
    if(k==20): sum_of_lengths+=len(tens[0])
    else: sum_of_lengths+=len(tens[0]+one_to_ten[k-21])
  elif(30<=k<=39):
    if(k==30): sum_of_lengths+=len(tens[1])
    else: sum_of_lengths+=len(tens[1]+one_to_ten[k-31])
  elif(40<=k<=49):
    if(k==40): sum_of_lengths+=len(tens[2])
    else: sum_of_lengths+=len(tens[2]+one_to_ten[k-41])
  elif(50<=k<=59):
    if(k==50): sum_of_lengths+=len(tens[3])
    else: sum_of_lengths+=len(tens[3]+one_to_ten[k-51])
  elif(60<=k<=69):
    if(k==60): sum_of_lengths+=len(tens[4])
    else: sum_of_lengths+=len(tens[4]+one_to_ten[k-61])
  elif(70<=k<=79):
    if(k==70): sum_of_lengths+=len(tens[5])
    else: sum_of_lengths+=len(tens[5]+one_to_ten[k-71])
  elif(80<=k<=89):
    if(k==80): sum_of_lengths+=len(tens[6])
    else: sum_of_lengths+=len(tens[6]+one_to_ten[k-81])
  elif(90<=k<=99):
    if(k==90): sum_of_lengths+=len(tens[7])
    else: sum_of_lengths+=len(tens[7]+one_to_ten[k-91])

# Now use pattern of "i+hundred+and+num" to get values for 100s, 200s, etc.
one_to_99 = sum_of_lengths


hundreds = [ones + 'hundred' for idx,ones in enumerate(one_to_ten)]
# Pop the last item because it is "tenhundred" :')
hundreds.pop()

# Get lengths of all 100s+ numbers
sum_of_lengths += sum([(99*len(item+'and') + one_to_99) for i,item in enumerate(hundreds)])

# Haven't included "100", "200", etc. so doing that now
sum_of_lengths += sum(len(item) for item in hundreds) + len('onethousand')

print(sum_of_lengths)