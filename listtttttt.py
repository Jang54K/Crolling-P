def selection_sort(list):
    for a in range(len(list)):
        for b in range(len(list)-1):
            if list[b]>list[b+1]:
                temp = list[b+1]
                list[b+1] = list[b]
                list[b] = temp
            else:
                pass

real_list = [21, 73, 40, 11, 5, 55, 32, 94, 68, 49, 83]
print("현재 리스트는 아래와 같습니다.\n", real_list);

selection_sort(real_list)
print("\n정렬된 리스트는 아래와 같습니다.\n",real_list);
