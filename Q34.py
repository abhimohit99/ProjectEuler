import math

sum_of_sums = 0
for idx in range(100,100000):
  digit_sum = sum(math.factorial(int(i)) for i in str(idx))
  if(digit_sum == idx):
      print("WHOA! " + str(digit_sum) + " sum of " + str(idx))
      sum_of_sums += idx

print(sum_of_sums)