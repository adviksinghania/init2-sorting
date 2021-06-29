#!/usr/bin/env python3
# mergesort.py


def merge_sort(list):
    # Store the length of the list
    list_length = len(list)

    # List with length less than is already sorted
    if list_length == 1:
        return list

    # Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point = list_length // 2

    # To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    # The merge_sort function returns a list composed of a sorted left and right partition.
    return merge(left_partition, right_partition)


# Takes in two lists and returns a sorted list made up of the content within the two lists
def merge(left, right):
    # Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output = []
    i = j = 0

    # Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # Compare the elements at every position of both lists during each iteration
        if left[i] < right[j]:
            # output is populated with the lesser value
            output.append(left[i])
            # Move pointer to the right
            i += 1
        else:
            output.append(right[j])
            j += 1

    # The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output


if __name__ == '__main__':
    unsorted_list = [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
    print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)
