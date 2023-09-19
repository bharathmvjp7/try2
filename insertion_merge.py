def merge_sort(lst):
    totalel=len(lst)
    if totalel > 1:
        mid = totalel // 2
        left_half=lst[:mid]
        print("Left half is",left_half)
        right_half = lst[mid:]
        print("Right half is",right_half)

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
    return lst


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr  


def initlist():
    my_list=[]
    num=int(input("enter the total number of Elelments to Sort\n"))
    for i in range(num):
        numelem=int(input("enter the number\n"))
        my_list.append(numelem)
    return my_list


while True:
    sel=int(input("enter 1---Insertion Sort,2--Merge Sort,3--Exit\n"))
    if sel ==3:
        break
    elif sel ==1:
        my_list=initlist()
        print("\nUnsorted List before Insertion Sort")
        print(my_list)
        insprt=insertion_sort(my_list)
        print("After Insertion Sort",insprt)
    elif sel ==2:
        my_list=initlist()
        print("\nUnsorted List before Merge Sort")
        print(my_list)
        mrsort=merge_sort(my_list)
        print(mrsort)
    else:
        print("!!!SELECT THE CORRECT OPTION,either 1 or 2")
        break
