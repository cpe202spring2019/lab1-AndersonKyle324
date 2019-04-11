import copy

def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if len(int_list) > 0:
      max = int_list[0]
      for i in int_list:
         if i > max:
            max = i
      return max
   else:
      return None

def reverse_rec(int_list, rev_list=[], spot=0, count=0):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
      
   if count == 0:
      rev_list = []
      spot = len(int_list) - 1
      count += 1
   if spot >= 0:
      rev_list.append(int_list[spot])
      spot -= 1
      if spot < 0:
         return rev_list
   return reverse_rec(int_list, rev_list, spot, count)


def bin_search(target, low, high, int_list, n=0):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError
   
   if int_list[n] != target and n == 0:
      n = (high - low)//2 + low 
      
   if int_list[high-1] < target or int_list[low] > target:
      return None
   elif int_list[n] == target:
      return n
   elif int_list[n] > target:
      if n-1 >= 0 and int_list[n-1] < target:
         return None
      subN = (n-low)//2
      if subN == 0:
         subN = 1
      n -= subN
   elif int_list[n] < target:
      if n+1 <= len(int_list)-1 and int_list[n+1] > target:
         return None
      addN = (high-n)//2
      if addN == 0:
         addN = 1
      n += addN
   return bin_search(target, low, high, int_list, n)
      