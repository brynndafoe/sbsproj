def split_by_sign(lst, low, high):
    if low == high:
        return
    i = low
    while i < high:
        if lst[i] > 0:
            break
        else:
            i += 1
    if i == high:
        return
    j = high
    while j >= low:
        if lst[j] < 0:
            break
        else:
            j -= 1
    if j < low:
        return
    if i >= j:
        return
    else:
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp
        split_by_sign(lst, i + 1, j - 1)

if __name__ == "__main__":
    lst = [-5, -2, 3, 7, -1, 4]
    print("Original list:", lst)
    split_by_sign(lst, 0, len(lst) - 1)
    print("List after split by sign:", lst)

