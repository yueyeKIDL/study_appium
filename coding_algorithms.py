from random import choice

import numpy as np

arr = [1, 4, 2]


def bubble_sort(arr):
    """冒泡排序：逐个相邻元素比较并交换位置，依次冒泡出最大值"""
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:  # 判断初始列表，已经是完美排序列表，直接跳出
            break
    return arr


def selection_sort(arr):
    """选择排序：每一轮选择出一个最小值并交换位置"""
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:  # 规避初始假设最小索引，为真最小索引
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def quicksort(arr):
    """快速排序：选取基准值，划分出左侧（小于基准值）、右侧（大于基准值）数组"""
    if len(arr) < 2:
        return arr
    else:
        reference = arr.pop()
        min_arr = [i for i in arr if i <= reference]
        max_arr = [i for i in arr if i > reference]
        return quicksort(min_arr) + [reference] + quicksort(max_arr)


def binary_search(arr, target):
    """二分查找：折半查找"""

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1


def random_list():
    """生成随机列表"""
    return list(np.random.randint(66, size=6))


# 主函数
if __name__ == '__main__':
    print(bubble_sort(random_list()))
    print(selection_sort(random_list()))
    print(quicksort(random_list()))

    sorted_list = quicksort(random_list())
    random_num = choice(sorted_list)
    index = binary_search(sorted_list, random_num)
    print(f'随机数字：{random_num}， 在列表 {sorted_list} 中的索引第 {index} 位')
