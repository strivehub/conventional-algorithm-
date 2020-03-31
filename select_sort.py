#这是一个用python实现的选择排序算法

def select_sort(arr):
    for i in range(len(arr)):  #遍历整个数组
        min_index = i  #记录最小值的索引，这里假设为i
        for j in range(i+1,len(arr)):  #遍历除去索引后面的值
            if arr[min_index]>arr[j]:  #如果取值比我们预先设定的小，则更新min_index，使之一直记录的是最小值的索引
                min_index = j  #更新
        arr[i],arr[min_index] = arr[min_index],arr[i]  #将最小值交换到前面
    return arr

if __name__ == "__main__":
    arr = [2,4,1,8,0,4,9]
    print(select_sort(arr))