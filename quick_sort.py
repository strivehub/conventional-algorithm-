def quick_sort(arr):
  if len(arr)<2:  #判断数组长度，如果数组里面只有一个元素，则不需要排序，直接返回
    return arr
  else:  #如果长度大于2个及以上，则需要排序
    value = arr[0]  #设定一个基准值，这里我们每次都取数组第一个，也阔以取数组其他值
    min_value = [i for i in arr[1:] if i <=value]  #将数组中小于等于基准值放在这个数组中
    max_value = [i for i in arr[1:] if i>value]  #将数组中大于基准值的放在这里
    return quick_sort(min_value)+[value]+quick_sort(max_value)  #循环以上步骤，数组将被我们分的越来越小，最后只剩下一个的时候就结束了
    

if __name__ == "__main__":
  arr = [3,5,1,7,9,0] #定义数组
  print(quick_sort(arr))  #调用排序函数
