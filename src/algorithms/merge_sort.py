
def merge_sort(list):

    print(f'sorting list: {list}')

    if len(list) == 1:
        return list

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    print(f'split in {left_sorted} and {right_sorted}')

    result_list = []

    for i in range(len(list)):
        if len(left_sorted) == 0:
            result_list.append(right_sorted.pop(0))
            continue
        if len(right_sorted) == 0:
            result_list.append(left_sorted.pop(0))
            continue

        if right_sorted[0] < left_sorted[0]:
            result_list.append(right_sorted.pop(0))
        else:
            result_list.append(left_sorted.pop(0))

    print(f'result list: {result_list}')

    return result_list


input1 = [83, 20, 9, 50, 115, 61, 17]
result1 = merge_sort(input1)
print(f'Merge sort: {input1} -> {result1}')
assert result1 == [9, 17, 20, 50, 61, 83, 115]

print('')

input2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
result2 = merge_sort(input2)
print(f'Merge sort: {input2} -> {result2}')
assert result2 == [17, 20, 26, 31, 44, 54, 55, 77, 93]
