def str_com(s):
    cur = s[0]
    cnt = 1
    res = ''
    for i in s[1:]:
        if i == cur:
            cnt += 1
        else:
            res += cur
            res += str(cnt)
            cnt = 1
        cur = i
    res += cur
    res += str(cnt)
    return res

def gen_compressed_str(string):
  ind = 0
  comp_str = ""
  len_str = len(string)
  while (ind != len_str):
    count = 1
    # increment ind until we found a different char
    while ((ind < (len_str-1)) and (string[ind] == string[ind+1])):
      count = count + 1
      ind = ind + 1

    if (count == 1):
      comp_str = comp_str + str(string[ind])
    else:
      comp_str = comp_str + str(string[ind]) + str(count)

    ind = ind + 1

  return comp_str

print(str_com('abcaaabbb') == 'a1b1c1a3b3')
print(gen_compressed_str('abcaaabbb'))
