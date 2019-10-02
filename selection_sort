def selection(current_list):
    for i in range(len(current_list)):
        smallest_index = i
        for j in range(i+1, len(current_list)):
            if current_list[smallest_index] > current_list[j]:

                smallest_index = j

        current_list[smallest_index], current_list[i] = current_list[i], current_list[smallest_index]
        print(current_list)


list_2= [7, 5, 9, 1, 2, 4, 3, 6, 10]
selection(list_2)
