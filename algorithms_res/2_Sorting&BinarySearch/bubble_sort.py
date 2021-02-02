def bubble_sort(nums):  

    count = 0

    swapped = True

    while swapped:

        swapped = False

        for i in range(len(nums) - 1):

            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                count += 1
                swapped = True

    return count
# Verify it works

print(bubble_sort(s))
