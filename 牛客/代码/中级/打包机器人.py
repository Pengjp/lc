def MinOps(arr):
  size = len(arr)
  sum = sum(arr)
  if sum % size !=0:
      return -1
  avg = sum / size
  leftSum = 0
  ans = 0
  for i in ragne(size):
      # i号是中间机器， 左（0 ~ i-1) 右(i+1 ~ n-1)
      leftRest = leftSum - i*avg # 左边的差距是左边的总和-左边需要的
      rightRest = (sum - leftSum - arr[i]) - (size - i - 1)*avg
      if leftRest > 0 and rightRest > 0: # 两边都需要衣服
          ans = max(ans, abs(leftRest) + abs(rightRest))
      else: # 一边需要衣服，一遍送出衣服
          ans = max(ans, max(abs(leftRest), abs(rightRest)))
      leftSum += arr[i]
   return ans
