#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import random,time
from numba import jit
'''
冒泡排序算法及其优化
冒泡排序的基本特征是只能交换相邻的元素。
从下边界开始，一趟扫描下来，可以把当前最大值顶到上边界；
如果没有发生交换操作，则表示数组是有序的。
'''
 
#算法一：基本冒泡排序
@jit
def BubbleSort_1(arr):
    #外层循环累计排序轮数，同时控制待排序数组的上边界，即A[0..i]为待排序部分
    #内层循环扫描A[0..i-1]，比较相邻元素，并通过交换元素值的方式将最大值顶到最上方
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]: arr[j],arr[j+1] = arr[j+1],arr[j]
 
#算法二：冒泡排序改进，设置交换操作标志
@jit
def BubbleSort_2(arr):
    for i in range(len(arr)-1,0,-1):
        swapFlag = False #先假设未做交换操作
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapFlag = True  #设置交互操作标志
        if not swapFlag: break #无交换操作，表示已完成排序，退出循环
 
#算法二：双向冒泡(鸡尾酒排序)，因为未发生交换操作的区域是有序的，故每轮扫描下来可以更新上下边界，减少扫描范围
@jit
def BubbleSort_3(arr):
    low,high = 0,len(arr)-1
    while low < high:
        swapPos = low #先假设最后一次发生交换操作的位置为low
        for j in range(low,high): #顺序扫描A[low..high-1]
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapPos = j
        high = swapPos #修改待排序数组的上界为最后一次发生交换操作的位置
        for j in range(high,low,-1): #逆序扫描A[low+1..high]
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                swapPos = j
        low = swapPos #修改待排序数组的下界为最后一次发生交换操作的位置
start = time.time()

a = list(range(1,10000))

random.shuffle(a)
a.sort()
#BubbleSort_1(a) 
print(a)

end = time.time()
run = end-start
print(run)