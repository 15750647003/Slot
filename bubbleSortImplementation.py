def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后 i 个元素已经是排好序的
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
print("原始数组是:", arr)

bubble_sort(arr)
print("冒泡排序后的数组是:", arr)