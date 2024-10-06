import unittest

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
                #swap of the element at i and min index
                arr[i], arr[min_index] = arr[min_index],arr[i]
    return arr

class TestSelectionSort(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        result = selectionSort(arr)
        self.assertEqual(result, arr)

    def test_single_element_array(self):
        arr = [5]
        result = selectionSort(arr)
        self.assertEqual(result, arr)

    def test_sorted_array(self):
        arr = [1,2,3,4,5]
        result = selectionSort(arr)
        self.assertEqual(result, arr)

    def test_reverse_sorted_array(self):
        arr = [5,4,3,2,1]
        result = selectionSort(arr)
        self.assertEqual(result, arr)

    def test_array_with_duplicates(self):
        arr = [5,4,3,2,1,1,3]
        result = selectionSort(arr)
        self.assertEqual(result, arr)

    def test_array_with_negative_numbers(self):
        arr = [-5,-4,-3,-2,-1,0,1,2,3,4]
        result = selectionSort(arr)
        self.assertEqual(result, arr)

if __name__ == '__main__':
    unittest.main()