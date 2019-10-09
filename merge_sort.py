def mergsort(list_a):
    if len(list_a) > 1:
        mid = len(list_a)//2
        left = list_a[:mid]
        right = list_a[mid:]
        mergsort(left)
        mergsort(right)
        i = j = k = 0
        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                list_a[k] = left[i]
                k += 1
                i += 1
            else:
                list_a[k] = right[i]
                k += 1
                j += 1
        while i < len(left):
            list_a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list_a[k] = right[j]
            j += 1
            k += 1
        return list_a


list_1 = [10, 2, 6, 7, 9, 1, 3, 5, 4, 8]
print(mergsort(list_1))
