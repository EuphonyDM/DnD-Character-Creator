def insertionSort(array):
    for index in range(1, len(array)):
        position = index
        current = array[index]
        while array[position] < array[position-1]and position > 0:
            array[position] = array[position-1]
            position -= 1
        array[position] = current
    return array

