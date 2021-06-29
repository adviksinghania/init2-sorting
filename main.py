import mergesort

unsorted_list = list(map(int, input().split()))
print(unsorted_list)
sorted_list = mergesort.merge_sort(unsorted_list)
print(sorted_list)
