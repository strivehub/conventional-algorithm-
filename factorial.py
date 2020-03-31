#这是一个利用python实现一个简单递归问题：阶乘

def factorial(num):  #定义函数
	if num == 1:  #如果输入数字为1了说明已经到最后了
		return num  #直接返回
	else:
		return num*factorial(num-1)  #如果不为1，则一直执行

if __name__ == "__main__":
	print(factorial(3))
